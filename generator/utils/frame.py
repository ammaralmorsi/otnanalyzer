from dataclasses import dataclass

from generator.utils import OtnField, Dimension, Position
from generator.overhead.opu import (JCOverheadGenerator, NJOOverheadGenerator, 
    PJOOverheadGenerator, NullPSIOverheadGenerator, PRBSPSIOverheadGenerator)
from generator.overhead.odu import (ResOverheadGenerator, PM_TCMOvherheadGenerator, ExpOverheadGenerator,
    TCMOverheadGenerator, PMOverheadGenerator, GCC1OverheadGenerator, GCC2OverheadGenerator, APS_PCCOverheadGenerator)


@dataclass
class OpuOverheads:
    jc1:OtnField = OtnField(name="jc1", position=Position(col=1, row=0), dimension=Dimension(nrows=1, ncols=1), generator=JCOverheadGenerator())
    jc2:OtnField = OtnField(name="jc2", position=Position(col=1, row=1), dimension=Dimension(nrows=1, ncols=1), generator=JCOverheadGenerator())
    jc3:OtnField = OtnField(name="jc3", position=Position(col=1, row=2), dimension=Dimension(nrows=1, ncols=1), generator=JCOverheadGenerator())
    jc4:OtnField = OtnField(name="jc4", position=Position(col=0, row=0), dimension=Dimension(nrows=1, ncols=1), generator=JCOverheadGenerator())
    jc5:OtnField = OtnField(name="jc5", position=Position(col=0, row=1), dimension=Dimension(nrows=1, ncols=1), generator=JCOverheadGenerator())
    jc6:OtnField = OtnField(name="jc6", position=Position(col=0, row=2), dimension=Dimension(nrows=1, ncols=1), generator=JCOverheadGenerator())
    njo:OtnField = OtnField(name="njo", position=Position(col=1, row=3), dimension=Dimension(nrows=1, ncols=1), generator=NJOOverheadGenerator())
    pjo:OtnField = OtnField(name="pjo", position=Position(col=2, row=3), dimension=Dimension(nrows=1, ncols=1), generator=PJOOverheadGenerator())


@dataclass
class NullOpuOverheads(OpuOverheads):
    psi:OtnField = OtnField(name="psi", position=Position(col=0, row=3), dimension=Dimension(nrows=1, ncols=1), generator=NullPSIOverheadGenerator())


@dataclass
class PRBSOpuOverheads(OpuOverheads):
    psi:OtnField = OtnField(name="psi", position=Position(col=0, row=3), dimension=Dimension(nrows=1, ncols=1), generator=PRBSPSIOverheadGenerator())


@dataclass
class OduOverheads:
    res1:OtnField = OtnField(name="res1", position=Position(col=0, row=1), dimension=Dimension(nrows=1, ncols=2), generator=ResOverheadGenerator(size=2))
    pm_tcm:OtnField = OtnField(name="pm_tcm", position=Position(col=2, row=1), dimension=Dimension(nrows=1, ncols=1), generator=PM_TCMOvherheadGenerator())
    exp1:OtnField = OtnField(name="exp1", position=Position(col=3, row=1), dimension=Dimension(nrows=1, ncols=1), generator=ExpOverheadGenerator(size=1))
    tcm6:OtnField = OtnField(name="tcm6", position=Position(col=4, row=1), dimension=Dimension(nrows=1, ncols=3), generator=TCMOverheadGenerator())
    tcm5:OtnField = OtnField(name="tcm5", position=Position(col=7, row=1), dimension=Dimension(nrows=1, ncols=3), generator=TCMOverheadGenerator())
    tcm4:OtnField = OtnField(name="tcm4", position=Position(col=10, row=1), dimension=Dimension(nrows=1, ncols=3), generator=TCMOverheadGenerator())
    exp2:OtnField = OtnField(name="exp2", position=Position(col=13, row=1), dimension=Dimension(nrows=1, ncols=1), generator=ExpOverheadGenerator(size=1))
    tcm3:OtnField = OtnField(name="tcm3", position=Position(col=0, row=2), dimension=Dimension(nrows=1, ncols=3), generator=TCMOverheadGenerator())
    tcm2:OtnField = OtnField(name="tcm2", position=Position(col=3, row=2), dimension=Dimension(nrows=1, ncols=3), generator=TCMOverheadGenerator())
    tcm1:OtnField = OtnField(name="tcm1", position=Position(col=6, row=2), dimension=Dimension(nrows=1, ncols=3), generator=TCMOverheadGenerator())
    pm:OtnField = OtnField(name="pm", position=Position(col=9, row=2), dimension=Dimension(nrows=1, ncols=3), generator=PMOverheadGenerator())
    exp3:OtnField = OtnField(name="exp3", position=Position(col=12, row=2), dimension=Dimension(nrows=1, ncols=2), generator=ExpOverheadGenerator(size=2))
    gcc1:OtnField = OtnField(name="gcc1", position=Position(col=0, row=3), dimension=Dimension(nrows=1, ncols=2), generator=GCC1OverheadGenerator())
    gcc2:OtnField = OtnField(name="gcc2", position=Position(col=2, row=3), dimension=Dimension(nrows=1, ncols=2), generator=GCC2OverheadGenerator())
    aps_pcc:OtnField = OtnField(name="aps_pcc", position=Position(col=4, row=3), dimension=Dimension(nrows=1, ncols=4), generator=APS_PCCOverheadGenerator())
    res2:OtnField = OtnField(name="res2", position=Position(col=8, row=3), dimension=Dimension(nrows=1, ncols=6), generator=ResOverheadGenerator(size=6))
