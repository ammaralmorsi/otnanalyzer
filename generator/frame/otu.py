from utils import Position, Dimension
from config import OtuOverheads
from utils import OtnField
from utils import GeneratorFactory

from .odu import OduFrameGenerator


class OtuFrameGenerator:
    def __init__(self, odu_frame_generator: OduFrameGenerator):
        self.dimension:Dimension = Dimension(nrows=4, ncols=3824)
        self.odu_frame:OduFrameGenerator = odu_frame_generator
        self.odu_position:Position = Position(row=0, col=0)
        self.overheads: list[OtnField] = OtuOverheads.get_fields()
        for current_field in self.overheads:
            current_field.generator = GeneratorFactory.get_overhead_generator(current_field)
        self._frame:list[list[int]] = [
            [0 for _ in range(self.dimension.ncols)]
            for _ in range(self.dimension.nrows)
        ]

    def get_next_frame(self) -> list[list[int]]:
        def add_field_to_frame(field: OtnField) -> None:
            field_value: list[int] = field.generator.next_value.as_list_int
            for rn in range(field.dimension.nrows):
                for cn in range(field.dimension.ncols):
                    self._frame[field.position.row + rn][field.position.col + cn] = field_value[rn * field.dimension.nrows + cn]

        odu_frame: list[list[int]] = self.odu_frame.get_next_frame()
        for rn in range(self.odu_frame.dimension.nrows):
            for cn in range(self.odu_frame.dimension.ncols):
                self._frame[self.odu_position.row + rn][self.odu_position.col + cn] = odu_frame[rn][cn]
        for current_field in self.overheads:
            add_field_to_frame(field=current_field)
        return self._frame
