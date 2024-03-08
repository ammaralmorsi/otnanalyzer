from Configuration.OTN_Fields_Config import OTN_OH
from Exceptions.Custom_Exception import CustomException
import logging

class ODU_Frame:

    def __init__(self , Frame):
        self.Frame = Frame
        self.ODU_Columns = None
        self.ODU_Overhead_data_mapper = {}
        self.ODU_OverHead_Field_Constructor()
        self.ODU_PM_inner_Overhead_Constrcutor()


    def ODU_OverHead_Column_Data(self):

        try:
            self.ODU_Columns = [row[0:15] for row in self.Frame]
            return self.ODU_Columns

        except CustomException as e:
            logging.error(f"An unexpected error occurred: {e}")
            return None

    def ODU_OverHead_Field_Constructor(self):

        self.ODU_Overhead_data_mapper[OTN_OH.ODU_RES1] = (
            self.Frame[OTN_OH.ODU_RES1.value.row_num]
            [OTN_OH.ODU_RES1.value.column_start:OTN_OH.ODU_RES1.value.column_end]
        )

        self.ODU_Overhead_data_mapper[OTN_OH.ODU_PM_TCM] = (
            self.Frame[OTN_OH.ODU_PM_TCM.value.row_num]
            [OTN_OH.ODU_PM_TCM.value.column_start]
        )

        self.ODU_Overhead_data_mapper[OTN_OH.ODU_EXP1] = (
            self.Frame[OTN_OH.ODU_EXP1.value.row_num]
            [OTN_OH.ODU_EXP1.value.column_start]
        )

        self.ODU_Overhead_data_mapper[OTN_OH.ODU_TCM6] = (
            self.Frame[OTN_OH.ODU_TCM6.value.row_num]
            [OTN_OH.ODU_TCM6.value.column_start:OTN_OH.ODU_TCM6.value.column_end]
        )

        self.ODU_Overhead_data_mapper[OTN_OH.ODU_TCM5] = (
            self.Frame[OTN_OH.ODU_TCM5.value.row_num]
            [OTN_OH.ODU_TCM5.value.column_start:OTN_OH.ODU_TCM5.value.column_end]
        )

        self.ODU_Overhead_data_mapper[OTN_OH.ODU_TCM4] = (
            self.Frame[OTN_OH.ODU_TCM4.value.row_num]
            [OTN_OH.ODU_TCM4.value.column_start:OTN_OH.ODU_TCM4.value.column_end]
        )

        self.ODU_Overhead_data_mapper[OTN_OH.ODU_TCM3] = (
            self.Frame[OTN_OH.ODU_TCM3.value.row_num]
            [OTN_OH.ODU_TCM3.value.column_start:OTN_OH.ODU_TCM3.value.column_end]
        )

        self.ODU_Overhead_data_mapper[OTN_OH.ODU_TCM2] = (
            self.Frame[OTN_OH.ODU_TCM2.value.row_num]
            [OTN_OH.ODU_TCM2.value.column_start:OTN_OH.ODU_TCM2.value.column_end]
        )

        self.ODU_Overhead_data_mapper[OTN_OH.ODU_TCM1] = (
            self.Frame[OTN_OH.ODU_TCM1.value.row_num]
            [OTN_OH.ODU_TCM1.value.column_start:OTN_OH.ODU_TCM1.value.column_end]
        )

        self.ODU_Overhead_data_mapper[OTN_OH.ODU_PM] = self.Frame[OTN_OH.ODU_PM.value.row_num][OTN_OH.ODU_PM.value.column_start:OTN_OH.ODU_PM.value.column_end]


        self.ODU_Overhead_data_mapper[OTN_OH.ODU_EXP2] = (
            self.Frame[OTN_OH.ODU_EXP2.value.row_num]
            [OTN_OH.ODU_EXP2.value.column_start]
        )

        self.ODU_Overhead_data_mapper[OTN_OH.ODU_GCC1] = (
            self.Frame[OTN_OH.ODU_GCC1.value.row_num]
            [OTN_OH.ODU_GCC1.value.column_start:OTN_OH.ODU_GCC1.value.column_end]
        )

        self.ODU_Overhead_data_mapper[OTN_OH.ODU_GCC2] = (
            self.Frame[OTN_OH.ODU_GCC2.value.row_num]
            [OTN_OH.ODU_GCC2.value.column_start:OTN_OH.ODU_GCC2.value.column_end]
        )
        self.ODU_Overhead_data_mapper[OTN_OH.ODU_APS_PCC] = (
            self.Frame[OTN_OH.ODU_APS_PCC.value.row_num]
            [OTN_OH.ODU_APS_PCC.value.column_start:OTN_OH.ODU_APS_PCC.value.column_end]
        )

        self.ODU_Overhead_data_mapper[OTN_OH.ODU_RES2] = (
            self.Frame[OTN_OH.ODU_RES2.value.row_num]
            [OTN_OH.ODU_RES2.value.column_start:OTN_OH.ODU_RES2.value.column_end]
        )


    def ODU_PM_inner_Overhead_Constrcutor(self):
        PM_Data = self.ODU_Overhead_data_mapper[OTN_OH.ODU_PM][2]
        print(PM_Data)
        binary_data = bin(int(PM_Data, 16))[2:].zfill(8)

        self.ODU_Overhead_data_mapper = {
            OTN_OH.ODU_PM_BEI_BIAE: int(binary_data[0:4], 2),
            OTN_OH.ODU_PM_BDI: int(binary_data[4]),
            OTN_OH.ODU_PM_STAT: int(binary_data[5:8], 2)
        }


    def ODU_OverHead_Field_Finder(self , ODU_Field):
        return self.ODU_Overhead_data_mapper[ODU_Field]