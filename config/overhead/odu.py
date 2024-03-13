import copy
from enum import Enum

from utils import OtnField, Position, Dimension
from utils import OtnFieldTypes
from .inner import TcmInnerFields, PmInnerFields


class OduOverheads(Enum):
    res1: OtnField = OtnField(name="res1", field_type=OtnFieldTypes.RES,
        position=Position(col=0, row=1), dimension=Dimension(nrows=1, ncols=2))
    pm_tcm: OtnField = OtnField(name="pm_tcm", field_type=OtnFieldTypes.PM_TCM,
        position=Position(col=2, row=1), dimension=Dimension(nrows=1, ncols=1))
    exp1: OtnField = OtnField(name="exp1", field_type=OtnFieldTypes.EXP,
        position=Position(col=3, row=1), dimension=Dimension(nrows=1, ncols=1))
    tcm6: OtnField = OtnField(name="tcm6", field_type=OtnFieldTypes.TCM,
        position=Position(col=4, row=1), dimension=Dimension(nrows=1, ncols=3),
        inner_fields=copy.deepcopy(TcmInnerFields.get_fields()))
    tcm5: OtnField = OtnField(name="tcm5", field_type=OtnFieldTypes.TCM,
        position=Position(col=7, row=1), dimension=Dimension(nrows=1, ncols=3),
        inner_fields=copy.deepcopy(TcmInnerFields.get_fields()))
    tcm4: OtnField = OtnField( name="tcm4", field_type=OtnFieldTypes.TCM,
        position=Position(col=10, row=1), dimension=Dimension(nrows=1, ncols=3),
        inner_fields=copy.deepcopy(TcmInnerFields.get_fields()))
    exp2: OtnField = OtnField( name="exp2", field_type=OtnFieldTypes.EXP,
        position=Position(col=13, row=1), dimension=Dimension(nrows=1, ncols=1))
    tcm3: OtnField = OtnField(name="tcm3", field_type=OtnFieldTypes.TCM,
        position=Position(col=0, row=2), dimension=Dimension(nrows=1, ncols=3),
        inner_fields=copy.deepcopy(TcmInnerFields.get_fields()))
    tcm2: OtnField = OtnField( name="tcm2", field_type=OtnFieldTypes.TCM,
        position=Position(col=3, row=2), dimension=Dimension(nrows=1, ncols=3),
        inner_fields=copy.deepcopy(TcmInnerFields.get_fields()))
    tcm1: OtnField = OtnField( name="tcm1", field_type=OtnFieldTypes.TCM,
        position=Position(col=6, row=2), dimension=Dimension(nrows=1, ncols=3),
        inner_fields=copy.deepcopy(TcmInnerFields.get_fields()))
    pm: OtnField = OtnField( name="pm", field_type=OtnFieldTypes.PM,
        position=Position(col=9, row=2), dimension=Dimension(nrows=1, ncols=3),
        inner_fields=copy.deepcopy(PmInnerFields.get_fields()))
    exp3: OtnField = OtnField( name="exp3", field_type=OtnFieldTypes.EXP,
        position=Position(col=12, row=2), dimension=Dimension(nrows=1, ncols=2))
    gcc1: OtnField = OtnField(name="gcc1", field_type=OtnFieldTypes.GCC,
        position=Position(col=0, row=3), dimension=Dimension(nrows=1, ncols=2))
    gcc2: OtnField = OtnField(name="gcc2", field_type=OtnFieldTypes.GCC,
        position=Position(col=2, row=3), dimension=Dimension(nrows=1, ncols=2))
    aps_pcc: OtnField = OtnField(name="aps_pcc", field_type=OtnFieldTypes.APS_PCC,
        position=Position(col=4, row=3), dimension=Dimension(nrows=1, ncols=4))
    res2: OtnField = OtnField(name="res2", field_type=OtnFieldTypes.RES,
        position=Position(col=8, row=3), dimension=Dimension(nrows=1, ncols=6))
