import warnings
import unittest

from generator.frame.otu import OtuFrameGenerator
from utils.field_types import OtnPayloadTypes


class TestOduFrameGenerator(unittest.TestCase):
    def test_null(self):
        otu = OtuFrameGenerator(payload_type=OtnPayloadTypes.NULL)
        l = otu.next_value
        l = otu.next_value
        l = otu.next_value
        l = otu.next_value
        l = otu.next_value
        try:
            import numpy
            numpy.set_printoptions(edgeitems=15, linewidth=180)
            print(numpy.array(l))
        except ImportError:
            warnings.warn(
                message="run tests in environment that has 'numpy' to be able to visualize the frame",
                category=ImportWarning)

    def test_prbs(self):
        otu = OtuFrameGenerator(payload_type=OtnPayloadTypes.PRBS)
        l = otu.next_value
        l = otu.next_value
        l = otu.next_value
        try:
            import numpy
            numpy.set_printoptions(edgeitems=15, linewidth=180)
            print(numpy.array(l))
        except ImportError:
            warnings.warn(
                message="run tests in environment that has 'numpy' to be able to visualize the frame",
                category=ImportWarning)
