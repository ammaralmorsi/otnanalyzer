
from Configuration.OTN_Fields_Config import OTN_OH
from Exceptions.Exceptions import CustomException

class OPUFrame:


    def __init__(self , Frame):

        self.Frame = Frame
        self.OPU_Columns = None

        self.OPU_Payload_Columns = None
        self.OPU_Payload_Partial_Column = None
        self.OPU_Overhead_Columns = None

        self.OPU_Payload = self.OPU_Payload_Constructor(self.Frame)
        self.OPU_Overhead = OPU_Overhead(self.Frame)


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

    def __init__(self , Frame):
        self.Frame = Frame
        # self.OPU_OH_First_Column = 0
        # self.OPU_OH_Second_Column = 1
        self.OPU_Overhead_Finder = {}

    def OPU_OverHead_Fields_Constrcutor(self):

        self.OPU_Overhead_Finder[OTN_OH.OPU_JC1] = (
            self.Frame[OTN_OH.OPU_JC1.value.row_num][OTN_OH.OPU_JC1.value.column_start]
        )

        self.OPU_Overhead_Finder[OTN_OH.OPU_JC2] = (
            self.Frame[OTN_OH.OPU_JC2.value.row_num][OTN_OH.OPU_JC2.value.column_start]
        )

        self.OPU_Overhead_Finder[OTN_OH.OPU_JC3] = (
            self.Frame[OTN_OH.OPU_JC3.value.row_num][OTN_OH.OPU_JC3.value.column_start]
        )

        self.OPU_Overhead_Finder[OTN_OH.OPU_JC4] = (
            self.Frame[OTN_OH.OPU_JC4.value.row_num][OTN_OH.OPU_JC4.value.column_start]
        )

        self.OPU_Overhead_Finder[OTN_OH.OPU_JC5] = (
            self.Frame[OTN_OH.OPU_JC5.value.row_num][OTN_OH.OPU_JC5.value.column_start]
        )

        self.OPU_Overhead_Finder[OTN_OH.OPU_JC6] = (
            self.Frame[OTN_OH.OPU_JC6.value.row_num][OTN_OH.OPU_JC6.value.column_start]
        )

        self.OPU_Overhead_Finder[OTN_OH.OPU_PSI] = (
            self.Frame[OTN_OH.OPU_PSI.value.row_num][OTN_OH.OPU_PSI.value.column_start]
        )

        self.OPU_Overhead_Finder[OTN_OH.OPU_NJO_OMFI] = (
            self.Frame[OTN_OH.OPU_NJO_OMFI.value.row_num][OTN_OH.OPU_NJO_OMFI.value.column_start]
        )

        self.OPU_Overhead_Finder[OTN_OH.OPU_PJO] = (
            self.Frame[OTN_OH.OPU_PJO.value.row_num][OTN_OH.OPU_PJO.value.column_start]
        )
        return self.OPU_Overhead_Finder


    def OPU_OverHead_Field_Finder(self , OPU_Field):
        try:
            return self.OPU_Overhead_Finder[OPU_Field]
        except CustomException as e:
            print("key not found")

