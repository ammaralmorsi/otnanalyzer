import unittest

from utils import OverheadValue


class TestOTUOverheads(unittest.TestCase):
    def test_gcc0(self):
        from generator.overhead.otu import GCC0OverheadGenerator
        og = GCC0OverheadGenerator()
        ov:OverheadValue = og.next_value
        self.assertListEqual(ov.as_list_int, [0, 0])
        ov:OverheadValue = og.next_value
        self.assertListEqual(ov.as_list_int, [0, 0])

        self.assertEqual(ov.as_binary_string, ''.zfill(2*8))

    def test_osmc(self):
        from generator.overhead.otu import OSMCOverheadGenerator
        og = OSMCOverheadGenerator()
        ov:OverheadValue = og.next_value
        self.assertEqual(ov.as_binary_string, ''.zfill(8))
        ov:OverheadValue = og.next_value
        self.assertEqual(ov.as_binary_string, ''.zfill(8))

        self.assertEqual(ov.as_int, 0)
        self.assertListEqual(ov.as_list_int, [0])

    def test_sm_tti(self):
        from generator.overhead.otu import SM_TTIOverheadGenerator
        og = SM_TTIOverheadGenerator()
        ov:OverheadValue = og.next_value
        self.assertEqual(ov.as_binary_string, ''.zfill(8))

    def test_sm_bip8(self):
        from generator.overhead.otu import SM_BIP8OverheadGenerator
        og = SM_BIP8OverheadGenerator()
        ov:OverheadValue = og.next_value
        # NOTE: this should break when implemnting the algorithm.
        self.assertEqual(ov.as_binary_string, ''.zfill(8))

    def test_sm_bei_biae(self):
        from generator.overhead.otu import SM_BEI_BIAEOverheadGenerator
        og = SM_BEI_BIAEOverheadGenerator()
        ov:OverheadValue = og.next_value
        self.assertEqual(ov.as_binary_string, ''.zfill(4))

    def test_sm_bdi(self):
        from generator.overhead.otu import SM_BDIOverheadGenerator
        og = SM_BDIOverheadGenerator()
        ov:OverheadValue = og.next_value
        self.assertEqual(ov.as_binary_string, ''.zfill(1))

    def test_sm_iae(self):
        from generator.overhead.otu import SM_IAEOverheadGenerator
        og = SM_IAEOverheadGenerator()
        ov:OverheadValue = og.next_value
        self.assertEqual(ov.as_binary_string, ''.zfill(1))
