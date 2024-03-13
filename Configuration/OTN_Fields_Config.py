from enum import Enum
from Configuration.OTN_Field_Data import otn_field_data

class OTN_OH(Enum):


# OPU Overheads Config

    OPU_JC1 = otn_field_data("OPU_JC1", parent_type="OPU", row_num=0, column_start=15 , column_end= 17)
    OPU_JC2 = otn_field_data("OPU_JC2", parent_type="OPU", row_num=1, column_start=15)
    OPU_JC3 = otn_field_data("OPU_JC3", parent_type="OPU", row_num=2, column_start=15)

    OPU_JC4 = otn_field_data("OPU_JC4", parent_type="OPU", row_num=0, column_start=14)
    OPU_JC5 = otn_field_data("OPU_JC5", parent_type="OPU", row_num=1, column_start=14)
    OPU_JC6 = otn_field_data("OPU_JC6", parent_type="OPU", row_num=2, column_start=14)

    OPU_PSI = otn_field_data("OPU_PSI", parent_type="OPU", row_num=3, column_start=14)
    OPU_NJO_OMFI = otn_field_data("OPU_NJO_OMFI", parent_type="OPU", row_num=3, column_start=15)
    OPU_PJO = otn_field_data("OPU_PJO", parent_type="OPU", row_num=3, column_start=16)

############################################################################################################

# ODU Overheads Config

    ODU_RES1 = otn_field_data("ODU_RES1", parent_type="ODU", row_num=1, column_start=0 , column_end= 2, num_of_bits=16)

    ODU_PM_TCM_DMt1 = otn_field_data("ODU_PM_TCM_DMt1", parent_type="ODU_PM_TCM" , num_of_bits=1)
    ODU_PM_TCM_DMt2 = otn_field_data("ODU_PM_TCM_DMt2", parent_type="ODU_PM_TCM" ,  num_of_bits=1)
    ODU_PM_TCM_DMt3 = otn_field_data("ODU_PM_TCM_DMt3", parent_type="ODU_PM_TCM" , num_of_bits=1)
    ODU_PM_TCM_DMt4 = otn_field_data("ODU_PM_TCM_DMt4", parent_type="ODU_PM_TCM" , num_of_bits=1)
    ODU_PM_TCM_DMt5 = otn_field_data("ODU_PM_TCM_DMt5", parent_type="ODU_PM_TCM" , num_of_bits=1)
    ODU_PM_TCM_DMt6 = otn_field_data("ODU_PM_TCM_DMt6", parent_type="ODU_PM_TCM" , num_of_bits=1)

    ODU_PM_TCM = otn_field_data("ODU_PM_TCM", parent_type="ODU", row_num=1, column_start=2 , column_end=3)

    ODU_EXP1 = otn_field_data("ODU_EXP1", parent_type="ODU", row_num=1, column_start=3 , column_end=4)
    ODU_EXP2 = otn_field_data("ODU_EXP2", parent_type="ODU", row_num=1, column_start=13 , column_end = 14)

    ODU_TCMi_inner_levels = {
        'TTI': None ,
        'BIP_8': None ,
        'BEI_BIAE' : None ,
        'BDI' : None,
        'STAT' : None
    }


    ODU_TCM1 = otn_field_data("ODU_TCM1", parent_type="ODU", row_num=2, column_start=6,column_end=9 , num_of_bits=24, inner_levels= ODU_TCMi_inner_levels)
    ODU_TCM2 = otn_field_data("ODU_TCM2", parent_type="ODU", row_num=2, column_start=3 , column_end = 6 , num_of_bits=24, inner_levels= ODU_TCMi_inner_levels)
    ODU_TCM3 = otn_field_data("ODU_TCM3", parent_type="ODU", row_num=2, column_start=0 , column_end = 3 ,num_of_bits=24, inner_levels= ODU_TCMi_inner_levels)
    ODU_TCM4 = otn_field_data("ODU_TCM4", parent_type="ODU", row_num=1, column_start=10, column_end = 13 ,num_of_bits=24, inner_levels= ODU_TCMi_inner_levels)
    ODU_TCM5 = otn_field_data("ODU_TCM5", parent_type="ODU", row_num=1, column_start=7, column_end = 10,num_of_bits=24, inner_levels= ODU_TCMi_inner_levels)
    ODU_TCM6 = otn_field_data("ODU_TCM6", parent_type="ODU", row_num=1, column_start=4, column_end = 7 ,num_of_bits=24, inner_levels= ODU_TCMi_inner_levels)




    # ODU_PM Config :

    ODU_PM_TTI = otn_field_data("ODU_PM_TTI", parent_type="ODU")
    ODU_PM_BIP_8 = otn_field_data("ODU_PM_BIP_8", parent_type="ODU")
    ODU_PM_BEI_BIAE = otn_field_data("ODU_PM_BEI_BIAE", parent_type="ODU" , num_of_bits=4)
    ODU_PM_BDI = otn_field_data("ODU_PM_BDI", parent_type="ODU",  num_of_bits=1)
    ODU_PM_STAT = otn_field_data("ODU_PM_STAT", parent_type="ODU", num_of_bits=3)


    ODU_PM = otn_field_data("ODU_PM", parent_type="ODU", row_num=2, column_start=9, column_end=12 ,num_of_bits=24)

    ODU_EXP3 = otn_field_data("ODU_EXP3", parent_type="ODU", row_num=1, column_start=12 , column_end= 14, num_of_bits=16)

    ODU_GCC1 = otn_field_data("ODU_GCC1", parent_type="ODU", row_num=3, column_start=0, column_end= 2,num_of_bits=16)
    ODU_GCC2 = otn_field_data("ODU_GCC2", parent_type="ODU", row_num=3, column_start=2, column_end= 4, num_of_bits=16)

    ODU_APS_PCC = otn_field_data("ODU_APS_PCC", parent_type="ODU", row_num=3, column_start=4, column_end=8 ,  num_of_bits=32)
    ODU_RES2 = otn_field_data("ODU_RES2", parent_type="ODU", row_num=3, column_start=8, column_end= 14 ,num_of_bits=48)

############################################################################################################

# OTU Overheads Config:
    
    OTU_SM_TTI = otn_field_data("OTU_SM_TTI", parent_type="OTU_SM")
    OTU_SM_BIP_8 = otn_field_data("OTU_SM_BIP_8", parent_type="OTU_SM")
    OTU_SM_BEI_BIAE = otn_field_data("OTU_SM_BEI_BIAE", parent_type="OTU_SM" , num_of_bits=4)
    OTU_SM_BDI = otn_field_data("OTU_SM_BDI", parent_type="OTU_SM" , num_of_bits=1)
    OTU_SM_IAE = otn_field_data("OTU_SM_IAE", parent_type="OTU_SM", num_of_bits=1)
    OTU_SM_STAT = otn_field_data("OTU_SM_STAT", parent_type="OTU_SM" , num_of_bits=2)

    OTU_SM = otn_field_data("OTU_SM", parent_type="OTU", row_num=0, column_start=7 , column_end=10 , num_of_bits=24)

    OTU_GCC0 = otn_field_data("OTU_GCC0", parent_type="OTU", row_num=0, column_start=10 , column_end=12, num_of_bits=16)
    OTU_OSMC = otn_field_data("OTU_OSMC", parent_type="OTU", row_num=0, column_start=12 , column_end=13)
    OTU_RES = otn_field_data("OTU_RES", parent_type="OTU", row_num=0, column_start=13 , column_end= 14)

############################################################################################################


# Frame Alignment Overheads Config :

    FA_FAS = otn_field_data("FA_FAS", parent_type="FA", row_num=0, column_start= 0, column_end= 6, num_of_bits=48)
    FA_MFAS = otn_field_data("FA_MFAS", parent_type="FA", row_num=0, column_start= 6 , column_end=7)