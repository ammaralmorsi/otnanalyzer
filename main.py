from src.backend.FrameBuilder import OPU_Frame
from src.backend.FrameBuilder.OPU_Frame import OPUFrame , OPU_Overheads
from src.backend.PreProcessing.Input_Processor import InputProcessor

file_path = "A:/Ahmed_SH/Siemens Projects/otnanalyzer/InputTests/input.txt"

test = InputProcessor(file_path)

opu = OPUFrame(test.File_in_OTN)

opu.OPU_Overhead.OPU_OverHead_Fields_Constrcutor()

print(opu.OPU_Overhead.OPU_OverHead_Field_Finder(OPU_Overheads.JC1))


# x = opu.OPU_Payload_Constructor(test.File_in_OTN)
#
#
# for row in test.File_in_OTN:
#     print(row)
#
# print("##################################################################################")
#
# for rows in x:
#     print(rows)

# for rows in x:
#     print(rows[0] + " " + rows[1])




