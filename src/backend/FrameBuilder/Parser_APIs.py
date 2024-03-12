from src.backend.FrameBuilder.ODU_Frame import ODU_Frame
from src.backend.FrameBuilder.OPU_Frame import OPU_Frame
from src.backend.FrameBuilder.OTU_Frame import OTU_Frame
from src.backend.PreProcessing.Input_Processor import InputProcessor
from Configuration.OTN_Fields_Config import OTN_OH
from Configuration.OTN_Field_Data import OTN_Field_Data
from Configuration.Log_Config import Logger
import os , logging


"""

# The frametype arg in the init parser_API , is either "OTN" , "OPU" , "ODU" , "OTU" , look in Configuration/OTN_Frams_Column_Ranges.py

# If a field is needed as argument it should be like this OTN_OH.field 

# In get_tcm_inner_field() , tcm_num is like OTN_OH.TCM1 , and field is either 'TTI' , 'BIP_8' , 'BEI_BIAE' , 'BDI' , 'STAT'

"""

class parser_API:

    def __init__(self, filepath, frametype):
        Logger.log_init()
        self.preprocessed_file = InputProcessor(filepath, frametype).get_File_in_STND_Format()

        if frametype == 'OTN' or frametype == 'OPU':
            self.opu = OPU_Frame(self.preprocessed_file)
        if(frametype == 'OTN' or frametype == 'ODU'):
            self.odu = ODU_Frame(self.preprocessed_file)
        if(frametype == 'OTN' or frametype == 'OPU'):
            self.otu = OTU_Frame(self.preprocessed_file)

    def get_otn_data_visualization(self):
        try:
            self.get_opu_data_visualization()
            self.get_odu_data_visualization()
            self.get_otu_data_visualization()
            self.get_fa_data_visualization()
        except (AttributeError,TypeError,KeyError) as e:
            print("# The frame doesnot have all overheads , it is possibly not an otn frame type")

    """
        Below are the APIs for the opu frame part
    """

    def get_opu_payload(self):
        try:
            return self.opu.OPU_Payload_Constructor()
        except (AttributeError, KeyError) as e:
            print(f"Error : {e}")
        return ""
    def get_opu_overhead(self):
        try:
            return self.opu.OPU_OverHead_Columns_Data()
        except (AttributeError, KeyError) as e:
            print(f"Error : {e}")
    def get_opu_field(self, opu_field):
        try:
            return self.opu.OPU_OverHead_Field_Finder(opu_field)
        except AttributeError as e:
            print(f"# Error : {e}")
        return ""


    def get_opu_data_visualization(self):
        try:
            return self.opu.visualize_OPU()
        except AttributeError as e:
            print("# The frame doesnot contain OPU , so cannot visualize opu data")
        return ""

    ##########################################################

    """
        Below are the APIs for the odu frame part
    """

    def get_odu_overhead(self):
        return self.odu.ODU_OverHead_Column_Data()
    def get_odu_field(self, odu_field):
        try:
            return self.odu.ODU_OverHead_Field_Finder(odu_field)
        except (AttributeError, KeyError) as e:
            print(f"Error : {e}")
    def get_tcm_inner_field(self, tcm_num, field):
        try:
            return tcm_num.value.inner_levels[field]
        except AttributeError:
            print("# TCM num doesnot exist")
        except KeyError as e:
            print("# This tcm_num does not have this field")
        return ""

    def get_tcm_details(self , tcm_num):
        try:
            # print(f"{tcm_num} details are : \n")
            for i in tcm_num.value.inner_levels:
                print(f"\t{i} field data is : {tcm_num.value.inner_levels[i]}")
        except (AttributeError,KeyError) as e:
            print(f"{e}")
        return ""

    def get_odu_data_visualization(self):
        self.odu.visualize_odu()
        return ""
    ############################################################

    """
        Below are the APIs for the otu frame part
    """

    def get_otu_overhead(self):
        return self.otu.OTU_OverHead_Column_Data()
    def get_otu_field(self , otu_field):
        try:
            return self.otu.OTU_OverHead_Field_Finder(otu_field)
        except (AttributeError,KeyError) as e:
            print(f"Error : {e}")
    def get_otu_data_visualization(self):
        return self.otu.Visualize_OTU()
        return ""
    ############################################################

    """
        Below are the APIs for the fa frame part
    """

    def get_fa_overhead(self):
        return self.otu.FA_overhead_column_data()
        return ""
    def get_fa_field(self , fa_field):
        return self.otu.FA_OverHead_Field_Finder(fa_field)
        return ""
    def get_fa_data_visualization(self):
        return self.otu.visualize_fa()
        return ""
