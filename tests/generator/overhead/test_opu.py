import unittest

from generator.utils import OverheadValue


class TestOPUOverheads(unittest.TestCase):
    def test_jc(self):
        from generator.overhead.opu import JCOverheadGenerator
        og = JCOverheadGenerator()
        ov:OverheadValue = og.get_next_value()
        self.assertEqual(ov.as_int, 0)

    def test_null_psi(self):
        from generator.overhead.opu import NullPSIOverheadGenerator
        og = NullPSIOverheadGenerator()
        ov:OverheadValue = og.get_next_value()
        self.assertEqual(int(ov.as_binary_string, 2), int("FD", 16))
        ov:OverheadValue = og.get_next_value()
        self.assertEqual(ov.as_int, int("FD", 16))

    def test_prbs_psi(self):
        from generator.overhead.opu import PRBSPSIOverheadGenerator
        og = PRBSPSIOverheadGenerator()
        ov:OverheadValue = og.get_next_value()
        self.assertEqual(ov.as_int, int("FE", 16))
        ov:OverheadValue = og.get_next_value()
        self.assertEqual(int(ov.as_binary_string, 2), int("FE", 16))
