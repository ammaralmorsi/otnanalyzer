import warnings
import unittest

from generator.frame.odu import OduFrameGenerator
from utils import OtnPayloadTypes


class TestOduFrameGenerator(unittest.TestCase):
    def test_null(self):
        odu = OduFrameGenerator(payload_type=OtnPayloadTypes.NULL)
        l = odu.next_value
        l = odu.next_value
        l = odu.next_value
        try:
            import numpy
            numpy.set_printoptions(edgeitems=15, linewidth=180)
            print(numpy.array(l))
        except ImportError:
            warnings.warn(
                message="run tests in environment that has 'numpy' to be able to visualize the frame",
                category=ImportWarning)


    def test_prbs(self):
        odu = OduFrameGenerator(payload_type=OtnPayloadTypes.PRBS)
        l = odu.next_value
        l = odu.next_value
        l = odu.next_value
        try:
            import numpy
            numpy.set_printoptions(edgeitems=15, linewidth=180)
            print(numpy.array(l))
        except ImportError:
            warnings.warn(
                message="run tests in environment that has 'numpy' to be able to visualize the frame",
                category=ImportWarning)
