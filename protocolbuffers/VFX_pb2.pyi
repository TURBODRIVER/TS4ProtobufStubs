from protocolbuffers._ProtobufTypes import Message
from enum import IntEnum

from protocolbuffers.Math_pb2 import *


class VFXTransitionType(IntEnum):
    SOFT_TRANSITION: 'VFXTransitionType' = 0
    HARD_TRANSITION: 'VFXTransitionType' = 1


SOFT_TRANSITION = VFXTransitionType.SOFT_TRANSITION
HARD_TRANSITION = VFXTransitionType.HARD_TRANSITION


class VFXStart(Message):
    class VFXStartTransitionType(IntEnum):
        SOFT_TRANSITION: 'VFXStart.VFXStartTransitionType' = 0
        HARD_TRANSITION: 'VFXStart.VFXStartTransitionType' = 1

    SOFT_TRANSITION = VFXStartTransitionType.SOFT_TRANSITION
    HARD_TRANSITION = VFXStartTransitionType.HARD_TRANSITION

    # __init__
    object_id: 'int'  # uint64
    effect_name: 'str'
    actor_id: 'int'  # uint64
    joint_name_hash: 'int'  # uint32
    target_actor_id: 'int'  # uint64
    target_joint_name_hash: 'int'  # uint32
    mirror_effect: 'bool'
    auto_on_effect: 'bool'
    transition_type: 'VFXStart.VFXStartTransitionType'
    transform: 'Transform'
    target_joint_offset: 'Vector3'
    callback_event_id: 'int'  # uint32


class VFXStop(Message):
    class VFXStopTransitionType(IntEnum):
        SOFT_TRANSITION: 'VFXStop.VFXStopTransitionType' = 0
        HARD_TRANSITION: 'VFXStop.VFXStopTransitionType' = 1

    SOFT_TRANSITION = VFXStopTransitionType.SOFT_TRANSITION
    HARD_TRANSITION = VFXStopTransitionType.HARD_TRANSITION

    # __init__
    object_id: 'int'  # uint64
    actor_id: 'int'  # uint64
    transition_type: 'VFXStop.VFXStopTransitionType'


class VFXSetState(Message):
    # __init__
    object_id: 'int'  # uint64
    actor_id: 'int'  # uint64
    state_index: 'int'  # int32
    transition_type: 'VFXTransitionType'
