from enum import Enum
from collections import namedtuple


# tuple to be able to make enum object having the start and end columns of frames
Frame_Column_Range = namedtuple('Frame_Column_Range', ['start', 'end'])

class Frames_Size(Enum):

    OTN = Frame_Column_Range(1, 3824)
    OPU = Frame_Column_Range(15, 3824)
    ODU = Frame_Column_Range(1, 14)
    OTU = Frame_Column_Range(1, 14)
    Raw_Data_Payload = Frame_Column_Range(17, 3808)