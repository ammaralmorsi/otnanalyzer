
from utils.OTN_Fields_Config import OTN_OH
from Exceptions.Custom_Exception import CustomException
import logging

class OPU_Frame:

    def __init__(self , Frame):

        self.Frame = Frame
        self.OPU_Columns = None

        self.OPU_Payload_Columns = None
        self.OPU_Overhead_Columns = None

        self.OPU_Payload = self.OPU_Payload_Constructor()
        self.OPU_Overhead_data_mapper = {}
        self.OPU_OH = [
            OTN_OH.OPU_JC1, OTN_OH.OPU_JC2, OTN_OH.OPU_JC3, OTN_OH.OPU_JC4,
            OTN_OH.OPU_JC5, OTN_OH.OPU_JC6, OTN_OH.OPU_PSI, OTN_OH.OPU_NJO_OMFI,
            OTN_OH.OPU_PJO
        ]
        self.OPU_OverHead_Fields_Constrcutor()

    def OPU_All_Frame_Constructror(self):

        self.OPU_Columns = [row[14:3824] for row in self.Frame]
        return self.OPU_Columns


    def OPU_Payload_Constructor(self):

        self.OPU_Payload_Columns = [row[16:3824] for row in self.Frame]
        return self.OPU_Payload_Columns

    def OPU_OverHead_Columns_Data(self):

        self.OPU_Overhead_Columns = [row[14:16] for row in self.Frame]
        self.OPU_Overhead_Columns[3].append(self.Frame[3][16])
        return self.OPU_Overhead_Columns


    def OPU_OverHead_Fields_Constrcutor(self):

        for i in self.OPU_OH:

            self.OPU_Overhead_data_mapper[i] = (
                self.Frame[i.value.row_num][i.value.column_start]
            )

        return self.OPU_Overhead_data_mapper


    def OPU_OverHead_Field_Finder(self , OPU_Field):
        try:
            return self.OPU_Overhead_data_mapper[OPU_Field]
        except CustomException as e:
            logging.error("OPU Field key not found")


    def visualize_OPU(self):
        for i in self.OPU_OH:
            field_data = self.OPU_OverHead_Field_Finder(i)
            print(f"{i} field : \'{field_data}\' \n ")
