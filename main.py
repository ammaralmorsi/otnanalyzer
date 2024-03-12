
from src.backend.FrameBuilder.Parser_APIs import parser_API
from Configuration.OTN_Fields_Config import OTN_OH


filepath = "A:/Ahmed_SH/Siemens Projects/otnanalyzer/InputTests/input.txt"
test = parser_API(filepath , "OTN")

otn = test.get_otn_frame()
odu = test.get_odu_overhead()
otu = test.get_otu_overhead()
opu = test.get_opu_frame()
fa = test.get_fa_overhead()




