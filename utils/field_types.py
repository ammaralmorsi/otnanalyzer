import enum


class OtnFrameTypes(enum.Enum):
    OPU = enum.auto()
    ODU = enum.auto()
    OTU = enum.auto()


class OtnPayloadTypes(enum.Enum):
    PRBS = enum.auto()
    NULL = enum.auto()


class OtnFieldTypes(enum.Enum):
    OPU_PAYLOAD_PRBS = enum.auto()
    OPU_PAYLOAD_NULL = enum.auto()

    ODU_PAYLOAD_PRBS = enum.auto()
    ODU_PAYLOAD_NULL = enum.auto()

    FAS = enum.auto()
    MFAS = enum.auto()

    SM = enum.auto()
    SM_TTI = enum.auto()
    SM_BIP8 = enum.auto()
    SM_BEI_BIAE = enum.auto()
    SM_BDI = enum.auto()
    SM_STAT = enum.auto()
    OSMC = enum.auto()

    RES = enum.auto()
    PM_TCM = enum.auto()
    EXP = enum.auto()
    TCM = enum.auto()
    TCM_TTI = enum.auto()
    TCM_BIP8 = enum.auto()
    TCM_BEI_BIAE = enum.auto()
    TCM_BDI = enum.auto()
    TCM_STAT = enum.auto()
    PM = enum.auto()
    PM_TTI = enum.auto()
    PM_BIP8 = enum.auto()
    PM_BEI = enum.auto()
    PM_BDI = enum.auto()
    PM_STAT = enum.auto()
    GCC = enum.auto()
    APS_PCC = enum.auto()

    JC = enum.auto()
    PSI = enum.auto()
    PJO = enum.auto()
    NJO = enum.auto()
