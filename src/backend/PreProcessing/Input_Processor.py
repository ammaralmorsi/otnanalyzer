import logging

from Configuration.OTN_Frames_Column_Ranges import OTN_Frames
from Exceptions.Custom_Exception import CustomException

class InputProcessor:

    def __init__(self , filepath , Frame_Type):

        self.Original_File = self.Frames_File_Reader(filepath)
        self.File_in_HEX =   self.Convert_To_HEX(self.Original_File)
        self.File_in_STND_Format =   self.Convert_To_OTN_Frame_Format(self.File_in_HEX , Frame_Type)



    def get_File_in_STND_Format(self):
        return self.File_in_STND_Format

    def Frames_File_Reader(self , file_path):

            try:
                with open(file_path, 'r') as file:
                    OTN_Frames = file.read()
                    print("File read successfully")
                    return OTN_Frames
            except FileNotFoundError:
                print(f"File '{file_path}' not found.")
                return None


    def Convert_To_HEX(self, OTN_Frame_Row):


            decimal_values = OTN_Frame_Row.split()

            # Convert each decimal value to hexadecimal
            hex_values = [hex(int(value))[2:].zfill(2) for value in decimal_values]

            hex_in_original_form = ' '.join(hex_values)

            return hex_in_original_form


    def Convert_To_OTN_Frame_Format(self , HEX_OTN_Frame , FrameType):


        frame_size = OTN_Frames.FRAME_SIZES.get(FrameType)

        if frame_size is not None:
            values = HEX_OTN_Frame.split()
            rows = [values[i:i + frame_size] for i in range(0, len(values), frame_size)]
            return rows

        else:
            logging.error("FrameType key not found")



