from utils.field_types import OtnFieldTypes
from utils.data_classes import OtnField, Position, Dimension

from .base import OtnOverheads


class OpuOverheads(OtnOverheads):
    jc1: OtnField = OtnField(name="jc1", field_type=OtnFieldTypes.JC,
        position=Position(col=1, row=0), dimension=Dimension(nrows=1, ncols=1))
    jc2: OtnField = OtnField(name="jc2", field_type=OtnFieldTypes.JC,
        position=Position(col=1, row=1), dimension=Dimension(nrows=1, ncols=1))
    jc3: OtnField = OtnField(name="jc3", field_type=OtnFieldTypes.JC,
        position=Position(col=1, row=2), dimension=Dimension(nrows=1, ncols=1))
    jc4: OtnField = OtnField(name="jc4", field_type=OtnFieldTypes.JC,
        position=Position(col=0, row=0), dimension=Dimension(nrows=1, ncols=1))
    jc5: OtnField = OtnField(name="jc5", field_type=OtnFieldTypes.JC,
        position=Position(col=0, row=1), dimension=Dimension(nrows=1, ncols=1))
    jc6: OtnField = OtnField(name="jc6", field_type=OtnFieldTypes.JC,
        position=Position(col=0, row=2), dimension=Dimension(nrows=1, ncols=1))
    njo: OtnField = OtnField(name="njo", field_type=OtnFieldTypes.NJO,
        position=Position(col=1, row=3), dimension=Dimension(nrows=1, ncols=1))
    pjo: OtnField = OtnField(name="pjo", field_type=OtnFieldTypes.PJO,
        position=Position(col=2, row=3), dimension=Dimension(nrows=1, ncols=1))
    psi: OtnField = OtnField(name="psi", field_type=OtnFieldTypes.PSI,
        position=Position(col=0, row=3), dimension=Dimension(nrows=1, ncols=1))
