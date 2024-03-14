from utils import OtnField, OtnFieldTypes, Position, Dimension

from .base import OtnOverheads



class PmInnerFields(OtnOverheads):
    tti: OtnField = OtnField(name="pm_tti", field_type=OtnFieldTypes.PM_TTI,
        position=Position(col=0, row=0), dimension=Dimension(nrows=1, ncols=8))
    bip8: OtnField = OtnField(name="pm_bip8", field_type=OtnFieldTypes.PM_BIP8,
        position=Position(col=8, row=0), dimension=Dimension(nrows=1, ncols=8))
    bei: OtnField = OtnField(name="pm_bei", field_type=OtnFieldTypes.PM_BEI,
        position=Position(col=16, row=0), dimension=Dimension(nrows=1, ncols=4))
    bdi: OtnField = OtnField(name="pm_bdi", field_type=OtnFieldTypes.PM_BDI,
        position=Position(col=20, row=0), dimension=Dimension(nrows=1, ncols=1))
    stat: OtnField = OtnField(name="pm_stat", field_type=OtnFieldTypes.PM_STAT,
        position=Position(col=21, row=0), dimension=Dimension(nrows=1, ncols=3))


class TcmInnerFields(OtnOverheads):
    tti: OtnField = OtnField(name="tcm_tti", field_type=OtnFieldTypes.TCM_TTI,
        position=Position(col=0, row=0), dimension=Dimension(nrows=1, ncols=8))
    bip8: OtnField = OtnField(name="tcm_bip8", field_type=OtnFieldTypes.TCM_BIP8,
        position=Position(col=8, row=0), dimension=Dimension(nrows=1, ncols=8))
    bei_biae: OtnField = OtnField(name="tcm_bei_biae", field_type=OtnFieldTypes.TCM_BEI_BIAE,
        position=Position(col=16, row=0), dimension=Dimension(nrows=1, ncols=4))
    bdi: OtnField = OtnField(name="tcm_bdi", field_type=OtnFieldTypes.TCM_BDI,
        position=Position(col=20, row=0), dimension=Dimension(nrows=1, ncols=1))
    stat: OtnField = OtnField(name="tcm_stat", field_type=OtnFieldTypes.TCM_STAT,
        position=Position(col=21, row=0), dimension=Dimension(nrows=1, ncols=3))


class SmInnerFields(OtnOverheads):
    tti: OtnField = OtnField(name="sm_tti", field_type=OtnFieldTypes.SM_TTI,
        position=Position(col=0, row=0), dimension=Dimension(nrows=1, ncols=8))
    bip8: OtnField = OtnField(name="sm_bip8", field_type=OtnFieldTypes.SM_BIP8,
        position=Position(col=8, row=0), dimension=Dimension(nrows=1, ncols=8))
    bei_biae: OtnField = OtnField(name="sm_bei_biae", field_type=OtnFieldTypes.SM_BEI_BIAE,
        position=Position(col=16, row=0), dimension=Dimension(nrows=1, ncols=4))
    bdi: OtnField = OtnField(name="sm_bdi", field_type=OtnFieldTypes.SM_BDI,
        position=Position(col=20, row=0), dimension=Dimension(nrows=1, ncols=1))
    stat: OtnField = OtnField(name="sm_stat", field_type=OtnFieldTypes.SM_STAT,
        position=Position(col=21, row=0), dimension=Dimension(nrows=1, ncols=3))
