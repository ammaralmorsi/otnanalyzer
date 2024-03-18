from utils.data_classes import OtnField 
from utils.field_types import OtnPayloadTypes, OtnFieldTypes
from utils.base_classes import OverheadGenerator, PayloadGenerator, FrameGenerator


class GeneratorFactory:
    payload_type: OtnPayloadTypes = OtnPayloadTypes.PRBS

    @staticmethod
    def set_payload_type(payload_type: OtnPayloadTypes):
        GeneratorFactory.payload_type = payload_type

    @staticmethod
    def get_overhead_generator(otn_field: OtnField) -> OverheadGenerator:
        if otn_field.field_type == OtnFieldTypes.PSI:
            from .overhead.custom import FixedValueOverheadGenerator
            if GeneratorFactory.payload_type == OtnPayloadTypes.NULL:
                return FixedValueOverheadGenerator(fixed_value=int('FD', 16), size=otn_field.dimension.size)
            else:  # OPU_PAYLOAD_PRBS
                return FixedValueOverheadGenerator(fixed_value=int('FE', 16), size=otn_field.dimension.size)
        elif otn_field.field_type == OtnFieldTypes.FAS:
            from .overhead.fa import FASOverheadGenerator
            return FASOverheadGenerator()
        elif otn_field.field_type == OtnFieldTypes.MFAS:
            from .overhead.custom import SweepOverheadGenerator
            return SweepOverheadGenerator(start=0, end=255, size=otn_field.dimension.size)
        elif otn_field.field_type in [
                OtnFieldTypes.JC,
                OtnFieldTypes.PJO,
                OtnFieldTypes.NJO,
                OtnFieldTypes.OSMC,
                OtnFieldTypes.GCC,
                OtnFieldTypes.SM,
                OtnFieldTypes.PM_TCM,
                OtnFieldTypes.APS_PCC,
                OtnFieldTypes.TCM,
                OtnFieldTypes.PM,
                OtnFieldTypes.EXP,
                OtnFieldTypes.RES,
            ]:
            from .overhead.custom import FixedValueOverheadGenerator
            return FixedValueOverheadGenerator(fixed_value=0, size=otn_field.dimension.size)
        else:
            raise NotImplemented

    @staticmethod
    def get_payload_generator(otn_field: OtnField, seed: int=2) -> PayloadGenerator:
        GeneratorFactory.set_payload_type(otn_field.field_type)
        if GeneratorFactory.payload_type == OtnPayloadTypes.PRBS:
            from .payload import PRBSPayloadGenerator
            return PRBSPayloadGenerator(seed=seed)
        elif GeneratorFactory.payload_type == OtnPayloadTypes.NULL:
            from .payload import FixedValuePayloadGenerator
            return FixedValuePayloadGenerator(fixed_value=0)
        else:
            raise NotImplemented

    @staticmethod
    def get_frame_generator(otn_field: OtnField, seed: int) -> FrameGenerator:
        GeneratorFactory.set_payload_type(otn_field.field_type)
        if GeneratorFactory.payload_type in [OtnPayloadTypes.NULL, OtnPayloadTypes.PRBS]:
            from .frame.opu import OpuFrameGenerator
            return OpuFrameGenerator(payload_type=GeneratorFactory.payload_type, seed=seed)
        elif GeneratorFactory.payload_type in [OtnPayloadTypes.NULL, OtnPayloadTypes.PRBS]:
            from .frame.odu import OduFrameGenerator
            return OduFrameGenerator(payload_type=GeneratorFactory.payload_type, seed=seed)
        else:
            raise NotImplemented
