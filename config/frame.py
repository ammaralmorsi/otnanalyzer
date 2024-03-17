import copy
import enum

from utils.field_types import OtnFrameTypes, OtnPayloadTypes
from utils.data_classes import Position, Dimension, OtnField, OtnFrame
from config.overhead import OpuOverheads, OduOverheads, OtuOverheads


class OtnFrameConfig(enum.Enum):
    DEFAULT_OPU_FRAME = OtnFrame(
        position=Position(row=0, col=14),
        dimension=Dimension(nrows=4, ncols=3810),
        payload=OtnField(
            name=OtnPayloadTypes.PRBS.name,
            field_type=OtnPayloadTypes.PRBS,
            position=Position(col=2, row=0),
            dimension=Dimension(nrows=4, ncols=3808)
        ),
        overheads=OpuOverheads.get_fields()
    )

    DEFAULT_ODU_FRAME = OtnFrame(
        position=Position(row=0, col=0),
        dimension=Dimension(nrows=4, ncols=3824),
        payload=OtnField(
            name=OtnPayloadTypes.PRBS.name,
            field_type=OtnPayloadTypes.PRBS,
            position=Position(row=0, col=14),
            dimension=Dimension(nrows=4, ncols=3810)
        ),
        overheads=OduOverheads.get_fields()
    )

    DEFAULT_OTU_FRAME = OtnFrame(
        position=Position(row=0, col=0),
        dimension=Dimension(nrows=4, ncols=3824),
        payload=OtnField(
            name=OtnPayloadTypes.PRBS.name,
            field_type=OtnPayloadTypes.PRBS,
            position=Position(row=0, col=0),
            dimension=Dimension(nrows=4, ncols=3824)
        ),
        overheads=OtuOverheads.get_fields()
    )

    @classmethod
    def get_new_frame(cls, frame_type: OtnFrameTypes, payload_type: OtnPayloadTypes, seed: int=2) -> OtnFrame:
        if frame_type == OtnFrameTypes.OPU:
            return cls._get_opu_frame(payload_type=payload_type, seed=seed)
        elif frame_type == OtnFrameTypes.ODU:
            return cls._get_odu_frame(payload_type=payload_type, seed=seed)
        elif frame_type == OtnFrameTypes.OTU:
            return cls._get_otu_frame(payload_type=payload_type, seed=seed)
        else:
            raise NotImplemented

    @classmethod
    def _get_opu_frame(cls, payload_type: OtnPayloadTypes, seed: int=2) -> OtnFrame:
        from generator.factory import GeneratorFactory
        new_frame: OtnFrame = cls._get_new_frame(cls.DEFAULT_OPU_FRAME.value, payload_type)
        new_frame.payload.generator = GeneratorFactory.get_payload_generator(new_frame.payload, seed)
        return new_frame

    @classmethod
    def _get_odu_frame(cls, payload_type: OtnPayloadTypes, seed: int=2) -> OtnFrame:
        from generator.factory import GeneratorFactory
        new_frame: OtnFrame = cls._get_new_frame(cls.DEFAULT_ODU_FRAME.value, payload_type)
        new_frame.payload.generator = GeneratorFactory.get_frame_generator(new_frame.payload, seed)
        return new_frame

    @classmethod
    def _get_otu_frame(cls, payload_type: OtnPayloadTypes, seed: int=2) -> OtnFrame:
        from generator.factory import GeneratorFactory
        new_frame: OtnFrame = cls._get_new_frame(cls.DEFAULT_OTU_FRAME.value, payload_type)
        new_frame.payload.generator = GeneratorFactory.get_frame_generator(new_frame.payload, seed)
        return new_frame

    @classmethod
    def _get_new_frame(cls, default_frame: OtnFrame, payload_type: OtnPayloadTypes) -> OtnFrame:
        from generator.factory import GeneratorFactory
        new_frame: OtnFrame = copy.deepcopy(default_frame)
        new_frame.set_payload_type(payload_type)
        for field in new_frame.overheads:
            field.generator = GeneratorFactory.get_overhead_generator(field)
        return new_frame
