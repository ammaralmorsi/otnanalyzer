from Configuration.OTN_Fields_Config import OTN_OH
from Exceptions.Custom_Exception import CustomException
import logging

class OTU_Frame:

    def __init__(self , Frame):
        self.Frame = Frame
        self.OTU_Columns = None
        self.OTU_Overhead_data_mapper = {}
        self.OTU_OverHead_Field_Constructor()

    def OTU_OverHead_Column_Data(self):

        try:
            self.OTU_Columns = [row[7:14] for row in self.Frame]
            return self.OTU_Columns

        except CustomException as e:
            logging.error(f"An unexpected error occurred: {e}")
            return None

    def OTU_OverHead_Field_Constructor(self):

        self.OTU_Overhead_data_mapper[OTN_OH.OTU_SM] = (
            self.Frame[OTN_OH.OTU_SM.value.row_num][OTN_OH.OTU_SM.value.column_start:OTN_OH.OTU_SM.value.column_end]
        )

        self.OTU_Overhead_data_mapper[OTN_OH.OTU_GCC0] = (
            self.Frame[OTN_OH.OTU_GCC0.value.row_num][OTN_OH.OTU_GCC0.value.column_start:OTN_OH.OTU_GCC0.value.column_end]
        )

        self.OTU_Overhead_data_mapper[OTN_OH.OTU_OSMC] = (
            self.Frame[OTN_OH.OTU_OSMC.value.row_num][OTN_OH.OTU_OSMC.value.column_start:OTN_OH.OTU_OSMC.value.column_end]
        )

        self.OTU_Overhead_data_mapper[OTN_OH.OTU_RES] = (
            self.Frame[OTN_OH.OTU_RES.value.row_num][OTN_OH.OTU_RES.value.column_start:OTN_OH.OTU_RES.value.column_end]
        )


    def OTU_OverHead_Field_Finder(self , OTU_Field):
        return self.OTU_Overhead_data_mapper[OTU_Field]