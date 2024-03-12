from generator.payload.prbs import PRBSPayloadGenerator
from generator.utils import OtnField, Dimension, Position
from generator.payload.null import NullPyaloadGenerator
from generator.utils.frame import NullOpuOverheads, PRBSOpuOverheads


class OpuFrameGenerator:
    def __init__(self):
        self.dimension:Dimension = Dimension(nrows=4, ncols=3810)
        self.frame:list[list[int]] = [[0 for _ in range(self.dimension.ncols)] for _ in range(self.dimension.nrows)]


class NullOpuFrameGenerator(OpuFrameGenerator):
    def __init__(self):
        super().__init__()
        self.overheads:NullOpuOverheads = NullOpuOverheads()
        self.payload:OtnField = OtnField(name="null", position=Position(col=2, row=0), dimension=Dimension(nrows=4, ncols=3808), generator=NullPyaloadGenerator())


class PRBSOpuFrameGenerator(OpuFrameGenerator):
    def __init__(self, seed:int):
        super().__init__()
        self.overheads:PRBSOpuOverheads = PRBSOpuOverheads()
        self.payload:OtnField = OtnField(name="null", position=Position(col=2, row=0), dimension=Dimension(nrows=4, ncols=3808), generator=PRBSPayloadGenerator(seed))
