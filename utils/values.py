

class OverheadValue:
    def __init__(self, binary_string:str):
        self._value:str = binary_string

    @property
    def as_binary_string(self) -> str:
        return self._value

    @property
    def as_int(self) -> int:
        if len(self.as_binary_string) > 8:
            raise ValueError("size of overhead value should not exceed 8 bits")
        if len(self.as_binary_string) == 0:
            return 0
        return int(self.as_binary_string, 2)

    @property
    def as_int_list(self) -> list[int]:
        binary_string = self.as_binary_string
        padded_string = binary_string.zfill(len(binary_string) + (8 - len(binary_string) % 8) % 8)
        bytes_list = [padded_string[i:i+8] for i in range(0, len(padded_string), 8)]
        return [int(byte_str, 2) for byte_str in bytes_list]

    @property
    def as_list_int(self) -> list[int]:
        return self.as_int_list

    def __eq__(self, other):
        if isinstance(other, OverheadValue):
            return self._value == other._value
        return False


class PayloadValue:
    def __init__(self, data:list[int]):
        self._value:list[int] = data

    @property
    def as_int_list(self) -> list[int]:
        return self._value

    def __eq__(self, other):
        if isinstance(other, PayloadValue):
            return self._value == other._value
        return False
