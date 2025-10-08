from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer


class RemoteArgs(Message):
    class Arg():
        # __init__
        bool: 'bool'
        int32: 'int'  # int32
        int64: 'int'  # int64
        uint32: 'int'  # uint32
        uint64: 'int'  # uint64
        float: 'float'  # float32
        string: 'str'

    # __init__
    args: 'RepeatedCompositeFieldContainer[RemoteArgs.Arg]'
    bool: 'bool'
    int32: 'int'  # int32
    int64: 'int'  # int64
    uint32: 'int'  # uint32
    uint64: 'int'  # uint64
    float: 'float'  # float32
    string: 'str'


class RemoteUpdate(Message):
    class Command():
        # __init__
        name: 'str'
        desc: 'str'
        usage: 'str'

    # __init__
    commands: 'RepeatedCompositeFieldContainer[RemoteUpdate.Command]'
    name: 'str'
    desc: 'str'
    usage: 'str'


class CommandResponse(Message):
    # __init__
    resultcode: 'bool'
    resultString: 'str'


class KeyValResponse(Message):
    class KeyVal():
        # __init__
        key: 'str'
        value: 'str'

    # __init__
    keyvals: 'RepeatedCompositeFieldContainer[KeyValResponse.KeyVal]'
    key: 'str'
    value: 'str'


class SimTravelCommand(Message):
    # __init__
    destZoneID: 'int'  # uint64
    selectedSims: 'str'
