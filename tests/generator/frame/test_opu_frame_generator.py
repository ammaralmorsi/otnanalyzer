import warnings
import unittest

from utils import OtnFieldTypes

class TestOpuFrameGenerator(unittest.TestCase):
    def test_null(self):
        from generator.frame.opu import OpuFrameGenerator

        opu = OpuFrameGenerator(OtnFieldTypes.OPU_PAYLOAD_NULL)
        l = opu.get_next_frame()
        l = opu.get_next_frame()
        try:
            import numpy
            numpy.set_printoptions(edgeitems=15, linewidth=180)
            print(numpy.array(l))
        except ImportError:
            warnings.warn(
                message="run tests in environment that has 'numpy' to be able to visualize the frame",
                category=ImportWarning)


    def test_prbs(self):
        from generator.frame.opu import OpuFrameGenerator
        opu = OpuFrameGenerator(payload_type=OtnFieldTypes.OPU_PAYLOAD_PRBS, seed=6)
        l = opu.get_next_frame()
        l = opu.get_next_frame()
        l = opu.get_next_frame()
        try:
            import numpy
            numpy.set_printoptions(edgeitems=15, linewidth=180)
            print(numpy.array(l))
        except ImportError:
            warnings.warn(
                message="run tests in environment that has 'numpy' to be able to visualize the frame",
                category=ImportWarning)
