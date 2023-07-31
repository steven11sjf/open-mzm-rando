from __future__ import annotations

import dataclasses
from bisect import insort
from open_mzm_rando.patching.MZM_Stream import MZM_Stream
from open_mzm_rando.logger import LOG

@dataclasses.dataclass(kw_only=True)
class AppendableData:
    orig_size: int
    orig_address: int
    pointed_to_by: list[int]
    
    def add_pointer(self, offset: int):
        self.pointed_to_by.append(offset)
    
    def to_bytes(self) -> bytes:
        raise NotImplementedError
    
    

@dataclasses.dataclass()
class FreeRegion:
    start_address: int
    size: int
    
    def add_data(self, added_data_size: int):
        if self.size < added_data_size:
            raise ValueError(f"Data region overflowed by {self.size - added_data_size} bytes!")
        
        self.start_address += added_data_size
        self.size -= added_data_size
    
    def __lt__(self, other):
        return self.size < other.size

class AppendedDataManager:
    all_data: list[AppendableData]
    stream: MZM_Stream
    free_regions: list[FreeRegion]

    def __init__(self, stream: MZM_Stream) -> None:
        self.all_data = []
        self.stream = stream
        self.free_regions = [ FreeRegion(start_address=0x7f7734, size=0x88cc) ]
    
    def add_data(self, data: AppendableData):
        self.all_data.append(data)
    
    def write_all(self):
        # sort all AppendableData big to small
        self.all_data.sort(reverse=True)

        # place each AppendableData
        while len(self.all_data) != 0:
            asset = self.all_data.pop(0)
            self.write_immediate(asset)
    
    def write_immediate(self, asset: AppendableData) -> int:
        binary = asset.to_bytes()
        size = len(binary)

        # remove from all_data
        if asset in self.all_data:
            self.all_data.remove(asset)
        
        # add data
        if size <= asset.orig_size:
            # write in place
            self.stream.seek(asset.orig_address)
            self.stream._write(binary)
            return asset.orig_address
        else:
            # add the AppendableData's original data region to free_regions, and write it somewhere with space
            insort(self.free_regions, FreeRegion(asset.orig_address, size))
            return self._write_to_open_region(asset.pointed_to_by, binary)
        

    def _write_to_open_region(self, pointers: list[int], bytes: bytes) -> int:
        # find the smallest data region that will fit this data
        region: FreeRegion = None
        length = len(bytes)
        for dr in self.free_regions:
            if length <= dr.size:
                region = dr
                break
        
        if region is None:
            raise ValueError("No region can fit asset!")
        
        # pop the data region, write the new data
        self.free_regions.pop(self.free_regions.index(region))
        new_address = region.start_address
        self.stream.seek(new_address)
        self.stream._write(bytes)
        region.add_data(len(bytes))

        # only keep this region in open_data_regions if it's big enough to be realistically used by something
        if region.size > 0x30:
            insort(self.free_regions, region)

        # point everything to the AppendableRegion
        for ptr in pointers:
            self.stream.seek(ptr)
            self.stream.write_Pointer(new_address)
        
        return new_address
