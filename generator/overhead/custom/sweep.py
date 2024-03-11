from generator.utils import OverheadValue


class SweepOverheadGenerator:
    def __init__(self, start:int, end:int):
        if start > end:
            raise ValueError(f"start should be less than or equal to end")
        self.start:int = start
        self.end:int = end
        self.current:int = self.start

    def get_next_value(self) -> OverheadValue:
        if self.current > self.end:
            self.current = self.start
        next_value:int = self.current
        self.current += 1
        return OverheadValue(binary_string=f"{next_value:08b}")
