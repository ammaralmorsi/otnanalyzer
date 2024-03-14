from utils import OtnField, Dimension, Position
from config import OpuOverheads
from utils import OtnFieldTypes
from utils import GeneratorFactory


class OpuFrameGenerator:
    def __init__(self, payload_type: OtnFieldTypes, seed: int=2):
        self.dimension: Dimension = Dimension(nrows=4, ncols=3810)
        self.payload: OtnField = OtnField(
            name=payload_type.name,
            field_type=payload_type,
            position=Position(col=2, row=0),
            dimension=Dimension(nrows=4, ncols=3808),
        )
        self.payload.generator = GeneratorFactory.get_payload_generator(self.payload, seed)
        self.overheads: list[OtnField] = OpuOverheads.get_fields()
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

        add_field_to_frame(field=self.payload)
        for current_field in self.overheads:
            current_field.generator = GeneratorFactory.get_overhead_generator(current_field)
            add_field_to_frame(field=current_field)
        return self._frame
