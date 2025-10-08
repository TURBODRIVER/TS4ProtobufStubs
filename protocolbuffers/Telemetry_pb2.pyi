from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer
from enum import IntEnum


class TelemetryAttribute(Message):
    class Type(IntEnum):
        NONE: 'TelemetryAttribute.Type' = 0
        BOOL: 'TelemetryAttribute.Type' = 1
        INT32: 'TelemetryAttribute.Type' = 2
        UINT32: 'TelemetryAttribute.Type' = 3
        FLOAT: 'TelemetryAttribute.Type' = 4
        STRING: 'TelemetryAttribute.Type' = 5
        UINT64: 'TelemetryAttribute.Type' = 6

    NONE = Type.NONE
    BOOL = Type.BOOL
    INT32 = Type.INT32
    UINT32 = Type.UINT32
    FLOAT = Type.FLOAT
    STRING = Type.STRING
    UINT64 = Type.UINT64

    # __init__
    name: 'int'  # uint32
    type: 'TelemetryAttribute.Type'
    boolval: 'bool'
    int32val: 'int'  # int32
    uint32val: 'int'  # uint32
    floatval: 'float'  # float32
    stringval: 'str'
    uint64val: 'int'  # uint64


class TelemetryMessage(Message):
    # __init__
    module: 'int'  # uint32
    group: 'int'  # uint32
    name: 'int'  # uint32
    timestamp: 'int'  # fixed uint32
    attrs: 'RepeatedCompositeFieldContainer[TelemetryAttribute]'


class TelemetryMessages(Message):
    # __init__
    messages: 'RepeatedCompositeFieldContainer[TelemetryMessage]'


class OfflineTelemetryMessage(Message):
    # __init__
    uint32val: 'int'  # uint32
    uint64val: 'int'  # uint64


class OfflineTelemetryMessages(Message):
    # __init__
    messages: 'RepeatedCompositeFieldContainer[OfflineTelemetryMessage]'
