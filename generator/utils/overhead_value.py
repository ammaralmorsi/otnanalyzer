

class OverheadValue:
    """Represents an overhead value that can be queried in various formats."""

    def __init__(self, binary_string:str):
        """
        Initializes the OverheadValue object with the provided binary string.

        Args:
            binary_string (str): The binary string representation of the overhead value.
        """
        self._value:str = binary_string

    @property
    def as_binary_string(self) -> str:
        """
        Returns the binary string representation of the overhead value.

        Returns:
            str: The binary string representation of the overhead value.
        """
        return self._value

    @property
    def as_int(self) -> int:
        """
        Returns the integer representation of the overhead value.

        Returns:
            int: The integer representation of the overhead value.

        Raises:
            ValueError: If the size of the overhead value exceeds 8 bits.
        """
        if len(self.as_binary_string) > 8:
            raise ValueError("size of overhead value should not exceed 8 bits")
        if len(self.as_binary_string) == 0:
            return 0
        return int(self.as_binary_string, 2)

    @property
    def as_int_list(self) -> list[int]:
        """
        Returns a list of integers, each representing a byte of the overhead value.

        If the size of overhead value as a binary string is not multiple of 8,
        then the value will be *left* justified.

        Returns:
            list[int]: A list of integers representing each byte of the overhead value.
        """
        binary_string = self.as_binary_string
        padded_string = binary_string.zfill(len(binary_string) + (8 - len(binary_string) % 8) % 8)
        bytes_list = [padded_string[i:i+8] for i in range(0, len(padded_string), 8)]
        return [int(byte_str, 2) for byte_str in bytes_list]

    def __eq__(self, other):
        if isinstance(other, OverheadValue):
            return self._value == other._value
        return False
