from generator.utils import OverheadValue, FieldGenerator

class OSMCOverheadGenerator(FieldGenerator):
    def get_next_value(self) -> OverheadValue:
        return OverheadValue(binary_string=''.zfill(8)) 
