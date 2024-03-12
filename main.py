
from src.backend.FrameBuilder.Parser_APIs import parser_API
from utils.OTN_Fields_Config import OTN_OH


filepath = "A:/Ahmed_SH/Siemens Projects/otnanalyzer/InputTests/input.txt"
test = parser_API(filepath , "OTN")

# #test.get_otn_data_visualization()
# # test.get_opu_data_visualization()
# test.get_odu_data_visualization()
# # test.get_otu_data_visualization()
# # test.get_fa_data_visualization()


print(test.get_tcm_details(OTN_OH.ODU_TCM6))
