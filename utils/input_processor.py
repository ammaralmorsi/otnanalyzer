

class InputProcessor:

    def __init__(self, filepath):
        self.file_path = filepath
        self.frames = self.frames_file_reader()
        self.formatted_frames = self.get_all_formatted_frames(self.frames)

    def frames_file_reader(self):

        try:
            frames_list = []
            with open(self.file_path, 'r') as file:
                for frame in file:
                    frames_list.append(frame.strip())
            return frames_list
        except FileNotFoundError:
            print(f"File '{self.file_path}' not found.")
            return None

    def convert_data_to_hex(self, otn_frame_row):

        """
            Convert decimal numbers in a single-line frame to hexadecimal.

            Args:
                OTN_Frame_Row (str): A single-line frame represented as decimal numbers separated by spaces.

            Returns:
                str: The frame with decimal numbers converted to hexadecimal, separated by spaces.

        """

        decimal_values = otn_frame_row.split()
        hex_values = [hex(int(value))[2:].zfill(2) for value in decimal_values]
        single_line_hex = ' '.join(hex_values)
        return single_line_hex


    def format_to_otn_frame(self , HEX_OTN_Frame):

        values = HEX_OTN_Frame.split()
        rows = [values[i:i + 3824] for i in range(0, len(values), 3824)]    # '3824' hardcoded , resolve after merging branches
        return rows

    def get_all_formatted_frames(self , frames_list):
        """
            Format each line in the file in the needed format which is the data to be in hex ,
            and every frame to be a list of lists [][]

            Args:
                frames_list (list) : A list of single frames

            Returns:
                 list of 2d otn frames , each 2d otn frame represent a single line in the input
        """
        formatted_frames = []
        for single_frame in frames_list:
            frame_in_hex = self.convert_data_to_hex(single_frame)
            frame_format = self.format_to_otn_frame(frame_in_hex)
            formatted_frames.append(frame_format)
        return formatted_frames






