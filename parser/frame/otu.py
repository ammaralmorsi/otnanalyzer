from config.overhead.otu import OtuOverheads
from config.overhead.inner import SmInnerFields
from tabulate import tabulate


class Otu:

    def __init__(self, formatted_frame):

        self._formatted_frame = formatted_frame
        self._overhead_data = {}
        self.__overhead_constructor()

    def __overhead_constructor(self):

        for overhead in OtuOverheads:
            oh_value = overhead.value
            self._overhead_data[overhead.value.name] = (
                self._formatted_frame[oh_value.position.row]
                [oh_value.position.col:oh_value.position.col+oh_value.dimension.ncols]
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

    def overhead_field_finder(self, otu_oh):

        return self._overhead_data[otu_oh.name]

    def inner_overhead_field_data(self , otu_oh_with_inner_fields):
        if len(otu_oh_with_inner_fields.value.inner_fields) > 0:
            return otu_oh_with_inner_fields.value.inner_fields
        else:
            return ""

    def __str__(self):
        column_headers = ["FAS", "MFAS", "SM", "GCC0", "OSMC", "RES"]
        data_frame = []
        for otu_oh in OtuOverheads:
            combined_value = ' '.join(self.overhead_field_finder(otu_oh))
            data_frame.append([combined_value])
        transposed_data = list(zip(*data_frame))

        print(tabulate(transposed_data, headers=column_headers, tablefmt="grid" , stralign="center" , numalign="center"))
        return ""


