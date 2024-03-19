from config.overhead.opu import OpuOverheads
from tabulate import tabulate

class Opu:

    def __init__(self, formatted_frame):
        self.formatted_frame = formatted_frame
        self.overhead_data = {}
        self.overhead_constructor()

    def overhead_constructor(self):
        for overhead in OpuOverheads:
            oh_value = overhead.value
            self.overhead_data[overhead.value.name] = (
                self.formatted_frame[oh_value.position.row]
                [oh_value.position.col:oh_value.position.col + oh_value.dimension.ncols]
            )

    def payload_data(self):
        return [row[16:3824] for row in self.formatted_frame]

    def overhead_data(self):
        return self.overhead_data

    def overhead_field_finder(self, opu_oh):
        return self.overhead_data[opu_oh.name]

    def __str__(self):
        header_itr = 0
        column_header = [
            ["JC4", "JC1"], ["JC5", "JC2"], ["JC6", "JC3"], ["PSI", "NJO" , "PJO"]
        ]
        row_data_frame = []
        for opu_oh in OpuOverheads:
            if opu_oh.name == "jc5" or opu_oh.name == "jc6" or opu_oh.name == "psi":
                first_row_transposed_data = list(zip(*row_data_frame))
                print(tabulate(first_row_transposed_data, headers=column_header[header_itr], tablefmt="grid",
                               stralign="center", numalign="center"))
                row_data_frame = []
                header_itr += 1
            combined_value = ' '.join(self.overhead_field_finder(opu_oh))
            row_data_frame.append([combined_value])
        first_row_transposed_data = list(zip(*row_data_frame))
        print(tabulate(first_row_transposed_data, headers=column_header[3], tablefmt="grid",
                       stralign="center", numalign="center"))
        return ""

