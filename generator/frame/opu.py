from generator.utils import OtnField, Dimension, Position
from generator.utils.frame import OpuOverheads
from generator.payload.prbs import PRBSPayloadGenerator


class OpuFrameGenerator:
    def __init__(self, seed=2):
        self.dimension: Dimension = Dimension(nrows=4, ncols=3810)
        self.overheads: OpuOverheads = OpuOverheads()
        self.payload: OtnField = OtnField(
            name="prbs",
            position=Position(col=2, row=0),
            dimension=Dimension(nrows=4, ncols=3808),
            generator=PRBSPayloadGenerator(seed),
        )
        self._frame: list[list[int]] = [
            [0 for _ in range(self.dimension.ncols)]
            for _ in range(self.dimension.nrows)
        ]

    def get_next_frame(self) -> list[list[int]]:
        payload: list[int] = self.payload.generator.get_next_value().as_int_list
        for rn in range(self.payload.dimension.nrows):
            for cn in range(self.payload.dimension.ncols):
                self._frame[self.payload.position.row + rn][
                    self.payload.position.col + cn
                ] = payload[rn * self.dimension.nrows + cn]
        for otn_field in self.overheads:
            self._frame[otn_field.position.row][
                otn_field.position.col
            ] = otn_field.generator.get_next_value().as_int
        return self._frame

    def __repr__(self) -> str:
        import numpy as np

        return repr(np.array(self._frame))
