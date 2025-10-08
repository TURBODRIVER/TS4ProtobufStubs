from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer
from enum import IntEnum


class VehicleControl(Message):
    class VehicleControlType(IntEnum):
        UNKNOWN: 'VehicleControl.VehicleControlType' = 0
        WHEEL: 'VehicleControl.VehicleControlType' = 1

    UNKNOWN = VehicleControlType.UNKNOWN
    WHEEL = VehicleControlType.WHEEL

    # __init__
    control_id: 'int'  # uint32
    control_type: 'VehicleControl.VehicleControlType'
    joint_name_hash: 'int'  # uint32
    reference_joint_name_hash: 'int'  # uint32
    enable_terrain_alignment: 'bool'
    bump_sound_name: 'str'


class VehicleData(Message):
    # __init__
    controls: 'RepeatedCompositeFieldContainer[VehicleControl]'
