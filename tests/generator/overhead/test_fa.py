import unittest

from generator.utils import OverheadValue


class TestFASOverheads(unittest.TestCase):
    def setUp(self): 
        from generator.overhead.fa import FASOverheadGenerator
        from generator.overhead.fa import MFASOverheadGenerator

        self.fas_generator = FASOverheadGenerator()
        self.mfas_generator = MFASOverheadGenerator()

    def test_fas(self):
        expected: list[int] = [246, 246, 246, 40, 40, 40]
        ov:OverheadValue = self.fas_generator.get_next_value()
        self.assertListEqual(ov.as_int_list, expected)
        self.assertListEqual(ov.as_int_list, expected)

    def test_mfas(self):
        for i in range(256):
            self.assertEqual(self.mfas_generator.get_next_value().as_int, i)

        self.assertEqual(self.mfas_generator.get_next_value().as_int, 0)

        for i in range(1, 256):
            self.assertEqual(self.mfas_generator.get_next_value().as_int, i)

        self.assertEqual(self.mfas_generator.get_next_value().as_int, 0)
