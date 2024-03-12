import unittest


class TestOpuFrameGenerator(unittest.TestCase):
    def test_null(self):
        from generator.frame.opu import OpuFrameGenerator
        from generator.overhead.custom import FixedValueOverheadGenerator
        from generator.overhead.opu import NullPSIOverheadGenerator
        from generator.payload.null import NullPyaloadGenerator

        opu = OpuFrameGenerator()
        opu.overheads.psi.generator = NullPSIOverheadGenerator()
        opu.overheads.jc1.generator = FixedValueOverheadGenerator(fixed_value=1)
        opu.overheads.jc2.generator = FixedValueOverheadGenerator(fixed_value=2)
        opu.overheads.jc3.generator = FixedValueOverheadGenerator(fixed_value=3)
        opu.overheads.jc4.generator = FixedValueOverheadGenerator(fixed_value=4)
        opu.overheads.jc5.generator = FixedValueOverheadGenerator(fixed_value=5)
        opu.overheads.jc6.generator = FixedValueOverheadGenerator(fixed_value=6)
        opu.overheads.pjo.generator = FixedValueOverheadGenerator(fixed_value=9)
        opu.overheads.njo.generator = FixedValueOverheadGenerator(fixed_value=77)
        opu.payload.generator = NullPyaloadGenerator()
        opu.get_next_frame()

    def test_prbs(self):
        from generator.frame.opu import OpuFrameGenerator
        from generator.overhead.custom import FixedValueOverheadGenerator

        opu2 = OpuFrameGenerator(seed=6)
        opu2.overheads.jc1.generator = FixedValueOverheadGenerator(fixed_value=1)
        opu2.overheads.jc2.generator = FixedValueOverheadGenerator(fixed_value=2)
        opu2.overheads.jc3.generator = FixedValueOverheadGenerator(fixed_value=3)
        opu2.overheads.jc4.generator = FixedValueOverheadGenerator(fixed_value=4)
        opu2.overheads.njo.generator = FixedValueOverheadGenerator(fixed_value=77)
        opu2.get_next_frame()
