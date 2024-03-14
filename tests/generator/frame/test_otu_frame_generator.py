import unittest

from generator.frame import OduFrameGenerator, OpuFrameGenerator, OtuFrameGenerator
from utils import OtnFieldTypes


class TestOduFrameGenerator(unittest.TestCase):
    def test_null(self):
        opu = OpuFrameGenerator(OtnFieldTypes.OPU_PAYLOAD_NULL)
        opu.get_next_frame()

        odu = OduFrameGenerator(opu_frame_generator=opu)
        odu.get_next_frame()

        otu = OtuFrameGenerator(odu_frame_generator=odu)
        otu.get_next_frame()

    def test_prbs(self):
        opu = OpuFrameGenerator(OtnFieldTypes.OPU_PAYLOAD_PRBS)
        odu = OduFrameGenerator(opu_frame_generator=opu)
        odu.get_next_frame()

        otu = OtuFrameGenerator(odu_frame_generator=odu)
        otu.get_next_frame()
