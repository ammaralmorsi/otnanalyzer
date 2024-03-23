from config.overhead.odu import OduOverheads
from tabulate import tabulate


class OduFrameParser:
    def __init__(self, formatted_frame):
        self._formatted_frame = formatted_frame
        self._overhead_data = {}
        for overhead in OduOverheads.get_fields():
            self._overhead_data[overhead.name] = self._formatted_frame[overhead.position.row][overhead.position.col:overhead.position.col + overhead.dimension.ncols]
            if len(overhead.inner_fields) > 0:
                self.__construct_inner_field(overhead)

    def __construct_inner_field(self , parent_overhead_field):
        """
            Below we are converting the parameter (parent field value) into binary to assign the data
            of the inner fields of parent field (which is the parameter in this func) ,
            as each inner field position is relative to its parent field, not the whole frame
        Args:
            Odu overhead field : that has a specific internal structure that are divided into inner fields
        """

        inner_field_value = self._overhead_data[parent_overhead_field.name]
        inner_binary_list = [bin(int(hex_str, 16))[2:].zfill(8) for hex_str in inner_field_value]
        inner_field_binary_value = ''.join(inner_binary_list)

        for inner_index in range(len(parent_overhead_field.inner_fields)):
            inner_name = parent_overhead_field.inner_fields[inner_index]
            inner_index_binary_value = inner_field_binary_value[inner_name.position.col:inner_name.position.col + inner_name.dimension.ncols]
            parent_overhead_field.inner_fields[inner_index] = hex(int(inner_index_binary_value, 2))[2:]

    @property
    def overhead_data(self):
        return self._overhead_data

    def overhead_field_finder(self, overhead):
        return self._overhead_data[overhead.name]

    def inner_overhead_field_data(self, overhead):
        if len(overhead.value.inner_fields) > 0:
            return overhead.value.inner_fields
        else:
            return ""

    def __str__(self):
        res: str = ""
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
            if otu_oh.value.name == OduOverheads.tcm3.value.name or otu_oh.value.name == OduOverheads.gcc1.value.name:
                first_row_transposed_data = list(zip(*row_data_frame))
                res += tabulate(first_row_transposed_data, headers=column_headers[start_index], tablefmt="grid", stralign="center", numalign="center")
                res += "\n"
                row_data_frame = []
                start_index += 1
            combined_value = ' '.join(self.overhead_field_finder(otu_oh))
            row_data_frame.append([combined_value])
        first_row_transposed_data = list(zip(*row_data_frame))
        res += tabulate(first_row_transposed_data, headers=column_headers[start_index], tablefmt="grid", stralign="center", numalign="center")
        res += "\n"
        return res
