import logging

from src.backend.FrameBuilder import OPU_Frame
from src.backend.FrameBuilder.OPU_Frame import OPU_Frame
from src.backend.FrameBuilder.OTU_Frame import OTU_Frame

from src.backend.PreProcessing.Input_Processor import InputProcessor
from Configuration.OTN_Fields_Config import OTN_OH
from Configuration.OTN_Frames_Column_Ranges import OTN_Frames
from Configuration.OTN_Field_Data import OTN_Field_Data

from Configuration.Log_Config import Logger

import os , logging

Logger.log_init()

file_path = "A:/Ahmed_SH/Siemens Projects/otnanalyzer/InputTests/input.txt"

test = InputProcessor(file_path , "OTN").get_File_in_STND_Format()

# for i in test:
#     print(i)

opu = OPU_Frame(test)

print(opu.OPU_Overhead.OPU_OverHead_Field_Finder(OTN_OH.OPU_JC1))

