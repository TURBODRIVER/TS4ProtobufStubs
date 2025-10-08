from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer
from enum import IntEnum

from protocolbuffers.Consts_pb2 import *
from protocolbuffers.Math_pb2 import *
from protocolbuffers.ResourceKey_pb2 import *


class AwarenessChannelName(IntEnum):
    AWARENESS_CHANNEL_PROXIMITY: 'AwarenessChannelName' = 0
    AWARENESS_CHANNEL_AUDIO_VOLUME: 'AwarenessChannelName' = 1
    AWARENESS_CHANNEL_GAMEPLAY_0: 'AwarenessChannelName' = 1000
    AWARENESS_CHANNEL_GAMEPLAY_1: 'AwarenessChannelName' = 1001
    AWARENESS_CHANNEL_GAMEPLAY_2: 'AwarenessChannelName' = 1002
    AWARENESS_CHANNEL_GAMEPLAY_3: 'AwarenessChannelName' = 1003
    AWARENESS_CHANNEL_GAMEPLAY_4: 'AwarenessChannelName' = 1004
    AWARENESS_CHANNEL_GAMEPLAY_5: 'AwarenessChannelName' = 1005
    AWARENESS_CHANNEL_GAMEPLAY_6: 'AwarenessChannelName' = 1006
    AWARENESS_CHANNEL_GAMEPLAY_7: 'AwarenessChannelName' = 1007
    AWARENESS_CHANNEL_GAMEPLAY_8: 'AwarenessChannelName' = 1008
    AWARENESS_CHANNEL_GAMEPLAY_9: 'AwarenessChannelName' = 1009


AWARENESS_CHANNEL_PROXIMITY = AwarenessChannelName.AWARENESS_CHANNEL_PROXIMITY
AWARENESS_CHANNEL_AUDIO_VOLUME = AwarenessChannelName.AWARENESS_CHANNEL_AUDIO_VOLUME
AWARENESS_CHANNEL_GAMEPLAY_0 = AwarenessChannelName.AWARENESS_CHANNEL_GAMEPLAY_0
AWARENESS_CHANNEL_GAMEPLAY_1 = AwarenessChannelName.AWARENESS_CHANNEL_GAMEPLAY_1
AWARENESS_CHANNEL_GAMEPLAY_2 = AwarenessChannelName.AWARENESS_CHANNEL_GAMEPLAY_2
AWARENESS_CHANNEL_GAMEPLAY_3 = AwarenessChannelName.AWARENESS_CHANNEL_GAMEPLAY_3
AWARENESS_CHANNEL_GAMEPLAY_4 = AwarenessChannelName.AWARENESS_CHANNEL_GAMEPLAY_4
AWARENESS_CHANNEL_GAMEPLAY_5 = AwarenessChannelName.AWARENESS_CHANNEL_GAMEPLAY_5
AWARENESS_CHANNEL_GAMEPLAY_6 = AwarenessChannelName.AWARENESS_CHANNEL_GAMEPLAY_6
AWARENESS_CHANNEL_GAMEPLAY_7 = AwarenessChannelName.AWARENESS_CHANNEL_GAMEPLAY_7
AWARENESS_CHANNEL_GAMEPLAY_8 = AwarenessChannelName.AWARENESS_CHANNEL_GAMEPLAY_8
AWARENESS_CHANNEL_GAMEPLAY_9 = AwarenessChannelName.AWARENESS_CHANNEL_GAMEPLAY_9


class AnimationEventHandler(Message):
    # __init__
    event_type: 'int'  # uint32
    event_id: 'int'  # uint32
    tag: 'int'  # uint64


class AnimationRequestBlock(Message):
    # __init__
    arb_data: 'bytes'
    event_handlers: 'RepeatedCompositeFieldContainer[AnimationEventHandler]'
    objects_to_reset: 'RepeatedCompositeFieldContainer[ManagerObjectId]'
    is_interruptible: 'bool'
    should_analyze: 'bool'


class AnimationStateRequest(Message):
    # __init__
    asm: 'ResourceKey'
    state_name: 'str'
    actor_name: 'str'


class CurveData(Message):
    # __init__
    input_value: 'float'  # float32
    output_value: 'float'  # float32


class FocusEvent(Message):
    class EventType(IntEnum):
        FOCUS_ADD: 'FocusEvent.EventType' = 0
        FOCUS_DELETE: 'FocusEvent.EventType' = 1
        FOCUS_CLEAR: 'FocusEvent.EventType' = 2
        FOCUS_MODIFY_SCORE: 'FocusEvent.EventType' = 3
        FOCUS_DISABLE: 'FocusEvent.EventType' = 4
        FOCUS_FORCE_UPDATE: 'FocusEvent.EventType' = 5
        FOCUS_PRINT: 'FocusEvent.EventType' = 6

    FOCUS_ADD = EventType.FOCUS_ADD
    FOCUS_DELETE = EventType.FOCUS_DELETE
    FOCUS_CLEAR = EventType.FOCUS_CLEAR
    FOCUS_MODIFY_SCORE = EventType.FOCUS_MODIFY_SCORE
    FOCUS_DISABLE = EventType.FOCUS_DISABLE
    FOCUS_FORCE_UPDATE = EventType.FOCUS_FORCE_UPDATE
    FOCUS_PRINT = EventType.FOCUS_PRINT

    # __init__
    type: 'FocusEvent.EventType'
    id: 'int'  # uint32
    layer: 'int'  # uint32
    flags: 'int'  # uint32
    score: 'float'  # float32
    joint_name_hash: 'int'  # uint32
    target_id: 'int'  # uint64
    offset: 'Vector3'
    distance_curve: 'RepeatedCompositeFieldContainer[CurveData]'
    facing_curve: 'RepeatedCompositeFieldContainer[CurveData]'
    source_id: 'int'  # uint64


class ConfigureAwarenessActor(Message):
    class ChannelEvaluationMode(IntEnum):
        AWARENESS_CHANNEL_EVALMODE_PEAK: 'ConfigureAwarenessActor.ChannelEvaluationMode' = 0
        AWARENESS_CHANNEL_EVALMODE_AVERAGE: 'ConfigureAwarenessActor.ChannelEvaluationMode' = 1
        AWARENESS_CHANNEL_EVALMODE_SUM: 'ConfigureAwarenessActor.ChannelEvaluationMode' = 2
        AWARENESS_CHANNEL_EVALMODE_SUM_SPLITSIGN: 'ConfigureAwarenessActor.ChannelEvaluationMode' = 3
        AWARENESS_CHANNEL_EVALMODE_AVERAGE_SPLITSIGN: 'ConfigureAwarenessActor.ChannelEvaluationMode' = 4

    AWARENESS_CHANNEL_EVALMODE_PEAK = ChannelEvaluationMode.AWARENESS_CHANNEL_EVALMODE_PEAK
    AWARENESS_CHANNEL_EVALMODE_AVERAGE = ChannelEvaluationMode.AWARENESS_CHANNEL_EVALMODE_AVERAGE
    AWARENESS_CHANNEL_EVALMODE_SUM = ChannelEvaluationMode.AWARENESS_CHANNEL_EVALMODE_SUM
    AWARENESS_CHANNEL_EVALMODE_SUM_SPLITSIGN = ChannelEvaluationMode.AWARENESS_CHANNEL_EVALMODE_SUM_SPLITSIGN
    AWARENESS_CHANNEL_EVALMODE_AVERAGE_SPLITSIGN = ChannelEvaluationMode.AWARENESS_CHANNEL_EVALMODE_AVERAGE_SPLITSIGN

    class ChannelOptions():
        # __init__
        name: 'AwarenessChannelName'
        eval_mode: 'ConfigureAwarenessActor.ChannelEvaluationMode'
        gate: 'float'  # float32
        gain: 'float'  # float32
        limit: 'float'  # float32
        trigger_threshold_delta: 'float'  # float32
        type_name: 'str'
        hold_time: 'float'  # float32
        cool_down_time: 'float'  # float32

    # __init__
    channels_to_remove: 'RepeatedCompositeFieldContainer[AwarenessChannelName]'
    channels_to_configure: 'RepeatedCompositeFieldContainer[ConfigureAwarenessActor.ChannelOptions]'
    proximity_inner_radius: 'float'  # float32
    proximity_outer_radius: 'float'  # float32
    name: 'AwarenessChannelName'
    eval_mode: 'ConfigureAwarenessActor.ChannelEvaluationMode'
    gate: 'float'  # float32
    gain: 'float'  # float32
    limit: 'float'  # float32
    trigger_threshold_delta: 'float'  # float32
    type_name: 'str'
    hold_time: 'float'  # float32
    cool_down_time: 'float'  # float32


class ConfigureAwarenessSourceObject(Message):
    class GameplayChannelValue():
        # __init__
        name: 'AwarenessChannelName'
        value: 'float'  # float32

    # __init__
    gameplay_channel_values: 'RepeatedCompositeFieldContainer[ConfigureAwarenessSourceObject.GameplayChannelValue]'
    audio_volume_multiplier: 'float'  # float32
    audio_full_volume_radius: 'float'  # float32
    audio_falloff_radius: 'float'  # float32
    name: 'AwarenessChannelName'
    value: 'float'  # float32


class ProceduralControl(Message):
    class ProceduralControlType(IntEnum):
        UNKNOWN: 'ProceduralControl.ProceduralControlType' = 0
        WHEEL: 'ProceduralControl.ProceduralControlType' = 1
        SPHERE_WHEEL: 'ProceduralControl.ProceduralControlType' = 2
        SKATE: 'ProceduralControl.ProceduralControlType' = 3
        LIP_SYNC: 'ProceduralControl.ProceduralControlType' = 4

    UNKNOWN = ProceduralControlType.UNKNOWN
    WHEEL = ProceduralControlType.WHEEL
    SPHERE_WHEEL = ProceduralControlType.SPHERE_WHEEL
    SKATE = ProceduralControlType.SKATE
    LIP_SYNC = ProceduralControlType.LIP_SYNC

    # __init__
    control_id: 'int'  # uint32
    control_type: 'ProceduralControl.ProceduralControlType'
    joint_name_hash: 'int'  # uint32
    reference_joint_name_hash: 'int'  # uint32
    enable_terrain_alignment: 'bool'
    bump_sound_name: 'str'
    dimensions: 'Vector3'
    start_vfx: 'str'
    stop_vfx: 'str'
    start_sound: 'str'
    loop_sound: 'str'
    stop_sound: 'str'
    vfx_joint_name_hash: 'int'  # uint32
    effect_speed_threshold: 'float'  # float32
    jaw_flap_override: 'int'  # uint32


class ProceduralAnimationData(Message):
    # __init__
    controls: 'RepeatedCompositeFieldContainer[ProceduralControl]'


class ProceduralControlRotation(Message):
    # __init__
    control_id: 'int'  # uint32
    joint_hash: 'int'  # uint32
    duration: 'float'  # float32
    target_id: 'int'  # uint64
    target_joint_hash: 'int'  # uint32
    rotation: 'Quaternion'
    rotation_around_facing: 'float'  # float32
