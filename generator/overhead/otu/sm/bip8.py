from generator.utils import OverheadValue


class SM_BIP8OverheadGenerator:
    def get_next_value(self) -> OverheadValue:
        # TODO: this should take opu frame and calculate the parity interleaved byte.
        return OverheadValue(binary_string=''.zfill(8))
