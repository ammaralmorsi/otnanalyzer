from generator.payload import FixedValuePayloadGenerator
from generator.payload import PRBSPayloadGenerator
from generator.overhead.custom import FixedValueOverheadGenerator
from generator.overhead.custom import SweepOverheadGenerator
from generator.overhead.fa import FASOverheadGenerator

from .data_classes import OtnField, OtnFieldTypes
from .base_classes import OverheadGenerator, PayloadGenerator


class GeneratorFactory:
    payload_type: OtnFieldTypes = OtnFieldTypes.OPU_PAYLOAD_PRBS

    @staticmethod
    def set_payload_type(field_type: OtnFieldTypes):
        GeneratorFactory.payload_type = field_type

    @staticmethod
    def get_overhead_generator(otn_field: OtnField) -> OverheadGenerator:
        if otn_field.field_type == OtnFieldTypes.PSI:
            if GeneratorFactory.payload_type == OtnFieldTypes.OPU_PAYLOAD_NULL:
                return FixedValueOverheadGenerator(fixed_value=int('FD', 16), size=otn_field.dimension.size)
            else:  # OPU_PAYLOAD_PRBS
                return FixedValueOverheadGenerator(fixed_value=int('FE', 16), size=otn_field.dimension.size)
        elif otn_field.field_type == OtnFieldTypes.JC:
            return FixedValueOverheadGenerator(fixed_value=0, size=otn_field.dimension.size)
        elif otn_field.field_type == OtnFieldTypes.PJO:
            return FixedValueOverheadGenerator(fixed_value=0, size=otn_field.dimension.size)
        elif otn_field.field_type == OtnFieldTypes.NJO:
            return FixedValueOverheadGenerator(fixed_value=0, size=otn_field.dimension.size)
        elif otn_field.field_type == OtnFieldTypes.GCC:
            return FixedValueOverheadGenerator(fixed_value=0, size=otn_field.dimension.size)
        elif otn_field.field_type == OtnFieldTypes.OSMC:
            return FixedValueOverheadGenerator(fixed_value=0, size=otn_field.dimension.size)
        elif otn_field.field_type == OtnFieldTypes.SM:
            return FixedValueOverheadGenerator(fixed_value=0, size=otn_field.dimension.size)
        elif otn_field.field_type == OtnFieldTypes.FAS:
            return FASOverheadGenerator()
        elif otn_field.field_type == OtnFieldTypes.MFAS:
            return SweepOverheadGenerator(start=0, end=255, size=otn_field.dimension.size)
        else:
            raise NotImplemented

    @staticmethod
    def get_payload_generator(otn_field: OtnField, seed: int=2) -> PayloadGenerator:
        if otn_field.field_type == OtnFieldTypes.OPU_PAYLOAD_PRBS:
            GeneratorFactory.payload_type = OtnFieldTypes.OPU_PAYLOAD_PRBS
            return PRBSPayloadGenerator(seed=seed)
        elif otn_field.field_type == OtnFieldTypes.OPU_PAYLOAD_NULL:
            GeneratorFactory.payload_type = OtnFieldTypes.OPU_PAYLOAD_NULL
            return FixedValuePayloadGenerator(fixed_value=0)
        else:
            raise NotImplemented
