from generator.utils import PayloadValue, FieldGenerator


class FixedValuePayloadGenerator(FieldGenerator):
    def __init__(self, fixed_value:int):
        """ a number between 0 and 255 """
        self.fixed_value:int = fixed_value

    def get_next_payload(self) -> list[int]:
        return [self.fixed_value for _ in range(4 * 3808)]

    def get_next_value(self) -> PayloadValue:
        return PayloadValue(data=self.get_next_payload())
