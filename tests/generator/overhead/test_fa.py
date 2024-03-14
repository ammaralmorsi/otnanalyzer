import unittest

from utils import OverheadValue
from utils import GeneratorFactory
from config import OtuOverheads


class TestFASOverheads(unittest.TestCase):
    def setUp(self):
        self.fas_generator = GeneratorFactory.get_overhead_generator(OtuOverheads.fas.value)
        self.mfas_generator = GeneratorFactory.get_overhead_generator(OtuOverheads.mfas.value)

    def test_fas(self):
        expected: list[int] = [246, 246, 246, 40, 40, 40]
        ov:OverheadValue = self.fas_generator.next_value
        self.assertListEqual(ov.as_list_int, expected)
        self.assertListEqual(ov.as_list_int, expected)

    def test_mfas(self):
        for i in range(256):
            self.assertEqual(self.mfas_generator.next_value.as_int, i)

        self.assertEqual(self.mfas_generator.next_value.as_int, 0)

        for i in range(1, 256):
            self.assertEqual(self.mfas_generator.next_value.as_int, i)

        self.assertEqual(self.mfas_generator.next_value.as_int, 0)
