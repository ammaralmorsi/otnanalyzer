from utils import OtnField, Dimension, Position
from config import OpuOverheads
from generator.payload.prbs import PRBSPayloadGenerator
from utils.base_classes import PayloadGenerator
from utils.field_types import OtnFieldTypes


class OpuFrameGenerator:
    def __init__(self, seed=2):
        self.dimension: Dimension = Dimension(nrows=4, ncols=3810)
        self.payload: OtnField = OtnField(
            name="prbs",
            field_type=OtnFieldTypes.OPU_PAYLOAD,
            position=Position(col=2, row=0),
            dimension=Dimension(nrows=4, ncols=3808),
        )
        self.payload_generator: PayloadGenerator = PRBSPayloadGenerator(seed)
        self._frame: list[list[int]] = [
            [0 for _ in range(self.dimension.ncols)]
            for _ in range(self.dimension.nrows)
        ]

    def get_next_frame(self) -> list[list[int]]:
        payload: list[int] = self.payload_generator.next_value.as_list_int
        for rn in range(self.payload.dimension.nrows):
            for cn in range(self.payload.dimension.ncols):
                self._frame[self.payload.position.row + rn][
                    self.payload.position.col + cn
                ] = payload[rn * self.dimension.nrows + cn]

        for otn_field in OpuOverheads.get_fields():
            otn_field.generator = None
        return self._frame
