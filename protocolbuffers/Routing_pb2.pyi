from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer
from enum import IntEnum

from protocolbuffers.Math_pb2 import *


class SurfaceId(Message):
    # __init__
    primary_id: 'int'  # uint64
    secondary_id: 'int'  # int32
    type: 'int'  # uint32
    routable_surface_height: 'int'  # int32


class RouteNodeData(Message):
    class DataType(IntEnum):
        DATA_STAIRS: 'RouteNodeData.DataType' = 1
        DATA_ANIMATE: 'RouteNodeData.DataType' = 2
        DATA_LADDER: 'RouteNodeData.DataType' = 3

    DATA_STAIRS = DataType.DATA_STAIRS
    DATA_ANIMATE = DataType.DATA_ANIMATE
    DATA_LADDER = DataType.DATA_LADDER

    # __init__
    type: 'RouteNodeData.DataType'
    data: 'bytes'
    do_stop_transition: 'bool'
    do_start_transition: 'bool'


class RouteStairsData(Message):
    # __init__
    traversing_up: 'bool'
    stair_count: 'int'  # uint32
    walkstyle: 'int'  # uint32
    stairs_per_cycle: 'int'  # uint32


class RouteLadderData(Message):
    class LadderType(IntEnum):
        LADDER_OCEAN: 'RouteLadderData.LadderType' = 0
        LADDER_BUILD: 'RouteLadderData.LadderType' = 1

    LADDER_OCEAN = LadderType.LADDER_OCEAN
    LADDER_BUILD = LadderType.LADDER_BUILD

    class PortalAlignment(IntEnum):
        PA_FRONT: 'RouteLadderData.PortalAlignment' = 0
        PA_LEFT: 'RouteLadderData.PortalAlignment' = 1
        PA_RIGHT: 'RouteLadderData.PortalAlignment' = 2

    PA_FRONT = PortalAlignment.PA_FRONT
    PA_LEFT = PortalAlignment.PA_LEFT
    PA_RIGHT = PortalAlignment.PA_RIGHT

    # __init__
    traversing_up: 'bool'
    step_count: 'int'  # uint32
    ladder_type: 'RouteLadderData.LadderType'
    portal_alignment: 'RouteLadderData.PortalAlignment'


class RouteAnimateData(Message):
    # __init__
    arb_data: 'bytes'


class RouteNode(Message):
    # __init__
    location: 'Transform'
    time: 'float'  # float32
    action: 'int'  # uint32
    walkstyle: 'int'  # uint32
    routing_surface_id: 'SurfaceId'
    portal_object_id: 'int'  # uint64
    node_data: 'RouteNodeData'
    surface_object_id: 'int'  # uint64
    is_procedural: 'bool'


class Location(Message):
    # __init__
    transform: 'Transform'
    level: 'int'  # int32
    parent_id: 'int'  # uint64
    joint_name_hash: 'int'  # uint32
    slot_hash: 'int'  # uint32
    surface_id: 'SurfaceId'


class GoalPoint(Message):
    # __init__
    location: 'Transform'
    weight: 'float'  # float32
    radius: 'float'  # float32


class RoutePoint(Message):
    # __init__
    pos: 'Vector2'


class RoutePolygon(Message):
    # __init__
    points: 'RepeatedCompositeFieldContainer[RoutePoint]'
    routing_surface_id: 'SurfaceId'


class RoutePolygons(Message):
    # __init__
    polygons: 'RepeatedCompositeFieldContainer[RoutePolygon]'


class RouteEvent(Message):
    class Type(IntEnum):
        PORTAL_ENTER: 'RouteEvent.Type' = 0
        PORTAL_EXIT: 'RouteEvent.Type' = 1
        PORTAL_CHANGE_OPACITY: 'RouteEvent.Type' = 2
        CONTROLLER_EVENT: 'RouteEvent.Type' = 3
        BARRIER_EVENT: 'RouteEvent.Type' = 4

    PORTAL_ENTER = Type.PORTAL_ENTER
    PORTAL_EXIT = Type.PORTAL_EXIT
    PORTAL_CHANGE_OPACITY = Type.PORTAL_CHANGE_OPACITY
    CONTROLLER_EVENT = Type.CONTROLLER_EVENT
    BARRIER_EVENT = Type.BARRIER_EVENT

    # __init__
    id: 'int'  # uint64
    type: 'RouteEvent.Type'
    time: 'float'  # float32
    duration: 'float'  # float32
    tag: 'int'  # uint64
    skippable: 'bool'
    data: 'bytes'


class PortalEnterEvent(Message):
    # __init__
    portal_object_id: 'int'  # uint64
    entering_front: 'bool'


class PortalExitEvent(Message):
    # __init__
    portal_object_id: 'int'  # uint64


class PortalChangeOpacityEvent(Message):
    # __init__
    object_id: 'int'  # fixed uint64
    opacity: 'float'  # float32
    duration: 'float'  # float32


class ControllerEvent(Message):
    class DataType(IntEnum):
        UINT32: 'ControllerEvent.DataType' = 0
        FLOAT: 'ControllerEvent.DataType' = 1
        ARB: 'ControllerEvent.DataType' = 2

    UINT32 = DataType.UINT32
    FLOAT = DataType.FLOAT
    ARB = DataType.ARB

    # __init__
    object_id: 'int'  # uint64
    event_id: 'int'  # uint32
    data_type: 'int'  # uint32
    data: 'bytes'


class ControllerEventUInt32(Message):
    # __init__
    data: 'int'  # uint32


class ControllerEventFloat(Message):
    # __init__
    data: 'float'  # float32


class ControllerEventARB(Message):
    # __init__
    data: 'bytes'


class NoiseParameters(Message):
    # __init__
    octave_count: 'int'  # uint32
    frequency: 'float'  # float32
    max_x_distance: 'float'  # float32
    max_z_distance: 'float'  # float32


class SpringParameters(Message):
    # __init__
    tension: 'float'  # float32
    damping: 'float'  # float32
    velocity_scale: 'float'  # float32


class FishtailParameters(Message):
    # __init__
    noise_behavior: 'NoiseParameters'
    spring_behavior: 'SpringParameters'


class AttachmentInfo(Message):
    class RoutingFormationFollowType(IntEnum):
        NODE_TYPE_FOLLOW_LEADER: 'AttachmentInfo.RoutingFormationFollowType' = 0
        NODE_TYPE_CHAIN: 'AttachmentInfo.RoutingFormationFollowType' = 1
        NODE_TYPE_FISHTAIL: 'AttachmentInfo.RoutingFormationFollowType' = 2

    NODE_TYPE_FOLLOW_LEADER = RoutingFormationFollowType.NODE_TYPE_FOLLOW_LEADER
    NODE_TYPE_CHAIN = RoutingFormationFollowType.NODE_TYPE_CHAIN
    NODE_TYPE_FISHTAIL = RoutingFormationFollowType.NODE_TYPE_FISHTAIL

    # __init__
    parent_offset: 'Vector2'
    offset: 'Vector2'
    angle_constraint: 'float'  # float32
    radius: 'float'  # float32
    flags: 'int'  # uint32
    type: 'AttachmentInfo.RoutingFormationFollowType'
    fishtail_behavior: 'FishtailParameters'


class WalkstyleOverride(Message):
    # __init__
    from_walkstyle: 'int'  # uint32
    to_walkstyle: 'int'  # uint32


class SlaveData(Message):
    class Type(IntEnum):
        SLAVE_NONE: 'SlaveData.Type' = 0
        SLAVE_FOLLOW_ATTACHMENT: 'SlaveData.Type' = 1
        SLAVE_PAIRED_CHILD: 'SlaveData.Type' = 2

    SLAVE_NONE = Type.SLAVE_NONE
    SLAVE_FOLLOW_ATTACHMENT = Type.SLAVE_FOLLOW_ATTACHMENT
    SLAVE_PAIRED_CHILD = Type.SLAVE_PAIRED_CHILD

    # __init__
    id: 'int'  # uint64
    type: 'SlaveData.Type'
    offset: 'RepeatedCompositeFieldContainer[AttachmentInfo]'
    walkstyle_overrides: 'RepeatedCompositeFieldContainer[WalkstyleOverride]'
    slaves: 'RepeatedCompositeFieldContainer[SlaveData]'
    final_location_override: 'Transform'


class Route(Message):
    # __init__
    id: 'int'  # uint64
    nodes: 'RepeatedCompositeFieldContainer[RouteNode]'
    time: 'float'  # float32
    absolute_time_ms: 'int'  # uint64
    goals: 'RepeatedCompositeFieldContainer[GoalPoint]'
    events: 'RepeatedCompositeFieldContainer[RouteEvent]'
    bounds_polygons: 'RepeatedCompositeFieldContainer[RoutePolygon]'
    track: 'int'  # uint32
    obstacle_polygons: 'RepeatedCompositeFieldContainer[RoutePolygons]'
    slaves: 'RepeatedCompositeFieldContainer[SlaveData]'
    mask: 'int'  # uint32
