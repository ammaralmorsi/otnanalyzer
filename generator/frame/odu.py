from generator.utils import Position
from generator.utils import Dimension
from generator.utils.frame import OduOverheads
from .opu import OpuFrameGenerator


class OduFrameGenerator:
    def __init__(self, opu_frame_generator: OpuFrameGenerator):
        self.dimension: Dimension = Dimension(nrows=4, ncols=3824)
        self.opu_frame: OpuFrameGenerator = opu_frame_generator
        self.opu_position: Position = Position(row=0, col=14)
        self.overheads: OduOverheads = OduOverheads()
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
        for otn_field in self.overheads:
            field_data = otn_field.generator.get_next_value().as_int_list
            for cn in range(otn_field.dimension.ncols):
                self._frame[otn_field.position.row][otn_field.position.col + cn] = (
                    field_data[cn]
                )
        return self._frame

    def __repr__(self) -> str:
        import numpy as np

        np.set_printoptions(edgeitems=18, linewidth=200)
        return repr(np.array(self._frame))
