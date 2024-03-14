import unittest

from utils import OtnFieldTypes

class TestOpuFrameGenerator(unittest.TestCase):
    def test_null(self):
        from generator.frame.opu import OpuFrameGenerator

        opu = OpuFrameGenerator(OtnFieldTypes.OPU_PAYLOAD_NULL)
        l = opu.get_next_frame()
        # import numpy
        # numpy.set_printoptions(edgeitems=4, linewidth=180)
        # print(numpy.array(l))


    def test_prbs(self):
        from generator.frame.opu import OpuFrameGenerator
        opu = OpuFrameGenerator(payload_type=OtnFieldTypes.OPU_PAYLOAD_PRBS, seed=6)
        l = opu.get_next_frame()
        # import numpy
        # numpy.set_printoptions(edgeitems=4, linewidth=180)
        # print(numpy.array(l))
