from utils import Position, Dimension
from config import OtuOverheads
from .odu import OduFrameGenerator


class OtuFrameGenerator:
    def __init__(self, odu_frame_generator: OduFrameGenerator):
        self.dimension:Dimension = Dimension(nrows=4, ncols=3824)
        self.odu_frame:OduFrameGenerator = odu_frame_generator
        self.odu_position:Position = Position(row=0, col=0)  # because odu and otu have the same size
        self._frame:list[list[int]] = [
            [0 for _ in range(self.dimension.ncols)]
            for _ in range(self.dimension.nrows)
        ]

    def get_next_frame(self) -> list[list[int]]:
        odu_frame: list[list[int]] = self.odu_frame.get_next_frame()
        for rn in range(self.odu_frame.dimension.nrows):
            for cn in range(self.odu_frame.dimension.ncols):
                self._frame[self.odu_position.row + rn][self.odu_position.col + cn] = (
                    odu_frame[rn][cn]
                )
        for otn_field in OtuOverheads.get_fields(): 
            otn_field.generator = None
        return self._frame

    def __repr__(self) -> str:
        import numpy as np

        np.set_printoptions(edgeitems=18, linewidth=200)
        return repr(np.array(self._frame))
