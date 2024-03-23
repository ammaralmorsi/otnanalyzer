from config.overhead.otu import OtuOverheads
from tabulate import tabulate


class OtuFrameParser:
    def __init__(self, formatted_frame):
        self._formatted_frame = formatted_frame
        self._overhead_data = {}
        for overhead in OtuOverheads.get_fields():
            self._overhead_data[overhead.name] = (
                self._formatted_frame[overhead.position.row]
                [overhead.position.col:overhead.position.col+overhead.dimension.ncols]
            )

            if len(overhead.inner_fields) > 0:
                self.construct_inner_field(overhead)

    def construct_inner_field(self , parent_overhead_field):
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
            parent_overhead_field.inner_fields[inner_index] = (
                hex(int(inner_index_binary_value, 2))[2:] # the [2:] to remove the 0x when converting to hex
            )

    @property
    def overhead_data(self):
        return self._overhead_data

    def overhead_field_finder(self, overhead):
        return self._overhead_data[overhead.name]

    def inner_overhead_field_data(self , overhead):
        if len(overhead.value.inner_fields) > 0:
            return overhead.value.inner_fields
        else:
            return ""

    def __str__(self):
        res: str = ""
        column_headers = ["FAS", "MFAS", "SM", "GCC0", "OSMC", "RES"]
        data_frame = []
        for otu_oh in OtuOverheads:
            combined_value = ' '.join(self.overhead_field_finder(otu_oh))
            data_frame.append([combined_value])
        transposed_data = list(zip(*data_frame))

        res += tabulate(transposed_data, headers=column_headers, tablefmt="grid" , stralign="center" , numalign="center")
        res += "\n"
        return res
