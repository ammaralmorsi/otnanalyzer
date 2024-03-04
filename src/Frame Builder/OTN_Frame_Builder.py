
from src.PreProcessing import Input_Processor
import ODU_Frame
import OPU_Frame
import OTU_Frame

class OTN:

    Frame_Rows = 4

    def __int__(self , filepath):

        self.PreProcessor = Input_Processor()
        self.OPU = OPU_Frame()
        self.ODU = ODU_Frame()
        self.OTU = OTU_Frame()
        self.Divided_OTN = [self.ODU, self.OPU, self.OTU]


    def Construct_OPU(self): None

    def Construct_ODU(self): None

    def Construct_OTU(self): None

    def get_OPU_overhead(self):
        return self.OPU

    def get_ODU_overhead(self):
        return self.ODU

    def get_OTU_overhead(self):
        return self.OTU










