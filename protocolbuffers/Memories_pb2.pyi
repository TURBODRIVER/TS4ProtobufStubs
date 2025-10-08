from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer


class MemoriesList(Message):
    # __init__
    simId: 'int'  # uint64
    householdId: 'int'  # uint64
    isFavorites: 'bool'
    memoryIds: 'RepeatedCompositeFieldContainer[int]'  # uint64


class MemoriesFilterFile(Message):
    # __init__
    lists: 'RepeatedCompositeFieldContainer[MemoriesList]'
