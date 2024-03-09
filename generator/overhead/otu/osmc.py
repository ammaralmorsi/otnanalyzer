from generator.utils import OverheadValue

class OSMCOverheadGenerator:
    def get_next_value(self) -> OverheadValue:
        return OverheadValue(binary_string=''.zfill(8)) 
