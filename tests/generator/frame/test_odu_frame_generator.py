import unittest

from generator.frame.odu import OduFrameGenerator, OpuFrameGenerator


class TestOduFrameGenerator(unittest.TestCase):
    def test_null(self):
        opu = OpuFrameGenerator()
        opu.get_next_frame()

        odu = OduFrameGenerator(opu_frame_generator=opu)
        odu.get_next_frame()

    def test_prbs(self):
        opu = OpuFrameGenerator(seed=6)
        odu = OduFrameGenerator(opu_frame_generator=opu)
        odu.get_next_frame()
