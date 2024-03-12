from generator.utils import OverheadValue, FieldGenerator


class APS_PCCOverheadGenerator(FieldGenerator):
    def get_next_value(self) -> OverheadValue:
        return OverheadValue(binary_string=''.zfill(4*8))
