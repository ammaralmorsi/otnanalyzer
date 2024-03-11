
from src.backend.FrameBuilder.Parser_APIs import parser_API



filepath = "A:/Ahmed_SH/Siemens Projects/otnanalyzer/InputTests/input.txt"
test = parser_API(filepath , "OTN")

print(test.get_opu_overhead())
print("####")
print(test.get_opu_field("JC1"))








