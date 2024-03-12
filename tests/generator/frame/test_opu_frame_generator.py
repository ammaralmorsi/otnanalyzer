import unittest


class TestOpuFrameGenerator(unittest.TestCase):
    def test_null(self):
        from generator.frame.opu import NullOpuFrameGenerator
        NullOpuFrameGenerator()

    def test_prbs(self):
        from generator.frame.opu import PRBSOpuFrameGenerator
        PRBSOpuFrameGenerator(seed=2)
