from utils import OverheadGenerator, OverheadValue
from .tti import TCM_TTIOverheadGenerator
from .bip8 import TCM_BIP8OverheadGenerator
from .bei_biae import TCM_BEI_BIAEOverheadGenerator
from .bdi import TCM_BDIOverheadGenerator
from .stat import TCM_STATOverheadGenerator


class TCMOverheadGenerator(OverheadGenerator):
    def __init__(self):
        self.tti_generator = TCM_TTIOverheadGenerator()
        self.bip8_generator = TCM_BIP8OverheadGenerator()
        self.bei_biae_generator = TCM_BEI_BIAEOverheadGenerator()
        self.bdi_generator = TCM_BDIOverheadGenerator()
        self.stat_generator = TCM_STATOverheadGenerator()

    @property
    def next_value(self) -> OverheadValue:
        binary_string = ""
        binary_string += f"{self.tti_generator.next_value.as_binary_string}"
        binary_string += f"{self.bip8_generator.next_value.as_binary_string}"
        binary_string += f"{self.bei_biae_generator.next_value.as_binary_string}"
        binary_string += f"{self.bdi_generator.next_value.as_binary_string}"
        binary_string += f"{self.stat_generator.next_value.as_binary_string}"
        return OverheadValue(binary_string=binary_string)
