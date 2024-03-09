import unittest
import random

from generator.utils import OverheadValue


class TestOverheadValue(unittest.TestCase):
    def generate_random_binary_string(self, size:int) -> str:
        return ''.join(random.choice("01") for _ in range(size))

    def test_as_binary_string(self):
        expected:str = self.generate_random_binary_string(size=0)
        ov = OverheadValue(binary_string=expected)
        self.assertEqual(ov.as_binary_string, expected)

        expected:str = self.generate_random_binary_string(size=5)
        ov = OverheadValue(binary_string=expected)
        self.assertEqual(ov.as_binary_string, expected)

        expected:str = self.generate_random_binary_string(size=9)
        ov = OverheadValue(binary_string=expected)
        self.assertEqual(ov.as_binary_string, expected)

    def test_as_int(self):
        binary_string:str = self.generate_random_binary_string(size=0)
        ov = OverheadValue(binary_string=binary_string)
        expected: int = 0 
        self.assertEqual(ov.as_int, expected)

        binary_string:str = self.generate_random_binary_string(size=8)
        ov = OverheadValue(binary_string=binary_string)
        expected: int = int(binary_string, 2) 
        self.assertEqual(ov.as_int, expected)

        binary_string:str = self.generate_random_binary_string(size=9)
        ov = OverheadValue(binary_string=binary_string)
        def expected_convert_to_int(overhead_value:OverheadValue):
            overhead_value.as_int
        self.assertRaises(ValueError, expected_convert_to_int, ov)

    def test_as_int_list(self):
        binary_string:str = self.generate_random_binary_string(size=0)
        ov = OverheadValue(binary_string=binary_string)
        expected: list[int] = []
        self.assertListEqual(ov.as_int_list, expected)

        binary_string:str = "0000000010"
        ov = OverheadValue(binary_string=binary_string)
        expected: list[int] = [0, 2]
        self.assertListEqual(ov.as_int_list, expected)

        binary_string:str = "00001"
        ov = OverheadValue(binary_string=binary_string)
        expected: list[int] = [1]
        self.assertListEqual(ov.as_int_list, expected)

        binary_string:str = "11111111"
        ov = OverheadValue(binary_string=binary_string)
        expected: list[int] = [255]
        self.assertListEqual(ov.as_int_list, expected)

    def test_equality(self):
        binary_string:str = self.generate_random_binary_string(size=0)
        ov1 = OverheadValue(binary_string=binary_string)
        ov2 = OverheadValue(binary_string=binary_string)
        self.assertEqual(ov1, ov2)

        binary_string:str = self.generate_random_binary_string(size=10)
        ov1 = OverheadValue(binary_string=binary_string)
        ov2 = OverheadValue(binary_string=binary_string)
        self.assertEqual(ov2, ov1)
