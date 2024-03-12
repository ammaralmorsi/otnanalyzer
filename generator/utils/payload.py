

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
