import unittest


class TestOpuFrameGenerator(unittest.TestCase):
    def test_null(self):
        from generator.frame.opu import NullOpuFrameGenerator
        from generator.frame.odu import OduFrameGenerator
        OduFrameGenerator(NullOpuFrameGenerator())

    def test_prbs(self):
        from generator.frame.opu import PRBSOpuFrameGenerator
        from generator.frame.odu import OduFrameGenerator
        OduFrameGenerator(PRBSOpuFrameGenerator(seed=2))
