from generator.utils import PayloadValue, FieldGenerator
from .custom.fixed_value import FixedValuePayloadGenerator


class NullPyaloadGenerator(FieldGenerator):
    def __init__(self):
        self.fixed_value_payload_generator = FixedValuePayloadGenerator(fixed_value=0) 

    def get_next_payload(self) -> list[int]:
        return self.fixed_value_payload_generator.get_next_payload()

    def get_next_value(self) -> PayloadValue:
        return PayloadValue(data=self.get_next_payload())
