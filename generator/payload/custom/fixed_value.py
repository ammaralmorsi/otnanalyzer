from utils import PayloadGenerator, PayloadValue


class FixedValuePayloadGenerator(PayloadGenerator):
    def __init__(self, fixed_value:int):
        """ a number between 0 and 255 """
        self.fixed_value:int = fixed_value

    @property
    def next_value(self) -> PayloadValue:
        return PayloadValue([self.fixed_value for _ in range(4 * 3808)])
