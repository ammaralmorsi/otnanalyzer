
from src.backend.FrameBuilder.Parser_APIs import parser_API
from Configuration.OTN_Fields_Config import OTN_OH


filepath = "C:/Users/ashar/OneDrive/Desktop/testinggg/otnanalyzer/InputTests/input.txt"

test = parser_API(filepath, "OTN")

print(test.get_odu_overhead())






