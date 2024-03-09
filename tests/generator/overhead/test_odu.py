import unittest

from generator.utils import OverheadValue


class TestODUGenerators(unittest.TestCase):
    def test_dm(self):
        from generator.overhead.odu import DMOverheadGenerator
        og = DMOverheadGenerator()
        ov:OverheadValue = og.get_next_value()
        self.assertEqual(ov.as_binary_string, ''.zfill(1))

    def test_gcc(self):
        from generator.overhead.odu import GCC1OverheadGenerator
        og = GCC1OverheadGenerator()
        ov:OverheadValue = og.get_next_value()
        self.assertListEqual(ov.as_int_list, [0, 0])

        from generator.overhead.odu import GCC2OverheadGenerator
        og = GCC2OverheadGenerator()
        ov:OverheadValue = og.get_next_value()
        self.assertEqual(ov.as_binary_string, ''.zfill(2*8))

    def test_aps_pcc(self):
        from generator.overhead.odu import APS_PCCOverheadGenerator
        og = APS_PCCOverheadGenerator()
        ov:OverheadValue = og.get_next_value()
        self.assertEqual(ov.as_binary_string, ''.zfill(4*8))

    def test_tcm_tti(self):
        from generator.overhead.odu import TCM_TTIOverheadGenerator
        og = TCM_TTIOverheadGenerator()
        ov:OverheadValue = og.get_next_value()
        self.assertEqual(ov.as_binary_string, ''.zfill(8))

    def test_tcm_bip8(self):
        from generator.overhead.odu import TCM_BIP8OverheadGenerator
        og = TCM_BIP8OverheadGenerator()
        ov:OverheadValue = og.get_next_value()
        # NOTE: this should break when implemnting the algorithm.
        self.assertEqual(ov.as_binary_string, ''.zfill(8))

    def test_tcm_bei_biae(self):
        from generator.overhead.odu import TCM_BEI_BIAEOverheadGenerator
        og = TCM_BEI_BIAEOverheadGenerator()
        ov:OverheadValue = og.get_next_value()
        self.assertEqual(ov.as_binary_string, ''.zfill(4))

    def test_tcm_bdi(self):
        from generator.overhead.odu import TCM_BDIOverheadGenerator
        og = TCM_BDIOverheadGenerator()
        ov:OverheadValue = og.get_next_value()
        self.assertEqual(ov.as_binary_string, ''.zfill(1))

    def test_tcm_stat(self):
        from generator.overhead.odu import TCM_STATOverheadGenerator
        og = TCM_STATOverheadGenerator()
        ov:OverheadValue = og.get_next_value()
        self.assertEqual(ov.as_binary_string, ''.zfill(3))

    def test_pm_tti(self):
        from generator.overhead.odu import PM_TTIOverheadGenerator
        og = PM_TTIOverheadGenerator()
        ov:OverheadValue = og.get_next_value()
        self.assertEqual(ov.as_binary_string, ''.zfill(8))

    def test_pm_bip8(self):
        from generator.overhead.odu import PM_BIP8OverheadGenerator
        og = PM_BIP8OverheadGenerator()
        ov:OverheadValue = og.get_next_value()
        # NOTE: this should break when implemnting the algorithm.
        self.assertEqual(ov.as_binary_string, ''.zfill(8))

    def test_pm_bei(self):
        from generator.overhead.odu import PM_BEIOverheadGenerator
        og = PM_BEIOverheadGenerator()
        ov:OverheadValue = og.get_next_value()
        self.assertEqual(ov.as_binary_string, ''.zfill(4))

    def test_pm_bdi(self):
        from generator.overhead.odu import PM_BDIOverheadGenerator
        og = PM_BDIOverheadGenerator()
        ov:OverheadValue = og.get_next_value()
        self.assertEqual(ov.as_binary_string, ''.zfill(1))

    def test_pm_stat(self):
        from generator.overhead.odu import PM_STATOverheadGenerator
        og = PM_STATOverheadGenerator()
        ov:OverheadValue = og.get_next_value()
        self.assertEqual(ov.as_binary_string, ''.zfill(3))
