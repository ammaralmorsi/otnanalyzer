from config.overhead.opu import OpuOverheads


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

    def opu_overhead_data(self):
        return self.overhead_data

    def opu_overhead_field_finder(self, opu_oh):
        return self.overhead_data[opu_oh.name]




