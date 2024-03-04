



class InputProcessor:

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

            # Split the decimal row into individual decimal values
            decimal_values = OTN_Frame_Row.split()

            # Convert each decimal value to hexadecimal
            hex_values = [hex(int(value))[2:].zfill(2) for value in decimal_values]

            return hex_values


    def Convert_To_OTN_Frame_Format(self , HEX_OTN_Frame):


            values = HEX_OTN_Frame.split()

            # Divide the values into 4 rows, each with 3824 values
            rows = [values[i:i + 3824] for i in range(0, len(values), 3824)]


            # this is just to ensure , you can comment this part
            for i, row in enumerate(rows):
                print(f"Length of row {i + 1}: {len(row)}")

            return rows


# test  = InputProcessor()
#
# path = "A:/Ahmed_SH/Siemens Projects/otnanalyzer/Input Tests/input.txt"
#
# obj = test.Frames_File_Reader(path)
#
# rows = test.Convert_To_OTN_Frame(obj)
#
#
# for row in rows:
#     print(len(row))
#     print(row)


