from config.frame import OtnFrameConfig
from utils.values import FrameValue
from utils.base_classes import FrameGenerator
from utils.data_classes import OtnField, OtnFrame
from utils.field_types import OtnFrameTypes, OtnPayloadTypes


class OtuFrameGenerator(FrameGenerator):
    def __init__(self, payload_type: OtnPayloadTypes, seed: int = 2):
        self.frame: OtnFrame = OtnFrameConfig.get_new_frame(frame_type=OtnFrameTypes.OTU, payload_type=payload_type, seed=seed)

    @property
    def next_value(self) -> FrameValue:
        def add_field_to_frame(field: OtnField) -> None:
            field_value: list[int] = field.generator.next_value.as_list_int
            for rn in range(field.dimension.nrows):
                for cn in range(field.dimension.ncols):
                    next_frame[field.position.row + rn][field.position.col + cn] = field_value[rn * field.dimension.nrows + cn]

        next_frame: list[list[int]] = [
            [0 for _ in range(self.frame.dimension.ncols)]
            for _ in range(self.frame.dimension.nrows)
        ]
        add_field_to_frame(field=self.frame.payload)
        for current_field in self.frame.overheads:
            add_field_to_frame(field=current_field)
        return FrameValue(next_frame)
