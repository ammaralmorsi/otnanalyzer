from src.FrameBuilder import OPU_Frame
from src.FrameBuilder.OPU_Frame import OPUFrame
from src.PreProcessing.Input_Processor import InputProcessor

file_path = "A:/Ahmed_SH/Siemens Projects/otnanalyzer/Input Tests/input.txt"

test = InputProcessor(file_path)

opu = OPUFrame(test.File_in_OTN)

x = opu.OPU_OverHead_Constructor(test.File_in_OTN)


for rows in x:
    print(rows)




