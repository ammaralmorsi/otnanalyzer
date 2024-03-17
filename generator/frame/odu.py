from utils import Position, Dimension
from config import OduOverheads
from utils import GeneratorFactory
from utils import OtnField

from .opu import OpuFrameGenerator

class OduFrameGenerator:
    def __init__(self, opu_frame_generator: OpuFrameGenerator):
        self.dimension: Dimension = Dimension(nrows=4, ncols=3824)
        self.opu_position: Position = Position(row=0, col=14)
        self.opu_frame: OpuFrameGenerator = opu_frame_generator
        self.overheads: list[OtnField] = OduOverheads.get_fields()
        for current_field in self.overheads:
            current_field.generator = GeneratorFactory.get_overhead_generator(current_field)
        self._frame: list[list[int]] = [
            [0 for _ in range(self.dimension.ncols)]
            for _ in range(self.dimension.nrows)
        ]

    def get_next_frame(self) -> list[list[int]]:
        def add_field_to_frame(field: OtnField) -> None:
            field_value: list[int] = field.generator.next_value.as_list_int
            for rn in range(field.dimension.nrows):
                for cn in range(field.dimension.ncols):
                    self._frame[field.position.row + rn][field.position.col + cn] = field_value[rn * field.dimension.nrows + cn]

        opu_frame: list[list[int]] = self.opu_frame.get_next_frame()
        for rn in range(self.opu_frame.dimension.nrows):
            for cn in range(self.opu_frame.dimension.ncols):
                self._frame[self.opu_position.row + rn][self.opu_position.col + cn] = opu_frame[rn][cn]
        for current_field in self.overheads:
            add_field_to_frame(field=current_field)
        return self._frame
