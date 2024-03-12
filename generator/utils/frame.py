from dataclasses import dataclass

from generator.utils import OtnField, Dimension, Position
from generator.overhead.opu import (JCOverheadGenerator, NJOOverheadGenerator, 
    PJOOverheadGenerator, NullPSIOverheadGenerator, PRBSPSIOverheadGenerator)


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
