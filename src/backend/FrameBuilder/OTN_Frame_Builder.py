
from src.backend.PreProcessing import Input_Processor
from src.backend.FrameBuilder.OPU_Frame import OPU_Frame
from src.backend.FrameBuilder.OTU_Frame import OTU_Frame
from src.backend.FrameBuilder.ODU_Frame import ODU_Frame



class OTN:

    Frame_Rows = 4

    def __init__(self , filepath):

        self.PreProcessor = Input_Processor()
        self.OPU = OPU_Frame()
        self.ODU = ODU_Frame()
        self.OTU = OTU_Frame()
        self.Divided_OTN = [self.ODU, self.OPU, self.OTU]

        self.Frame_Fields = {}


    def Fields_Constructor(self):

        self.Frame_Fields['OPU'] = self.OPU.OPU_Overhead.OPU_OverHead_Fields_Constrcutor()

        # same for ODU
        self.Frame_Fields['ODU'] = None

        # same for OTU
        self.Frame_Fields['OTU'] = None


    def Construct_OPU(self): None

    def Construct_ODU(self): None

    def Construct_OTU(self): None

    def get_OPU_overhead(self):
        return self.OPU

    def get_ODU_overhead(self):
        return self.ODU

    def get_OTU_overhead(self):
        return self.OTU

    def get_specific_field(self , field) : None











