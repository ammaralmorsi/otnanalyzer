from enum import Enum
from collections import namedtuple



class OTN_Frames():

    FRAME_SIZES = {
        'OTN' : 3824,
        'OPU' : 3810,
        'ODU' : 15,
        'OTU' : 15,
    }