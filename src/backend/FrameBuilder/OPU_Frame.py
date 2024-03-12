
from Configuration.OTN_Fields_Config import OTN_OH
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

        try:
            self.OPU_OverHead_Fields_Constrcutor()
        except (TypeError , KeyError) as e:
            print(f"# Error in opu : {e}")
            logging.error(e)

    def OPU_All_Frame_Constructror(self):

        self.OPU_Columns = [row[14:3824] for row in self.Frame]
        return self.OPU_Columns


    def OPU_Payload_Constructor(self):
        try:
            self.OPU_Payload_Columns = [row[16:3824] for row in self.Frame]
            return self.OPU_Payload_Columns
        except IndexError as e:
            logging.error(f"The frame isnot OPU , {e}")
            print("The frame isnot opu, so this API not available")


    def OPU_OverHead_Columns_Data(self):

        try:
            self.OPU_Overhead_Columns = [row[14:16] for row in self.Frame]
            self.OPU_Overhead_Columns[3].append(self.Frame[3][16])
            return self.OPU_Overhead_Columns
        except IndexError as e:
            logging.error(f"The frame isnot OPU , {e}")
            print("The frame isnot opu, so this API not available")



    def OPU_OverHead_Fields_Constrcutor(self):

        for i in self.OPU_OH:

            self.OPU_Overhead_data_mapper[i] = (
                self.Frame[i.value.row_num][i.value.column_start]
            )

        return self.OPU_Overhead_data_mapper


    def OPU_OverHead_Field_Finder(self , OPU_Field):
        try:
            return self.OPU_Overhead_data_mapper[OPU_Field]
        except (KeyError , AttributeError) as e:
            logging.error(f"OPU Field key not found , + {e}")
            print(f"opu field not found , + {e}")

    def visualize_OPU(self):
        try:

            print("\nThe opu overheads are : ")
            print("-----------------------------------")
            for i in self.OPU_OH:
                field_data = self.OPU_OverHead_Field_Finder(i)
                print(f"{i} field : {field_data} \n ")
            print("-----------------------------------")
            return ""
        except IndexError as e:
            logging.error(f"The frame isnot OPU , {e}")
            print("The frame isnot opu, so this API not available")
