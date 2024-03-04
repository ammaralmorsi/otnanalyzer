from src.backend.FrameBuilder import OPU_Frame
from src.backend.FrameBuilder.OPU_Frame import OPUFrame
from src.backend.PreProcessing.Input_Processor import InputProcessor

file_path = "A:/Ahmed_SH/Siemens Projects/otnanalyzer/InputTests/input.txt"

test = InputProcessor(file_path)

opu = OPUFrame(test.File_in_OTN)

x = opu.OPU_OverHead_Constructor(test.File_in_OTN)


# for row in test.File_in_OTN:
#     print(row)


for rows in x:
    print(rows)

# for rows in x:
#     print(rows[0] + " " + rows[1])




