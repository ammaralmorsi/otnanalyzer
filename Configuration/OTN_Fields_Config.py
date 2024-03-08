from enum import Enum
from Configuration.OTN_Field_Data import OTN_Field_Data

class OTN_OH(Enum):


# OPU Overheads Config

    OPU_JC1 = OTN_Field_Data(parent_type="OPU", row_num=0, column_start=15 , column_end= 17)
    OPU_JC2 = OTN_Field_Data(parent_type="OPU", row_num=1, column_start=15)
    OPU_JC3 = OTN_Field_Data(parent_type="OPU", row_num=2, column_start=15)

    OPU_JC4 = OTN_Field_Data(parent_type="OPU", row_num=0, column_start=14)
    OPU_JC5 = OTN_Field_Data(parent_type="OPU", row_num=1, column_start=14)
    OPU_JC6 = OTN_Field_Data(parent_type="OPU", row_num=2, column_start=14)

    OPU_PSI = OTN_Field_Data(parent_type="OPU", row_num=3, column_start=14)
    OPU_NJO_OMFI = OTN_Field_Data(parent_type="OPU", row_num=3, column_start=15)
    OPU_PJO = OTN_Field_Data(parent_type="OPU", row_num=3, column_start=16)

############################################################################################################

# ODU Overheads Config

    ODU_RES1 = OTN_Field_Data(parent_type="ODU", row_num=1, column_start=2, num_of_bits=16)

    ODU_PM_TCM_DMt1 = OTN_Field_Data(parent_type="ODU_PM_TCM", row_num=0, column_start=2 , num_of_bits=1)
    ODU_PM_TCM_DMt2 = OTN_Field_Data(parent_type="ODU_PM_TCM", row_num=0, column_start=2, num_of_bits=1)
    ODU_PM_TCM_DMt3 = OTN_Field_Data(parent_type="ODU_PM_TCM", row_num=0, column_start=2, num_of_bits=1)
    ODU_PM_TCM_DMt4 = OTN_Field_Data(parent_type="ODU_PM_TCM", row_num = 0, column_start=2, num_of_bits=1)
    ODU_PM_TCM_DMt5 = OTN_Field_Data(parent_type="ODU_PM_TCM", row_num=0, column_start=2, num_of_bits=1)
    ODU_PM_TCM_DMt6 = OTN_Field_Data(parent_type="ODU_PM_TCM", row_num=0, column_start=2, num_of_bits=1)

    ODU_PM_TCM_DMt_inner_levels = {

        'DMt1': ODU_PM_TCM_DMt1,
        'DMt2': ODU_PM_TCM_DMt2,
        'DMt3': ODU_PM_TCM_DMt3,
        'DMt4': ODU_PM_TCM_DMt4,
        'DMt5': ODU_PM_TCM_DMt5,
        'DMt6': ODU_PM_TCM_DMt6

    }

    ODU_PM_TCM = OTN_Field_Data(parent_type="ODU", row_num=1, column_start=2 , inner_levels=ODU_PM_TCM_DMt_inner_levels)


    ODU_EXP1 = OTN_Field_Data(parent_type="ODU", row_num=1, column_start=2)
    ODU_EXP2 = OTN_Field_Data(parent_type="ODU", row_num=1, column_start=2)


    ODU_TCMi_TTI = OTN_Field_Data(parent_type="ODU_TCM")
    ODU_TCMi_BIP8 = OTN_Field_Data(parent_type="ODU_TCM")
    ODU_TCMi_BEI_BIAE = OTN_Field_Data(parent_type="ODU_TCM", num_of_bits=4)
    ODU_TCMi_BDI = OTN_Field_Data(parent_type="ODU_TCM" , num_of_bits=1)
    ODU_TCMi_STAT = OTN_Field_Data(parent_type="ODU_TCM" , num_of_bits=3)

    ODU_TCMi_inner_levels = {
        'TTI': ODU_TCMi_TTI ,
        'BIP8': ODU_TCMi_BIP8 ,
        'BEI_BIAE' : ODU_TCMi_BEI_BIAE ,
        'BDI' : ODU_TCMi_BDI,
        'STAT' : ODU_TCMi_STAT
    }


    ODU_TCM1 = OTN_Field_Data(parent_type="ODU", row_num=1, column_start=2, num_of_bits=24, inner_levels= ODU_TCMi_inner_levels)
    ODU_TCM2 = OTN_Field_Data(parent_type="ODU", row_num=1, column_start=2, num_of_bits=24, inner_levels= ODU_TCMi_inner_levels)
    ODU_TCM3 = OTN_Field_Data(parent_type="ODU", row_num=1, column_start=2, num_of_bits=24, inner_levels= ODU_TCMi_inner_levels)
    ODU_TCM4 = OTN_Field_Data(parent_type="ODU", row_num=1, column_start=2, num_of_bits=24, inner_levels= ODU_TCMi_inner_levels)
    ODU_TCM5 = OTN_Field_Data(parent_type="ODU", row_num=1, column_start=2, num_of_bits=24, inner_levels= ODU_TCMi_inner_levels)
    ODU_TCM6 = OTN_Field_Data(parent_type="ODU", row_num=1, column_start=2, num_of_bits=24, inner_levels= ODU_TCMi_inner_levels)




# ODU_PM Config :

    ODU_PM_TTI = OTN_Field_Data(parent_type="ODU")
    ODU_PM_BIP_8 = OTN_Field_Data(parent_type="ODU")
    ODU_PM_BEI_BIAE = OTN_Field_Data(parent_type="ODU" , num_of_bits=4)
    ODU_PM_BDI = OTN_Field_Data(parent_type="ODU",  num_of_bits=1)
    ODU_PM_STAT = OTN_Field_Data(parent_type="ODU", num_of_bits=3)

    ODU_PM_inner_levels = {
        'TTI': ODU_PM_TTI,
        'BIP_8': ODU_PM_BIP_8,
        'BEI_BIAE': ODU_PM_BEI_BIAE,
        'BDI': ODU_PM_BDI,
        'STAT': ODU_PM_STAT,
    }

    ODU_PM = OTN_Field_Data(parent_type="ODU", row_num=1, column_start=2, num_of_bits=24 , inner_levels=ODU_PM_inner_levels)



    ODU_EXP3 = OTN_Field_Data(parent_type="ODU", row_num=1, column_start=2, num_of_bits=16)

    ODU_GCC1 = OTN_Field_Data(parent_type="ODU", row_num=1, column_start=2, num_of_bits=16)
    ODU_GCC2 = OTN_Field_Data(parent_type="ODU", row_num=1, column_start=2, num_of_bits=16)

    ODU_APS_PCC = OTN_Field_Data(parent_type="ODU", row_num=1, column_start=2, num_of_bits=32)
    ODU_RES2 = OTN_Field_Data(parent_type="ODU", row_num=1, column_start=2, num_of_bits=48)

############################################################################################################

# OTU Overheads Config:

    OTU_SM_TTI = OTN_Field_Data(parent_type="OTU_SM")
    OTU_SM_BIP_8 = OTN_Field_Data(parent_type="OTU_SM")
    OTU_SM_BEI_BIAE = OTN_Field_Data(parent_type="OTU_SM" , num_of_bits=4)
    OTU_SM_BDI = OTN_Field_Data(parent_type="OTU_SM" , num_of_bits=1)
    OTU_SM_IAE = OTN_Field_Data(parent_type="OTU_SM", num_of_bits=1)
    OTU_SM_STAT = OTN_Field_Data(parent_type="OTU_SM" , num_of_bits=2)

    OTU_SM_inner_levels = {

        'TTI' : OTU_SM_TTI ,
        'BIP_8': OTU_SM_BIP_8 ,
        'BEI_BIAE': OTU_SM_BEI_BIAE ,
        'BDI': OTU_SM_BDI ,
        'IAE': OTU_SM_IAE ,
        'STAT': OTU_SM_STAT

    }

    OTU_SM = OTN_Field_Data(parent_type="OTU", row_num=0, column_start=7 , column_end=9 , num_of_bits=24 , inner_levels= OTU_SM_inner_levels)

    OTU_GCC0 = OTN_Field_Data(parent_type="OTU", row_num=0, column_start=10 , column_end=11, num_of_bits=16)
    OTU_OSMC = OTN_Field_Data(parent_type="OTU", row_num=0, column_start=12)
    OTU_RES = OTN_Field_Data(parent_type="OTU", row_num=0, column_start=13)

############################################################################################################


# Frame Alignment Overheads Config :

    FA_FAS = OTN_Field_Data(parent_type="FA", row_num=0, column_start= 0, column_end= 5, num_of_bits=48)
    FA_MFAS = OTN_Field_Data(parent_type="FA", row_num=0, column_start= 6)