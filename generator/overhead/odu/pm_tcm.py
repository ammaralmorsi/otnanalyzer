from generator.utils import OverheadValue, FieldGenerator
from .dm import DMOverheadGenerator


class PM_TCMOvherheadGenerator(FieldGenerator):
    def __init__(self):
        self.dmt1_generator = DMOverheadGenerator()
        self.dmt2_generator = DMOverheadGenerator()
        self.dmt3_generator = DMOverheadGenerator()
        self.dmt4_generator = DMOverheadGenerator()
        self.dmt5_generator = DMOverheadGenerator()
        self.dmt6_generator = DMOverheadGenerator()
        self.dmp_generator = DMOverheadGenerator()

    def get_next_value(self) -> OverheadValue:
        binary_string = ""
        binary_string += f"{self.dmt1_generator.get_next_value().as_binary_string}"
        binary_string += f"{self.dmt2_generator.get_next_value().as_binary_string}"
        binary_string += f"{self.dmt3_generator.get_next_value().as_binary_string}"
        binary_string += f"{self.dmt4_generator.get_next_value().as_binary_string}"
        binary_string += f"{self.dmt5_generator.get_next_value().as_binary_string}"
        binary_string += f"{self.dmt6_generator.get_next_value().as_binary_string}"
        binary_string += f"{self.dmp_generator.get_next_value().as_binary_string}"
        binary_string += f"0"  # to make a complete byte
        return OverheadValue(binary_string=binary_string)
