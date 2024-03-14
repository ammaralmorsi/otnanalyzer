from typing import Tuple, Optional, Dict
from dataclasses import dataclass

@dataclass
class otn_field_data:


    name : str
    parent_type: str     # otn opu odu
    inner_levels: Dict[str, 'otn_field_data']
    row_num: int
    column_start : int
    column_end : int
    column_num: Tuple[int, int] = 0
    num_of_bits: int = 8


    def __init__(self, name:str = "" , parent_type: str = "", row_num: int = None, column_start: int = None, column_end: int = None, num_of_bits: int = 8 , inner_levels: Optional[Dict[str, 'OTN_Field_Data']] = None):
        self.name = name
        self.parent_type = parent_type
        self.row_num = row_num
        self.column_start = column_start
        self.column_end = column_end if column_end is not None else column_start
        self.num_of_bits = num_of_bits
        self.column_num = (self.column_start, self.column_end)
        self.inner_levels = inner_levels if inner_levels is not None else {}


    def __hash__(self):
        return hash(self.name)


