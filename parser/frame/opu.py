from config.frame import OtnFrameConfig
from config.overhead.opu import OpuOverheads
from tabulate import tabulate

class OpuFrameParser:
    def __init__(self, formatted_frame):
        self._formatted_frame = formatted_frame
        self._overhead_data = {}
        for overhead in OpuOverheads.get_fields():
            self._overhead_data[overhead.name] = self._formatted_frame[overhead.position.row][overhead.position.col:overhead.position.col + overhead.dimension.ncols]

    @property
    def payload_data(self):
        opu_frame_configuration = OtnFrameConfig.DEFAULT_OPU_FRAME.value
        start_col: int = opu_frame_configuration.position.col + opu_frame_configuration.payload.position.col
        return [row[start_col:] for row in self._formatted_frame]

    @property
    def overhead_data(self):
        return self._overhead_data

    def overhead_field_finder(self, overhead):
        return self._overhead_data[overhead.name]

    def __str__(self):
        res: str = ""
        header_itr = 0
        column_header = [["JC4", "JC1"], ["JC5", "JC2"], ["JC6", "JC3"], ["PSI", "NJO" , "PJO"]]
        row_data_frame = []
        for opu_oh in OpuOverheads:
            if opu_oh.name == OpuOverheads.jc5.value.name or opu_oh.name == OpuOverheads.jc6.value.name or opu_oh.name == OpuOverheads.psi.value.name:
                first_row_transposed_data = list(zip(*row_data_frame))
                res += tabulate(first_row_transposed_data, headers=column_header[header_itr], tablefmt="grid", stralign="center", numalign="center")
                res += "\n"
                row_data_frame = []
                header_itr += 1
            combined_value = ' '.join(self.overhead_field_finder(opu_oh))
            row_data_frame.append([combined_value])
        first_row_transposed_data = list(zip(*row_data_frame))
        res += tabulate(first_row_transposed_data, headers=column_header[3], tablefmt="grid", stralign="center", numalign="center")
        res += "\n"
        return res
