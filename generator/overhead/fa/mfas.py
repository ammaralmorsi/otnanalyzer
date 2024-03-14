from utils import OverheadGenerator, OverheadValue


class MFASOverheadGenerator(OverheadGenerator):
    def __init__(self):
        self.current_frame_number = 0

    @property
    def next_value(self) -> OverheadValue:
        next_value = self.current_frame_number
        self.current_frame_number = (self.current_frame_number + 1) % 256
        return OverheadValue(binary_string=f"{next_value:08b}")
