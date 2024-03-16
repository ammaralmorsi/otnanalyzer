from config.overhead.otu import OtuOverheads
from config.overhead.inner import SmInnerFields

class Otu:

    def __init__(self, formatted_frame):

        self.formatted_frame = formatted_frame
        self.overhead_data = {}
        self.overhead_constructor()

    def overhead_constructor(self):

        for overhead in OtuOverheads:
            oh_value = overhead.value
            self.overhead_data[overhead.value.name] = (
                self.formatted_frame[oh_value.position.row]
                [oh_value.position.col:oh_value.position.col+oh_value.dimension.ncols]
            )

        """
        Below we are converting the sm field value into binary (24 bits) to assign the data
        of the inner fields of sm field , as each inner field position is relative to the sm field,
        not the whole frame
        """

        sm_field_value = self.overhead_data[OtuOverheads.sm.name]
        sm_binary_list = [bin(int(hex_str, 16))[2:].zfill(8) for hex_str in sm_field_value]
        sm_field_binary_value = ''.join(sm_binary_list)

        for inner_field in SmInnerFields:
            inner_value = inner_field.value
            inner_binary_value = sm_field_binary_value[inner_value.position.col:inner_value.position.col + inner_value.dimension.ncols]
            self.overhead_data[inner_field.value.name] = hex(int(inner_binary_value, 2))[2:]    #binary -> int -> hex , to store it back in original form

    def otu_overhead_data(self):
        return self.overhead_data

    def otu_overhead_field_finder(self, otu_oh):

        return self.overhead_data[otu_oh]



