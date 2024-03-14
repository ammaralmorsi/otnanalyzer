import unittest

from generator.payload import FixedValuePayloadGenerator
from generator.payload import NullPyaloadGenerator
from generator.payload import PRBSPayloadGenerator


class TestPayload(unittest.TestCase):
    def test_custom(self):
        fg = FixedValuePayloadGenerator(fixed_value=5)
        fg.next_value.as_list_int

    def test_null(self):
        ng = NullPyaloadGenerator()
        ng.next_value.as_list_int

    def test_prbs(self):
        pg = PRBSPayloadGenerator(seed=2)
        pg.next_value.as_list_int
