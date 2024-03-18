import unittest

from utils import OverheadValue
from generator.factory import GeneratorFactory
from config.overhead import OtuOverheads


class TestOTUOverheads(unittest.TestCase):
    def test_gcc0(self):
        g = GeneratorFactory.get_overhead_generator(otn_field=OtuOverheads.gcc0.value)
        ov: OverheadValue = g.next_value
        self.assertListEqual(ov.as_list_int, [0, 0])
        ov:OverheadValue = g.next_value
        self.assertListEqual(ov.as_list_int, [0, 0])
        self.assertEqual(ov.as_binary_string, ''.zfill(2*8))

    def test_osmc(self):
        og = GeneratorFactory.get_overhead_generator(otn_field=OtuOverheads.osmc.value)
        ov:OverheadValue = og.next_value
        self.assertEqual(ov.as_binary_string, ''.zfill(8))
        ov:OverheadValue = og.next_value
        self.assertEqual(ov.as_binary_string, ''.zfill(8))
        self.assertEqual(ov.as_int, 0)
        self.assertListEqual(ov.as_list_int, [0])

    def test_sm(self):
        og = GeneratorFactory.get_overhead_generator(otn_field=OtuOverheads.sm.value)
        ov:OverheadValue = og.next_value
        self.assertListEqual(ov.as_list_int, [0, 0, 0])
        ov:OverheadValue = og.next_value
        self.assertListEqual(ov.as_list_int, [0, 0, 0])
