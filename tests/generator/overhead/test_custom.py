import unittest

from generator.utils import OverheadValue


class TestCustomOverheadGenerator(unittest.TestCase):
    def test_fixed_value(self):
        from generator.overhead.custom import FixedValueOverheadGenerator

        expected:int = 212
        og = FixedValueOverheadGenerator(fixed_value=expected)
        ov:OverheadValue = og.get_next_value()
        self.assertEqual(ov.as_int, expected)

        expected:int = 2123
        og = FixedValueOverheadGenerator(fixed_value=expected)
        ov:OverheadValue = og.get_next_value()
        def should_raise_value_error():
            ov.as_int
        self.assertRaises(ValueError, should_raise_value_error)

    def test_sweep(self):
        from generator.overhead.custom import SweepOverheadGenerator

        og = SweepOverheadGenerator(start=0, end=10)
        for i in range(10):
            ov:OverheadValue = og.get_next_value()
            self.assertEqual(ov.as_int, i)
        ov:OverheadValue = og.get_next_value()
        self.assertEqual(ov.as_int, 10)  # assuming inclusion

        ov:OverheadValue = og.get_next_value()
        self.assertEqual(ov.as_int, 0)

        og = SweepOverheadGenerator(start=10, end=10)
        for _ in range(10):
            ov:OverheadValue = og.get_next_value()
            self.assertEqual(ov.as_int, 10)

        self.assertRaises(ValueError, SweepOverheadGenerator, 10, 9)
