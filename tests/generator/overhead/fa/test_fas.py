import unittest
from generator.overhead.fa.fas import FASOverheadGenerator


class TestFASOverheadGenerator(unittest.TestCase):
    def test_basic_usage(self):
        expected: list[int] = [246, 246, 246, 40, 40, 40]

        fas_generator = FASOverheadGenerator()
        self.assertListEqual(fas_generator.get_next_value(), expected)
        self.assertListEqual(fas_generator.get_next_value(), expected)
        self.assertListEqual(fas_generator.get_next_value(), expected)
