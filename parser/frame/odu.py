from config.overhead.odu import OduOverheads
from tabulate import tabulate

class Odu:

    def __init__(self, formatted_frame):

        self.formatted_frame = formatted_frame
        self.overhead_data = {}
        self.overhead_constructor()

    def overhead_constructor(self):

        for overhead in OduOverheads:
            oh_value = overhead.value
            self.overhead_data[oh_value.name] = (
                self.formatted_frame[oh_value.position.row]
                [oh_value.position.col:oh_value.position.col + oh_value.dimension.ncols]
            )

            if len(oh_value.inner_fields) > 0:
                self.construct_inner_field(oh_value)

    def construct_inner_field(self , parent_overhead_field):
        """
            Below we are converting the parameter (parent field value) into binary to assign the data
            of the inner fields of parent field (which is the parameter in this func) ,
            as each inner field position is relative to its parent field, not the whole frame
        Args:
            Odu overhead field : that has a specific internal structure that are divided into inner fields
        """

        inner_field_value = self.overhead_data[parent_overhead_field.name]
        inner_binary_list = [bin(int(hex_str, 16))[2:].zfill(8) for hex_str in inner_field_value]
        inner_field_binary_value = ''.join(inner_binary_list)

        for inner_index in range(len(parent_overhead_field.inner_fields)):
            inner_name = parent_overhead_field.inner_fields[inner_index]
            inner_index_binary_value = inner_field_binary_value[inner_name.position.col:inner_name.position.col + inner_name.dimension.ncols]
            parent_overhead_field.inner_fields[inner_index] = (
                hex(int(inner_index_binary_value, 2))[2:]
            )

    def overhead_data(self):
        return self.overhead_data

    def overhead_field_finder(self, odu_oh):
        return self.overhead_data[odu_oh.name]

    def inner_overhead_field_data(self, odu_oh):
        if len(odu_oh.value.inner_fields) > 0:
            return odu_oh.value.inner_fields
        else:
            return ""

    def __str__(self):
        all_headers = []
        sublist_lengths = [7, 5, 4]

        for odu_oh_col in OduOverheads:
            all_headers.append(odu_oh_col.value.name)

        column_headers = []
        start_index = 0
        for length in sublist_lengths:
            end_index = start_index + length
            column_headers.append(all_headers[start_index:end_index])
            start_index = end_index
        start_index = 0

        row_data_frame = []
        for otu_oh in OduOverheads:
            if otu_oh.name == "tcm3" or otu_oh.name == "gcc1":
                first_row_transposed_data = list(zip(*row_data_frame))
                print(tabulate(first_row_transposed_data, headers=column_headers[start_index], tablefmt="grid",
                               stralign="center", numalign="center"))
                row_data_frame = []
                start_index += 1
            combined_value = ' '.join(self.overhead_field_finder(otu_oh))
            row_data_frame.append([combined_value])
        first_row_transposed_data = list(zip(*row_data_frame))
        print(tabulate(first_row_transposed_data, headers=column_headers[start_index], tablefmt="grid",
                       stralign="center", numalign="center"))
        return ""

