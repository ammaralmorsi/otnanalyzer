
from parser.frame.opu import Opu
from parser.frame.otu import Otu


"""

# The frametype arg in the init parser_API , is either "OTN" , "OPU" , "ODU" , "OTU" , look in Configuration/OTN_Frams_Column_Ranges.py

# If a field is needed as argument it should be like this OTN_OH.field 

# In get_tcm_inner_field() , tcm_num is like OTN_OH.TCM1 , and field is either 'TTI' , 'BIP_8' , 'BEI_BIAE' , 'BDI' , 'STAT'

"""


class Parser_API:


    def __init__(self, formatted_frame):
        self.formatted_frame = formatted_frame
        self.Opu = Opu(self.formatted_frame)
        self.Otu = Otu(self.formatted_frame)
    """
        Below are the APIs for the opu frame part
    """

    def get_opu_overhead(self):
        return self.Opu.opu_overhead_data()

    def get_opu_field(self, opu_field):
        return self.Opu.opu_overhead_field_finder(opu_field)

    def visualize_opu(self):
        pass

    ##########################################################

    """
        Below are the APIs for the odu frame part
    """

    def get_odu_overhead(self):
        return self.odu.ODU_OverHead_Column_Data()

    def get_odu_field(self, odu_field):
        return self.odu.ODU_OverHead_Field_Finder(odu_field)

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
        Below are the APIs for the otu , fa frame part  , assume fa and otu overheads in one frame for now
    """

    def get_otu_overhead(self):
        return self.Otu.otu_overhead_data()

    def get_otu_field(self , otu_field):
        return self.Otu.otu_overhead_field_finder(otu_field)

    def visualize_otu(self):
        pass


