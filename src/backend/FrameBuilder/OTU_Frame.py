from Configuration.OTN_Fields_Config import OTN_OH
from Exceptions.Custom_Exception import CustomException
import logging

class OTU_Frame:

    def __init__(self , Frame):
        self.Frame = Frame
        self.OTU_Columns = None
        self.OTU_Overhead_Finder = {}
        self.OTU_OH_Row = 0

    def OTU_OverHead_Constructor(self):

        try:
            self.OTU_Columns = [row[7:14] for row in self.Frame]
            return self.OTU_Columns

        except CustomException as e:
            logging.error(f"An unexpected error occurred: {e}")
            return None

    def OTU_OverHead_Field_Constructor(self):

        self.OTU_Overhead_Finder[OTU_OH.SM] = self.Frame[self.OTU_OH_Row][7:10]
        self.OTU_Overhead_Finder[OTU_OH.OTU_GCC0] = self.Frame[self.OTU_OH_Row][10:12]
        self.OTU_Overhead_Finder[OTU_OH.OTU_OSMC] = self.Frame[self.OTU_OH_Row][13]
        self.OTU_Overhead_Finder[OTU_OH.OTU_RES] = self.Frame[self.OTU_OH_Row][14]


    def OTU_OverHead_Field_Finder(self , OTU_Field):
        return self.OTU_Overhead_Finder[OTU_Field]