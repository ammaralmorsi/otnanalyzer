from utils import OverheadGenerator, OverheadValue


class TCM_BIP8OverheadGenerator(OverheadGenerator):
    @property
    def next_value(self) -> OverheadValue:
        # TODO: this should take opu frame and calculate the parity interleaved byte.
        return OverheadValue(binary_string=''.zfill(8))
