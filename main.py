from src.backend.FrameBuilder import OPU_Frame
from src.backend.FrameBuilder.OPU_Frame import OPUFrame
from src.backend.PreProcessing.Input_Processor import InputProcessor
from Configuration.OTN_Fields_Config import OPU_OH , ODU_OH , OTU_OH
from src.backend.FrameBuilder.OTU_Frame import OTUFrame


# *_OH is realting to the Enum objects in OTN_Fileds_Config.py


file_path = "A:/Ahmed_SH/Siemens Projects/otnanalyzer/InputTests/input.txt"

test = InputProcessor(file_path)

# for row in test.File_in_STND_Format:
#     print(row)

opu = OPUFrame(test.File_in_STND_Format)
x = opu.OPU_OverHead_Constructor(test.File_in_STND_Format)
print(x)

# otu = OTUFrame(test.File_in_OTN)
#
# # all_otu = otu.OTU_OverHead_Constructor()
# #
# # print(all_otu)
#
# otu.OTU_OverHead_Field_Constructor()
# print(otu.OTU_OverHead_Field_Finder(OTU_OH.SM))

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




