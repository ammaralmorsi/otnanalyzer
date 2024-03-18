import warnings
import unittest

from utils import OtnPayloadTypes

class TestOpuFrameGenerator(unittest.TestCase):
    def test_null(self):
        from generator.frame.opu import OpuFrameGenerator

        opu = OpuFrameGenerator(OtnPayloadTypes.NULL)
        l = opu.next_value
        l = opu.next_value
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
        opu = OpuFrameGenerator(payload_type=OtnPayloadTypes.PRBS, seed=6)
        l = opu.next_value
        l = opu.next_value
        l = opu.next_value
        try:
            import numpy
            numpy.set_printoptions(edgeitems=15, linewidth=180)
            print(numpy.array(l))
        except ImportError:
            warnings.warn(
                message="run tests in environment that has 'numpy' to be able to visualize the frame",
                category=ImportWarning)
