
from parser.frame.opu import Opu
from parser.frame.otu import Otu
from parser.frame.odu import Odu


class Parser_API:

    def __init__(self, formatted_frame):
        self.formatted_frame = formatted_frame
        self.Opu = Opu(self.formatted_frame)
        self.Odu = Odu(self.formatted_frame)
        self.Otu = Otu(self.formatted_frame)

    """
        Below are the APIs for the opu frame part
    """

    def get_opu_payload(self):
        return self.Opu.payload_data

    def get_opu_overhead(self):
        return self.Opu.overhead_data

    def get_opu_field(self, opu_field):
        return self.Opu.overhead_field_finder(opu_field)

    ##########################################################

    """
        Below are the APIs for the odu frame part
    """

    def get_odu_overhead(self):
        return self.Odu.overhead_data

    def get_odu_field(self, odu_field):
        return self.Odu.overhead_field_finder(odu_field)

    def get_odu_inner_field(self, odu_parent_field):
        return self.Odu.inner_overhead_field_data(odu_parent_field)


    ############################################################

    """
        Below are the APIs for the otu , fa frame part  , 
        assume fa and otu overheads in one frame for now
    """

    def get_otu_overhead(self):
        return self.Otu.overhead_data

    def get_otu_field(self, otu_field):
        return self.Otu.overhead_field_finder(otu_field)

    def get_otu_inner_field(self , otu_parent_field):
        return self.Otu.inner_overhead_field_data(otu_parent_field)


