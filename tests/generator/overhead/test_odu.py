import unittest

from utils import OverheadValue
from generator.factory import GeneratorFactory
from config.overhead import OduOverheads


class TestODUGenerators(unittest.TestCase):
    def test_pm_tcm(self):
        og = GeneratorFactory.get_overhead_generator(otn_field=OduOverheads.pm_tcm.value)
        ov:OverheadValue = og.next_value
        self.assertEqual(ov.as_binary_string, ''.zfill(8*OduOverheads.pm_tcm.value.dimension.size))

    def test_gcc(self):
        og = GeneratorFactory.get_overhead_generator(otn_field=OduOverheads.gcc1.value)
        ov:OverheadValue = og.next_value
        self.assertListEqual(ov.as_list_int, [0 for _ in range(OduOverheads.gcc1.value.dimension.size)])

        og = GeneratorFactory.get_overhead_generator(otn_field=OduOverheads.gcc2.value)
        ov:OverheadValue = og.next_value
        self.assertEqual(ov.as_binary_string, ''.zfill(8*OduOverheads.gcc1.value.dimension.size))

    def test_aps_pcc(self):
        og = GeneratorFactory.get_overhead_generator(otn_field=OduOverheads.aps_pcc.value)
        ov:OverheadValue = og.next_value
        self.assertEqual(ov.as_binary_string, ''.zfill(8*OduOverheads.aps_pcc.value.dimension.size))

    def test_tcm(self):
        og = GeneratorFactory.get_overhead_generator(otn_field=OduOverheads.tcm1.value)
        ov:OverheadValue = og.next_value
        self.assertEqual(ov.as_binary_string, ''.zfill(8*OduOverheads.tcm1.value.dimension.size))

        og = GeneratorFactory.get_overhead_generator(otn_field=OduOverheads.tcm3.value)
        ov:OverheadValue = og.next_value
        self.assertEqual(ov.as_binary_string, ''.zfill(8*OduOverheads.tcm3.value.dimension.size))

        og = GeneratorFactory.get_overhead_generator(otn_field=OduOverheads.tcm5.value)
        ov:OverheadValue = og.next_value
        self.assertEqual(ov.as_binary_string, ''.zfill(8*OduOverheads.tcm5.value.dimension.size))

        og = GeneratorFactory.get_overhead_generator(otn_field=OduOverheads.tcm6.value)
        ov:OverheadValue = og.next_value
        self.assertEqual(ov.as_binary_string, ''.zfill(8*OduOverheads.tcm6.value.dimension.size))

    def test_pm(self):
        og = GeneratorFactory.get_overhead_generator(otn_field=OduOverheads.pm.value)
        ov:OverheadValue = og.next_value
        self.assertEqual(ov.as_binary_string, ''.zfill(8*OduOverheads.pm.value.dimension.size))

    def test_exp(self):
        og = GeneratorFactory.get_overhead_generator(otn_field=OduOverheads.exp1.value)
        ov: OverheadValue = og.next_value
        self.assertEqual(ov.as_binary_string, ''.zfill(8*OduOverheads.exp1.value.dimension.size))

        og = GeneratorFactory.get_overhead_generator(otn_field=OduOverheads.exp3.value)
        ov: OverheadValue = og.next_value
        self.assertEqual(ov.as_binary_string, ''.zfill(8*OduOverheads.exp3.value.dimension.size))

    def test_res(self):
        og = GeneratorFactory.get_overhead_generator(otn_field=OduOverheads.res1.value)
        ov: OverheadValue = og.next_value
        self.assertEqual(ov.as_binary_string, ''.zfill(8*OduOverheads.res1.value.dimension.size))

        og = GeneratorFactory.get_overhead_generator(otn_field=OduOverheads.res2.value)
        ov: OverheadValue = og.next_value
        self.assertEqual(ov.as_binary_string, ''.zfill(8*OduOverheads.res2.value.dimension.size))
