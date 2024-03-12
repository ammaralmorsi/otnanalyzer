from generator.utils.frame import OduOverheads
from .opu import OpuFrameGenerator


class OduFrameGenerator:
    def __init__(self, opu_frame_generator:OpuFrameGenerator):
        self.opu_frame_generator:OpuFrameGenerator = opu_frame_generator
        self.overheads:OduOverheads = OduOverheads()
