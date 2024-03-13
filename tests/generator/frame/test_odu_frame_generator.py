import unittest

from generator.frame.odu import OduFrameGenerator, OpuFrameGenerator
from generator.overhead.custom import FixedValueOverheadGenerator
from generator.overhead.custom.sweep import SweepOverheadGenerator


class TestOduFrameGenerator(unittest.TestCase):
    def test_null(self):
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

        odu = OduFrameGenerator(opu_frame_generator=opu)
        odu.overheads.pm_tcm.generator = FixedValueOverheadGenerator(fixed_value=23)
        odu.overheads.pm.generator = FixedValueOverheadGenerator(
            fixed_value=6, size=odu.overheads.pm.dimension.ncols
        )
        odu.overheads.tcm6.generator = SweepOverheadGenerator(
            start=5, end=9, size=odu.overheads.tcm6.dimension.ncols
        )
        odu.get_next_frame()
        # print(odu)

    def test_prbs(self):
        opu = OpuFrameGenerator(seed=6)
        odu = OduFrameGenerator(opu_frame_generator=opu)
        odu.overheads.pm_tcm.generator = FixedValueOverheadGenerator(fixed_value=23)
        odu.overheads.pm.generator = FixedValueOverheadGenerator(
            fixed_value=10, size=odu.overheads.pm.dimension.ncols
        )
        odu.overheads.gcc1.generator = SweepOverheadGenerator(
            start=6, end=19, size=odu.overheads.gcc1.dimension.ncols
        )
        odu.get_next_frame()
        # print(odu)
