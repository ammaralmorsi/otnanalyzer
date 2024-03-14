import unittest

from utils import OverheadValue
from config import OpuOverheads
from utils import GeneratorFactory
from utils import OverheadGenerator
from utils import OtnFieldTypes


class TestOPUOverheads(unittest.TestCase):
    def test_jc(self):
        g: OverheadGenerator = GeneratorFactory.get_overhead_generator(otn_field=OpuOverheads.jc1.value)
        ov: OverheadValue = g.next_value
        self.assertEqual(ov.as_int, 0)
        g: OverheadGenerator = GeneratorFactory.get_overhead_generator(otn_field=OpuOverheads.jc2.value)
        ov: OverheadValue = g.next_value
        self.assertEqual(ov.as_int, 0)
        g: OverheadGenerator = GeneratorFactory.get_overhead_generator(otn_field=OpuOverheads.jc3.value)
        ov: OverheadValue = g.next_value
        self.assertEqual(ov.as_int, 0)
        g: OverheadGenerator = GeneratorFactory.get_overhead_generator(otn_field=OpuOverheads.jc4.value)
        ov: OverheadValue = g.next_value
        self.assertEqual(ov.as_int, 0)
        g: OverheadGenerator = GeneratorFactory.get_overhead_generator(otn_field=OpuOverheads.jc4.value)
        ov: OverheadValue = g.next_value
        self.assertEqual(ov.as_int, 0)
        g: OverheadGenerator = GeneratorFactory.get_overhead_generator(otn_field=OpuOverheads.jc5.value)
        ov: OverheadValue = g.next_value
        self.assertEqual(ov.as_int, 0)
        g: OverheadGenerator = GeneratorFactory.get_overhead_generator(otn_field=OpuOverheads.jc6.value)
        ov: OverheadValue = g.next_value
        self.assertEqual(ov.as_int, 0)

    def test_psi(self):
        GeneratorFactory.set_payload_type(field_type=OtnFieldTypes.OPU_PAYLOAD_NULL)
        g: OverheadGenerator = GeneratorFactory.get_overhead_generator(otn_field=OpuOverheads.psi.value)
        ov: OverheadValue = g.next_value
        self.assertEqual(int(ov.as_binary_string, 2), int("FD", 16))
        ov:OverheadValue = g.next_value
        self.assertEqual(ov.as_int, int("FD", 16))

        GeneratorFactory.set_payload_type(field_type=OtnFieldTypes.OPU_PAYLOAD_PRBS)
        g: OverheadGenerator = GeneratorFactory.get_overhead_generator(otn_field=OpuOverheads.psi.value)
        ov: OverheadValue = g.next_value
        ov:OverheadValue = g.next_value
        self.assertEqual(ov.as_int, int("FE", 16))
        ov:OverheadValue = g.next_value
        self.assertEqual(int(ov.as_binary_string, 2), int("FE", 16))
