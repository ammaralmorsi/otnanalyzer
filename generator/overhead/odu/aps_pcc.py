from generator.utils import OverheadValue


class APS_PCCOverheadGenerator:
    def get_next_value(self):
        return OverheadValue(binary_string=''.zfill(4*8))
