from io import BytesIO

class AppendedData:
    data: bytearray
    size: int
    pointed_to_by: list[int]

    def __init__(self, data: bytearray, pointers: list[int]):
        self.data = data
        self.size = len(data)
        if pointers:
            self.pointed_to_by = pointers
        else:
            self.pointed_to_by = []
    
    def add_pointer(self, offset: int):
        self.pointed_to_by.append(offset)
    
    def write(self, stream: BytesIO, offset: int):
        stream.seek(offset)
        stream.write(self.data)

        for ptr in self.pointed_to_by:
            stream.seek(ptr)
            stream.write(offset + 0x80000000) # all pointers have 0x80 as last byte


class AppendedDataManager:
    all_data: list[AppendedData]

    def __init__(self) -> None:
        self.all_data = []
    
    def add_data(self, data: AppendedData):
        self.all_data.append(data)
    
    def write(self, stream: BytesIO, offset: int):
        current_off = offset

        for data in self.all_data:
            data.write(stream, current_off)
            current_off += data.size
