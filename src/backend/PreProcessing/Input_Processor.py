


class InputProcessor:

    def __init__(self , filepath):

        self.Original_File = self.Frames_File_Reader(filepath)
        self.File_in_HEX =   self.Convert_To_HEX(self.Original_File)
        self.File_in_OTN =   self.Convert_To_OTN_Frame_Format(self.File_in_HEX)


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


    def Convert_To_OTN_Frame_Format(self , HEX_OTN_Frame , Type):

            values = HEX_OTN_Frame.split()

            rows = [values[i:i + 3824] for i in range(0, len(values), 3824)]

            return rows



