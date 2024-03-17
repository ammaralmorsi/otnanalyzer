import warnings
import unittest

from generator.frame import OduFrameGenerator, OpuFrameGenerator
from utils import OtnFieldTypes


class TestOduFrameGenerator(unittest.TestCase):
    def test_null(self):
        opu = OpuFrameGenerator(OtnFieldTypes.OPU_PAYLOAD_NULL)
        odu = OduFrameGenerator(opu_frame_generator=opu)
        l = odu.get_next_frame()
        l = odu.get_next_frame()
        l = odu.get_next_frame()
        try:
            import numpy
            numpy.set_printoptions(edgeitems=15, linewidth=180)
            print(numpy.array(l))
        except ImportError:
            warnings.warn(
                message="run tests in environment that has 'numpy' to be able to visualize the frame",
                category=ImportWarning)


    def test_prbs(self):
        opu = OpuFrameGenerator(OtnFieldTypes.OPU_PAYLOAD_PRBS, seed=6)
        odu = OduFrameGenerator(opu_frame_generator=opu)
        l = odu.get_next_frame()
        l = odu.get_next_frame()
        l = odu.get_next_frame()
        try:
            import numpy
            numpy.set_printoptions(edgeitems=15, linewidth=180)
            print(numpy.array(l))
        except ImportError:
            warnings.warn(
                message="run tests in environment that has 'numpy' to be able to visualize the frame",
                category=ImportWarning)
