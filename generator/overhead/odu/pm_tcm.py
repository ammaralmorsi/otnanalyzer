from utils import OverheadGenerator, OverheadValue
from .dm import DMOverheadGenerator


class PM_TCMOvherheadGenerator(OverheadGenerator):
    def __init__(self):
        self.dmt1_generator = DMOverheadGenerator()
        self.dmt2_generator = DMOverheadGenerator()
        self.dmt3_generator = DMOverheadGenerator()
        self.dmt4_generator = DMOverheadGenerator()
        self.dmt5_generator = DMOverheadGenerator()
        self.dmt6_generator = DMOverheadGenerator()
        self.dmp_generator = DMOverheadGenerator()

    @property
    def next_value(self) -> OverheadValue:
        binary_string = ""
        binary_string += f"{self.dmt1_generator.next_value.as_binary_string}"
        binary_string += f"{self.dmt2_generator.next_value.as_binary_string}"
        binary_string += f"{self.dmt3_generator.next_value.as_binary_string}"
        binary_string += f"{self.dmt4_generator.next_value.as_binary_string}"
        binary_string += f"{self.dmt5_generator.next_value.as_binary_string}"
        binary_string += f"{self.dmt6_generator.next_value.as_binary_string}"
        binary_string += f"{self.dmp_generator.next_value.as_binary_string}"
        binary_string += f"0"
        return OverheadValue(binary_string=binary_string)
