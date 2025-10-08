from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer
from enum import IntEnum

from protocolbuffers.Math_pb2 import *


class DebugViz_LineSet(Message):
    class Line():
        # __init__
        begin: 'Vector3'
        end: 'Vector3'
        color: 'int'  # uint32

    # __init__
    lines: 'RepeatedCompositeFieldContainer[DebugViz_LineSet.Line]'
    begin: 'Vector3'
    end: 'Vector3'
    color: 'int'  # uint32


class DebugViz_Text(Message):
    class Alignment(IntEnum):
        ALIGN_LEFT: 'DebugViz_Text.Alignment' = 0
        ALIGN_CENTER: 'DebugViz_Text.Alignment' = 1
        ALIGN_RIGHT: 'DebugViz_Text.Alignment' = 2

    ALIGN_LEFT = Alignment.ALIGN_LEFT
    ALIGN_CENTER = Alignment.ALIGN_CENTER
    ALIGN_RIGHT = Alignment.ALIGN_RIGHT

    class VertAlign(IntEnum):
        VERTALIGN_TOP: 'DebugViz_Text.VertAlign' = 0
        VERTALIGN_MIDDLE: 'DebugViz_Text.VertAlign' = 1
        VERTALIGN_BOTTOM: 'DebugViz_Text.VertAlign' = 2

    VERTALIGN_TOP = VertAlign.VERTALIGN_TOP
    VERTALIGN_MIDDLE = VertAlign.VERTALIGN_MIDDLE
    VERTALIGN_BOTTOM = VertAlign.VERTALIGN_BOTTOM

    # __init__
    position_2d: 'Vector2'
    position_3d: 'Vector3'
    color_fg: 'int'  # uint32
    color_bg: 'int'  # uint32
    text: 'str'
    alignment: 'DebugViz_Text.Alignment'
    vertalign: 'DebugViz_Text.VertAlign'
    object_id: 'int'  # fixed uint64
    bone_index: 'int'  # int32


class DebugViz_Layer(Message):
    # __init__
    name: 'str'
    lines_data: 'bytes'
    zoneId: 'int'  # uint64
    text_set: 'RepeatedCompositeFieldContainer[DebugViz_Text]'
    tris_data: 'bytes'


class DebugViz_LayerUpdateNotification(Message):
    # __init__
    layerName: 'str'
    zoneId: 'int'  # uint64
