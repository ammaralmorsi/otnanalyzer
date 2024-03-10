import logging

from src.backend.FrameBuilder import OPU_Frame
from src.backend.FrameBuilder.OPU_Frame import OPU_Frame
from src.backend.FrameBuilder.OTU_Frame import OTU_Frame
from src.backend.FrameBuilder.ODU_Frame import ODU_Frame
from src.backend.PreProcessing.Input_Processor import InputProcessor
from Configuration.OTN_Fields_Config import OTN_OH
from Configuration.OTN_Frames_Column_Ranges import OTN_Frames
from Configuration.OTN_Field_Data import OTN_Field_Data
from src.backend.Comparator.Frame_Comparator import OTU_Comparator , OPU_Comparator
from Configuration.Log_Config import Logger

import os , logging

Logger.log_init()

file_path = "A:/Ahmed_SH/Siemens Projects/otnanalyzer/InputTests/input.txt"
file_path2 = "A:/Ahmed_SH/Siemens Projects/otnanalyzer/InputTests/inputt.txt"


test = InputProcessor(file_path , "OTN").get_File_in_STND_Format()

testa = InputProcessor(file_path2 , "OTN").get_File_in_STND_Format()


odu = OPU_Frame(test)


odu2 = OPU_Frame(testa)

print(odu.OPU_OverHead_Columns_Data())
print(odu2.OPU_OverHead_Columns_Data())


d = OPU_Comparator(odu , odu2)