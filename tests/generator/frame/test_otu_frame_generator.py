import unittest

from generator.frame import OduFrameGenerator, OpuFrameGenerator, OtuFrameGenerator


class TestOduFrameGenerator(unittest.TestCase):
    def test_null(self):
        opu = OpuFrameGenerator()
        opu.get_next_frame()

        odu = OduFrameGenerator(opu_frame_generator=opu)
        odu.get_next_frame()

        otu = OtuFrameGenerator(odu_frame_generator=odu)
        otu.get_next_frame()

    def test_prbs(self):
        opu = OpuFrameGenerator(seed=6)
        odu = OduFrameGenerator(opu_frame_generator=opu)
        odu.get_next_frame()

        otu = OtuFrameGenerator(odu_frame_generator=odu)
        otu.get_next_frame()
