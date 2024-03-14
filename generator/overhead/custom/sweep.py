from utils import OverheadGenerator, OverheadValue


class SweepOverheadGenerator(OverheadGenerator):
    def __init__(self, start: int, end: int, size=1):
        if start > end:
            raise ValueError(f"start should be less than or equal to end")
        self.start: int = start
        self.end: int = end
        self.current: int = self.start
        self.size: int = size

    @property
    def next_value(self) -> OverheadValue:
        if self.current > self.end:
            self.current = self.start
        next_value: int = self.current
        self.current += 1
        return OverheadValue(binary_string=f"{next_value:08b}" * self.size)
