import unittest


class TestOpuFrameGenerator(unittest.TestCase):
    def test_null(self):
        from generator.frame.opu import OpuFrameGenerator

        opu = OpuFrameGenerator()
        opu.get_next_frame()

    def test_prbs(self):
        from generator.frame.opu import OpuFrameGenerator

        opu2 = OpuFrameGenerator(seed=6)
        opu2.get_next_frame()
