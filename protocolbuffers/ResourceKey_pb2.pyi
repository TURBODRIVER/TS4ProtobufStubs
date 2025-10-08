from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer


class ResourceKey(Message):
    # __init__
    type: 'int'  # uint32
    group: 'int'  # uint32
    instance: 'int'  # uint64


class ResourceKeyList(Message):
    # __init__
    resource_keys: 'RepeatedCompositeFieldContainer[ResourceKey]'
