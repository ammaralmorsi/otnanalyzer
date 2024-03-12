from Configuration.OTN_Fields_Config import OTN_OH
from Exceptions.Custom_Exception import CustomException
import logging

class ODU_Frame:

    def __init__(self , Frame):

        self.Frame = Frame
        self.ODU_Columns = None
        self.ODU_Overhead_data_mapper = {}
        self.ODU_OH = [
            OTN_OH.ODU_RES1, OTN_OH.ODU_PM_TCM, OTN_OH.ODU_EXP1, OTN_OH.ODU_TCM6, OTN_OH.ODU_TCM5,
            OTN_OH.ODU_TCM4, OTN_OH.ODU_TCM3, OTN_OH.ODU_TCM2, OTN_OH.ODU_TCM1, OTN_OH.ODU_PM,
            OTN_OH.ODU_EXP2, OTN_OH.ODU_GCC1, OTN_OH.ODU_GCC2, OTN_OH.ODU_APS_PCC, OTN_OH.ODU_RES2
        ]
        self.TCMi_keys = [
            OTN_OH.ODU_TCM1, OTN_OH.ODU_TCM2, OTN_OH.ODU_TCM3,
            OTN_OH.ODU_TCM4, OTN_OH.ODU_TCM5, OTN_OH.ODU_TCM6
        ]

        try:
            self.ODU_OverHead_Field_Constructor()
            self.ODU_PM_inner_Overhead_Constrcutor()
            self.ODU_PM_TCM_DMti_inner_Overhead_Constructor()
            self.ODU_TCMi_inner_Overhead_Constructor()
        except (KeyError , TypeError) as e:
            print(f"# Error in odu : {e}")
            logging.error(e)
    def ODU_OverHead_Column_Data(self):

        try:
            self.ODU_Columns = [row[0:15] for row in self.Frame]
            return self.ODU_Columns

        except CustomException as e:
            logging.error(f"# An unexpected error occurred: {e}")
            return None

    def ODU_OverHead_Field_Constructor(self):

        for i in self.ODU_OH:
            self.ODU_Overhead_data_mapper[i] = (
                self.Frame[i.value.row_num][i.value.column_start:i.value.column_end]
        )

    def ODU_PM_inner_Overhead_Constrcutor(self):
        PM_Data = self.ODU_Overhead_data_mapper[OTN_OH.ODU_PM][2]
        binary_data = bin(int(PM_Data, 16))[2:].zfill(8)

        # format(int(binary_data[5:8], 2), 'x')
        self.ODU_Overhead_data_mapper[OTN_OH.ODU_PM_BEI_BIAE] = int(binary_data[0:4], 2) % 10
        self.ODU_Overhead_data_mapper[OTN_OH.ODU_PM_BDI]  = int(binary_data[4]) % 10
        self.ODU_Overhead_data_mapper[OTN_OH.ODU_PM_STAT] = int(binary_data[5:8], 2) % 10

        self.ODU_Overhead_data_mapper[OTN_OH.ODU_PM_TTI] = self.ODU_Overhead_data_mapper[OTN_OH.ODU_PM][0]
        self.ODU_Overhead_data_mapper[OTN_OH.ODU_PM_BIP_8] = self.ODU_Overhead_data_mapper[OTN_OH.ODU_PM][1]


    def ODU_PM_TCM_DMti_inner_Overhead_Constructor(self):

        PM_TCM_Data = self.ODU_Overhead_data_mapper[OTN_OH.ODU_PM_TCM][0]
        binary_data = bin(int(PM_TCM_Data, 16))[2:].zfill(8)
        self.ODU_Overhead_data_mapper[OTN_OH.ODU_PM_TCM_DMt1] = int(binary_data[0]) % 10
        self.ODU_Overhead_data_mapper[OTN_OH.ODU_PM_TCM_DMt2] = int(binary_data[1]) % 10
        self.ODU_Overhead_data_mapper[OTN_OH.ODU_PM_TCM_DMt3] = binary_data[2]

        self.ODU_Overhead_data_mapper[OTN_OH.ODU_PM_TCM_DMt4] = binary_data[3]
        self.ODU_Overhead_data_mapper[OTN_OH.ODU_PM_TCM_DMt5] = binary_data[4]
        self.ODU_Overhead_data_mapper[OTN_OH.ODU_PM_TCM_DMt6] = binary_data[5]


    def ODU_TCMi_inner_Overhead_Constructor(self):

        for i in self.TCMi_keys:
            ODU_TCMi_Data = self.ODU_Overhead_data_mapper[i][2]
            binary_data = bin(int(ODU_TCMi_Data, 16))[2:].zfill(8)
            i.value.inner_levels['TTI'] = self.ODU_Overhead_data_mapper[i][0]
            i.value.inner_levels['BIP_8'] = self.ODU_Overhead_data_mapper[i][1]
            i.value.inner_levels['BEI_BIAE'] = hex(int(binary_data[0:4], 2))[2:]   # the [2:] to remove the 0x when changed to hex
            i.value.inner_levels['BDI'] = hex(int(binary_data[4], 2))[2:]        # the arg inside the binary_data is the bits inside the field that maps to the data we need
            i.value.inner_levels['STAT'] = hex(int(binary_data[5:8], 2))[2:]



    def ODU_OverHead_Field_Finder(self, ODU_Field):
        return self.ODU_Overhead_data_mapper[ODU_Field]


    def visualize_odu(self):
        print("\nThe odu overheads are :  ")
        print("-----------------------------------")
        for i in self.ODU_OH:
            data = self.ODU_OverHead_Field_Finder(i)
            print(f"{i} field is : {data}")
        print("-----------------------------------")
        return ""



    def visualize_tcmi_odu(self , TCM):
        TCM_OH = [
            'TTI' , 'BIP_8' , 'BEI_BIAE' , 'BDI' , 'STAT' ,
        ]

        print(f"{TCM} levels data are : ")
        for i in TCM_OH:
            print(f"{i} is {TCM.value.inner_levels[i]}")
        return ""



