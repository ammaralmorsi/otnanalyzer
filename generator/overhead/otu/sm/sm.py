from generator.utils import OverheadValue, FieldGenerator
from .tti import SM_TTIOverheadGenerator
from .bip8 import SM_BIP8OverheadGenerator
from .bei_biae import SM_BEI_BIAEOverheadGenerator
from .bdi import SM_BDIOverheadGenerator


class SMOverheadGenerator(FieldGenerator):
    def __init__(self):
        self.tti_generator = SM_TTIOverheadGenerator()
        self.bip8_generator = SM_BIP8OverheadGenerator()
        self.bei_biae_generator = SM_BEI_BIAEOverheadGenerator()
        self.bdi_generator = SM_BDIOverheadGenerator()

    def get_next_value(self) -> OverheadValue:
        binary_string = ""
        binary_string += f"{self.tti_generator.get_next_value().as_binary_string}"
        binary_string += f"{self.bip8_generator.get_next_value().as_binary_string}"
        binary_string += f"{self.bei_biae_generator.get_next_value().as_binary_string}"
        binary_string += f"{self.bdi_generator.get_next_value().as_binary_string}"
        binary_string += f"00"
        return OverheadValue(binary_string=binary_string)
