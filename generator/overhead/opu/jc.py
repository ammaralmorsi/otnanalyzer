from generator.utils import OverheadValue


class JCOverheadGenerator:
    def get_next_value(self):
        return OverheadValue(binary_string=''.zfill(8))
