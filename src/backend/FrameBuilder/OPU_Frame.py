
from Configuration.OTN_Fields_Config import OPU_OH


class OPUFrame:


    def __init__(self , Frame):

        self.Frame = Frame
        self.OPU_Columns = None

        self.OPU_Payload_Columns = None
        self.OPU_Payload_Partial_Column = None
        self.OPU_Overhead_Columns = None

        self.OPU_Payload = self.OPU_Payload_Constructor(self.Frame)
        self.OPU_Overhead_Extracted_Data = self.OPU_OverHead_Constructor(self.Frame)
        self.OPU_Overhead = OPU_Overhead(self.OPU_Overhead_Extracted_Data)


    def OPU_All_Frame_Constructror(self , Frame):

        self.OPU_Columns = [row[14:3824] for row in Frame]
        return self.OPU_Columns


    def OPU_Payload_Constructor(self , Frame):

        self.OPU_Payload_Columns = [row[16:3824] for row in Frame]
        return self.OPU_Payload_Columns

    def OPU_OverHead_Constructor(self , Frame):

        self.OPU_Overhead_Columns = [row[14:16] for row in Frame]
        self.OPU_Overhead_Columns[3].append(Frame[3][16])
        return self.OPU_Overhead_Columns


class OPU_Overhead:

    def __init__(self , OPU_OH_Frame):

        self.OPU_OverHead_Frame = OPU_OH_Frame
        self.OPU_OH_First_Column = 0
        self.OPU_OH_Second_Column = 1
        self.OPU_Overhead_Finder = {}

    def OPU_OverHead_Fields_Constrcutor(self):

        self.OPU_Overhead_Finder[OPU_OH.JC1] = self.OPU_OverHead_Frame[0][self.OPU_OH_Second_Column]
        self.OPU_Overhead_Finder[OPU_OH.JC2] = self.OPU_OverHead_Frame[1][self.OPU_OH_Second_Column]
        self.OPU_Overhead_Finder[OPU_OH.JC3] = self.OPU_OverHead_Frame[2][self.OPU_OH_Second_Column]
        self.OPU_Overhead_Finder[OPU_OH.JC4] = self.OPU_OverHead_Frame[0][self.OPU_OH_First_Column]
        self.OPU_Overhead_Finder[OPU_OH.JC5] = self.OPU_OverHead_Frame[1][self.OPU_OH_First_Column]
        self.OPU_Overhead_Finder[OPU_OH.JC6] = self.OPU_OverHead_Frame[2][self.OPU_OH_First_Column]
        self.OPU_Overhead_Finder[OPU_OH.PSI] = self.OPU_OverHead_Frame[3][self.OPU_OH_First_Column]
        self.OPU_Overhead_Finder[OPU_OH.NJO] = self.OPU_OverHead_Frame[3][self.OPU_OH_Second_Column]
        self.OPU_Overhead_Finder[OPU_OH.PJO] = self.OPU_OverHead_Frame[3][2]

        return self.OPU_Overhead_Finder


    def OPU_OverHead_Field_Finder(self , OPU_Field):
        return self.OPU_Overhead_Finder[OPU_Field]


