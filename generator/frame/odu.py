from utils import Position, Dimension
from config import OduOverheads
from .opu import OpuFrameGenerator


class OduFrameGenerator:
    def __init__(self, opu_frame_generator: OpuFrameGenerator):
        self.dimension: Dimension = Dimension(nrows=4, ncols=3824)
        self.opu_position: Position = Position(row=0, col=14)
        self.opu_frame: OpuFrameGenerator = opu_frame_generator
        self._frame: list[list[int]] = [
            [0 for _ in range(self.dimension.ncols)]
            for _ in range(self.dimension.nrows)
        ]

    def get_next_frame(self) -> list[list[int]]:
        opu_frame: list[list[int]] = self.opu_frame.get_next_frame()
        for rn in range(self.opu_frame.dimension.nrows):
            for cn in range(self.opu_frame.dimension.ncols):
                self._frame[self.opu_position.row + rn][self.opu_position.col + cn] = (
                    opu_frame[rn][cn]
                )
        for otn_field in OduOverheads.get_fields():
            otn_field.generator = None
        return self._frame
