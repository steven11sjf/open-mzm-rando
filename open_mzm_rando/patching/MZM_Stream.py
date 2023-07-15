import io


class MZM_Stream:
    stream: io.BytesIO

    def __init__(self, stream: io.BytesIO):
        self.stream = stream

    def seek(self, offset: int):
        self.stream.seek(offset)
    
    def seek_from_current(self, offset: int):
        self.stream.seek(self.stream.tell() + offset)
    
    def follow_pointer(self):
        """Goes to the pointer highlighted"""
        ptr = self.read_Pointer()
        self.seek(ptr)

    def _read(self, size: int) -> bytes:
        return self.stream.read(size)
    
    def _write(self, data: bytes) -> int:
        return self.stream.write(data)

    def read_UInt8(self) -> int:
        return int.from_bytes(self._read(1), 'little', signed=False)
    
    def write_UInt8(self, val: int):
        self._write(val.to_bytes(1, 'little', signed=False))

    def read_UInt16(self) -> int:
        return int.from_bytes(self._read(2), 'little', signed=False)
    
    def write_UInt16(self, val: int):
        self._write(val.to_bytes(2, 'little', signed=False))

    def read_UInt32(self) -> int:
        return int.from_bytes(self._read(4), 'little', signed=False)

    def write_UInt32(self, val: int):
        self._write(val.to_bytes(4, 'little', signed=False))
    
    def read_Pointer(self) -> int:
        return self.read_UInt32() - 0x8000000
    
    def write_Pointer(self, ptr: int):
        self._write((ptr + 0x8000000).to_bytes(4, 'little'))