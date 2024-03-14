from utils import OtnField, OtnFieldTypes, Position, Dimension

from .base import OtnOverheads
from .inner import SmInnerFields


class OtuOverheads(OtnOverheads):
    fas: OtnField = OtnField(name="fas", field_type=OtnFieldTypes.FAS,
        position=Position(col=0, row=0), dimension=Dimension(nrows=1, ncols=6))
    mfas: OtnField = OtnField(name="mfas", field_type=OtnFieldTypes.MFAS,
        position=Position(col=6, row=0), dimension=Dimension(nrows=1, ncols=1))
    sm: OtnField = OtnField(name="sm", field_type=OtnFieldTypes.SM,
        position=Position(col=7, row=0), dimension=Dimension(nrows=1, ncols=3),
        inner_fields=SmInnerFields.get_fields())
    gcc0: OtnField = OtnField(name="gcc0", field_type=OtnFieldTypes.GCC,
        position=Position(col=10, row=0), dimension=Dimension(nrows=1, ncols=2))
    osmc: OtnField = OtnField(name="osmc", field_type=OtnFieldTypes.OSMC,
        position=Position(col=12, row=0), dimension=Dimension(nrows=1, ncols=1))
    res: OtnField = OtnField(name="res", field_type=OtnFieldTypes.RES,
        position=Position(col=13, row=0), dimension=Dimension(nrows=1, ncols=1))
