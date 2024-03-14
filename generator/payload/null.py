from utils import PayloadGenerator, PayloadValue
from .custom import FixedValuePayloadGenerator


class NullPyaloadGenerator(PayloadGenerator):
    def __init__(self):
        self.fixed_value_payload_generator = FixedValuePayloadGenerator(fixed_value=0) 

    @property
    def next_value(self) -> PayloadValue:
        return self.fixed_value_payload_generator.next_value
