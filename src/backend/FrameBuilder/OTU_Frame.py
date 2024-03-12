from Configuration.OTN_Fields_Config import OTN_OH
from Exceptions.Custom_Exception import CustomException
import logging
from tabulate import tabulate

class OTU_Frame:

    def __init__(self , Frame):
        self.Frame = Frame
        self.OTU_Columns = None
        self.FA_Columns = None
        self.OTU_Overhead_data_mapper = {}
        self.FA_Overhead_data_mapper = {}
        self.OTU_OH = [
            OTN_OH.OTU_SM, OTN_OH.OTU_GCC0, OTN_OH.OTU_OSMC, OTN_OH.OTU_RES
        ]

        self.FA_OH = [
            OTN_OH.FA_FAS , OTN_OH.FA_MFAS]

        try:
            self.OTU_OverHead_Field_Constructor()
            self.OTU_SM_Overhead_Constructor()
            self.Frame_Alignment_overheads_Constructor()
        except (KeyError,TypeError) as e:
            print(f"# Error in otu : {e}")
            logging.error(e)

    def OTU_OverHead_Column_Data(self):

        try:
            self.OTU_Columns = self.Frame[0][7:15]
            return self.OTU_Columns

        except CustomException as e:
            logging.error(f"An unexpected error occurred: {e}")
            return None

    def FA_overhead_column_data(self):
        self.FA_Columns = self.Frame[0][0:7]
        return self.FA_Columns

    def OTU_OverHead_Field_Constructor(self):

        for i in self.OTU_OH:
            self.OTU_Overhead_data_mapper[i] = (
                self.Frame[i.value.row_num][i.value.column_start:i.value.column_end]
            )

    def OTU_SM_Overhead_Constructor(self):


        self.OTU_Overhead_data_mapper[OTN_OH.OTU_SM_TTI] = self.OTU_Overhead_data_mapper[OTN_OH.OTU_SM][0]
        self.OTU_Overhead_data_mapper[OTN_OH.OTU_SM_BIP_8] = self.OTU_Overhead_data_mapper[OTN_OH.OTU_SM][1]

        OTU_SM_Data = self.OTU_Overhead_data_mapper[OTN_OH.OTU_SM][2]
        binary_data = bin(int(OTU_SM_Data, 16))[2:].zfill(8)

        self.OTU_Overhead_data_mapper[OTN_OH.OTU_SM_BEI_BIAE] = int(binary_data[0:4], 2) % 10
        self.OTU_Overhead_data_mapper[OTN_OH.OTU_SM_BDI] = int(binary_data[4]) % 10
        self.OTU_Overhead_data_mapper[OTN_OH.OTU_SM_IAE] = int(binary_data[5], 2) % 10
        self.OTU_Overhead_data_mapper[OTN_OH.OTU_SM_STAT] = int(binary_data[6:8], 2) % 10


    def Frame_Alignment_overheads_Constructor(self):
        for i in self.FA_OH:
            self.FA_Overhead_data_mapper[i] = (
                self.Frame[i.value.row_num][i.value.column_start:i.value.column_end]
            )


    def OTU_OverHead_Field_Finder(self , OTU_Field):
        try:
            return self.OTU_Overhead_data_mapper[OTU_Field]
        except (AttributeError, KeyError) as e:
            print(f"Error : {e}")
    def FA_OverHead_Field_Finder(self , FA_Field):
            return self.FA_Overhead_data_mapper[FA_Field]

    def Visualize_OTU(self):
        print("\nThe otu overheads are :  ")
        print("-----------------------------------")
        for i in self.OTU_OH:
            field_data = self.OTU_OverHead_Field_Finder(i)
            print(f"{i} field : {field_data} \n ")
            if i is OTN_OH.OTU_SM:
                print("OTU_SM details : \n ")
                print(f"\tSM_BEI_BIAE is : {self.OTU_Overhead_data_mapper[OTN_OH.OTU_SM_BEI_BIAE]}")
                print(f"\tSM_BDI is : {self.OTU_Overhead_data_mapper[OTN_OH.OTU_SM_BDI]}")
                print(f"\tSM_IAE is : {self.OTU_Overhead_data_mapper[OTN_OH.OTU_SM_IAE]}")
                print(f"\tSM_STAT is : {self.OTU_Overhead_data_mapper[OTN_OH.OTU_SM_STAT]}")
                print(f"\tSM_TTI is : {self.OTU_Overhead_data_mapper[OTN_OH.OTU_SM_TTI]}")
                print(f"\tSM_BIP_8 is : {self.OTU_Overhead_data_mapper[OTN_OH.OTU_SM_BIP_8]} \n")

        print("-----------------------------------")
        return ""
    def OTU_Table_Frame(self):
        self.OTU_headers = [ "OTU_SM","OTU_GCC0" ,"OTN_OSMC" , "OTU_RES"]

        self.OTU_Frame = [
            self.OTU_Overhead_data_mapper[OTN_OH.OTU_SM],
            self.OTU_Overhead_data_mapper[OTN_OH.OTU_GCC0],
            self.OTU_Overhead_data_mapper[OTN_OH.OTU_OSMC],
        ]
        table = tabulate([self.OTU_Frame] , headers= self.OTU_headers , tablefmt="grid" , colalign=("center",))
        print(table)

    def visualize_fa(self):

        print("\nThe fa overheads are :  ")
        print("-----------------------------------")
        for i in self.FA_OH:
            print(f"{i} field is : {self.FA_Overhead_data_mapper[i]}")
        print("-----------------------------------")
        return ""