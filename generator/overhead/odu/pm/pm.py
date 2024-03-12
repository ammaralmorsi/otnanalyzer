from generator.utils import OverheadValue, FieldGenerator
from .tti import PM_TTIOverheadGenerator
from .bdi import PM_BDIOverheadGenerator
from .bei import PM_BEIOverheadGenerator
from .bip8 import PM_BIP8OverheadGenerator
from .stat import PM_STATOverheadGenerator


class PMOverheadGenerator(FieldGenerator):
    def __init__(self):
        self.tti_generator = PM_TTIOverheadGenerator()
        self.bip8_generator = PM_BIP8OverheadGenerator()
        self.bei_generator = PM_BEIOverheadGenerator()
        self.bdi_generator = PM_BDIOverheadGenerator()
        self.stat_generator = PM_STATOverheadGenerator()

    def get_next_value(self) -> OverheadValue:
        binary_string = ""
        binary_string += f"{self.tti_generator.get_next_value().as_binary_string}"
        binary_string += f"{self.bip8_generator.get_next_value().as_binary_string}"
        binary_string += f"{self.bei_generator.get_next_value().as_binary_string}"
        binary_string += f"{self.bdi_generator.get_next_value().as_binary_string}"
        binary_string += f"{self.stat_generator.get_next_value().as_binary_string}"
        return OverheadValue(binary_string=binary_string)
