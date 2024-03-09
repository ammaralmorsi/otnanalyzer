from Configuration.OTN_Fields_Config import OTN_OH
from Exceptions.Custom_Exception import CustomException
import logging

class OTU_Frame:

    def __init__(self , Frame):
        self.Frame = Frame
        self.OTU_Columns = None
        self.OTU_Overhead_data_mapper = {}
        self.OTU_OverHead_Field_Constructor()
        self.OTU_SM_Overhead_Constructor()

    def OTU_OverHead_Column_Data(self):

        try:
            self.OTU_Columns = [row[7:14] for row in self.Frame]
            return self.OTU_Columns

        except CustomException as e:
            logging.error(f"An unexpected error occurred: {e}")
            return None

    def OTU_OverHead_Field_Constructor(self):

        self.OTU_OH = [OTN_OH.OTU_SM , OTN_OH.OTU_GCC0 , OTN_OH.OTU_OSMC , OTN_OH.OTU_RES]

        for i in self.OTU_OH:
            self.OTU_Overhead_data_mapper[i] = (
                self.Frame[i.value.row_num][i.value.column_start:i.value.column_end]
            )

    def OTU_SM_Overhead_Constructor(self):

# error hereeeeee

        self.OTU_Overhead_data_mapper[OTN_OH.OTU_SM_BIP_8] = self.OTU_Overhead_data_mapper[OTN_OH.OTU_SM][0]
        self.OTU_Overhead_data_mapper[OTN_OH.OTU_SM_TTI] = self.OTU_Overhead_data_mapper[OTN_OH.OTU_SM]

        OTU_SM_Data = self.OTU_Overhead_data_mapper[OTN_OH.OTU_SM][2]
        binary_data = bin(int(OTU_SM_Data, 16))[2:].zfill(8)

        # format(int(binary_data[5:8], 2), 'x')
        self.OTU_Overhead_data_mapper[OTN_OH.OTU_SM_BEI_BIAE] = int(binary_data[0:4], 2) % 10
        self.OTU_Overhead_data_mapper[OTN_OH.OTU_SM_BDI] = int(binary_data[4]) % 10
        self.OTU_Overhead_data_mapper[OTN_OH.OTU_SM_IAE] = int(binary_data[5], 2) % 10
        self.OTU_Overhead_data_mapper[OTN_OH.OTU_SM_STAT] = int(binary_data[6:8], 2) % 10




    def OTU_OverHead_Field_Finder(self , OTU_Field):
            return self.OTU_Overhead_data_mapper[OTU_Field]

    def Visualize_OTU(self):

        for i in self.OTU_OH:
            field_data = self.OTU_OverHead_Field_Finder(i)
            print(f"{i} field : \'{field_data}\' \n ")
            if i is OTN_OH.OTU_SM:
                print("OTU_SM details : \n ")
                print(f"SM_BEI_BIAE is {self.OTU_Overhead_data_mapper[OTN_OH.OTU_SM_BEI_BIAE]}")
                print(f"SM_BDI is {self.OTU_Overhead_data_mapper[OTN_OH.OTU_SM_BDI]}")
                print(f"SM_IAE is {self.OTU_Overhead_data_mapper[OTN_OH.OTU_SM_IAE]}")
                print(f"SM_STAT is {self.OTU_Overhead_data_mapper[OTN_OH.OTU_SM_STAT]}")
                print(f"SM_TTI is {self.OTU_Overhead_data_mapper[OTN_OH.OTU_SM_TTI]}")
                print(f"SM_BIP_8 is {self.OTU_Overhead_data_mapper[OTN_OH.OTU_SM_BIP_8]}")
                print("###########################################")