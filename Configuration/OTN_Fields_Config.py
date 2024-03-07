from enum import Enum



class OPU_OH(Enum):
    OPU_JC1 = "OPU_JC1"
    OPU_JC2 = "OPU_JC2"
    OPU_JC3 = "OPU_JC3"

    OPU_JC4 = "OPU_JC4"
    OPU_JC5 = "OPU_JC5"
    OPU_JC6 = "OPU_JC6"

    OPU_PSI = "PSI"
    OPU_NJO = "NJO"
    OPU_PJO = "PJO"

class ODU_OH(Enum):

    ODU_RES1 = ""
    ODU_PM_TCM = " "
    ODU_EXP1 = ""
    ODU_TCM6 = ""
    ODU_TCM5 = " "
    ODU_TCM4 = " "
    ODU_EXP2 = " "
    ODU_TCM3 = " "
    ODU_TCM2 = " "

    ODU_TCM1 = ""
    ODU_PM_TTI = ""
    ODU_PM_BIP_8 = ""
    ODU_PM_BEI_BIAE = ""
    ODU_PM_BDI = " "
    ODU_PM_STAT = ""
    ODU_EXP3 = ""
    ODU_GCC1 = ""

    ODU_GCC2 = ""
    ODU_APS_PCC = " "
    ODU_RES2 = ""

class OTU_OH(Enum):

    OTU_SM_TTI = ','
    OTU_SM_BIP_8 = ', '
    OTU_SM_BEI_BIAE =', '
    OTU_SM_BDI =','
    OTU_SM_IAE = ','
    OTU_SM_STAT = ','

    OTU_GCC0 = "GCC0"
    OTU_OSMC = "OSMC"
    OTU_RES = "RES"

class FrameAlignment_OH(Enum):

    FA_FAS = ""
    FA_MFAS = ""

