

class OPUFrame:


    def __init__(self , OTN_Frame):

        self.OTN_Frame = OTN_Frame

        self.OPU_Columns = None
        self.OPU_Payload_Columns = None
        self.OPU_Payload_Partial_Column = None
        self.OPU_Overhead_Columns = None

        self.OPU_Payload = self.OPU_Payload_Constructor(self.OTN_Frame)
        self.OPU_Overhead_Extracted_Data = self.OPU_OverHead_Constructor(self.OTN_Frame)
        self.OPU_Overhead = OPU_Overhead(self.OPU_Overhead_Extracted_Data)

    def OPU_Frame_Constructror(self , OTN_Frame):
        self.OPU_Columns = [row[14:3824] for row in OTN_Frame]
        return self.OPU_Columns



    def OPU_Payload_Constructor(self , OTN_Frame):

        self.OPU_Payload_Columns = [row[17:3824] for row in OTN_Frame]
        self.OPU_Payload_Partial_Column = [row[17] for row in OTN_Frame[:3]]
        for i, value in enumerate(self.OPU_Payload_Partial_Column):
            self.OPU_Payload_Columns[i].insert(0, value)

        return self.OPU_Payload_Columns

    def OPU_OverHead_Constructor(self , OTN_Frame):

        self.OPU_Overhead_Columns = [row[14:16] for row in OTN_Frame]
        return self.OPU_Overhead_Columns


class OPU_Overhead:

    def __init__(self , OPU_OH_Frame):

        self.OPU_OH_Frame = OPU_OH_Frame
        self.OPU_OH_First_Column = 0
        self.OPU_OH_Second_Column = 1
        self.OPU_Overhead_Finder = {}

    def print(self):
        print(self.OPU_OH_Frame)

    def JC_Constrcutor(self):

        # constructing the JC 1-6

        self.OPU_Overhead_Finder['JC1'] = self.OPU_OH_Frame[0][1]
        self.OPU_Overhead_Finder['JC2'] = self.OPU_OH_Frame[1][1]
        self.OPU_Overhead_Finder['JC3'] = self.OPU_OH_Frame[2][1]
        self.OPU_Overhead_Finder['JC4'] = self.OPU_OH_Frame[0][0]
        self.OPU_Overhead_Finder['JC5'] = self.OPU_OH_Frame[1][0]
        self.OPU_Overhead_Finder['JC6'] = self.OPU_OH_Frame[2][0]

    def OPU_Row_4_OH_Constructor(self):
        self.OPU_Overhead_Finder['PSI'] = self.OPU_OH_Frame[3][0]
        self.OPU_Overhead_Finder['NJO'] = self.OPU_OH_Frame[3][1]

    def OPU_OverHead_Field_Finder(self , OPU_Field):
        return self.OPU_Overhead_Finder(OPU_Field)

