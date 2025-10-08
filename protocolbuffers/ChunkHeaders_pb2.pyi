from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer


class BlueprintThumbnailChunkPackageHeader(Message):
    # __init__
    blueprintID: 'int'  # uint64
    index: 'int'  # uint32


class LotThumbnailChunkPackageHeader(Message):
    # __init__
    blueprintID: 'int'  # uint64
    index: 'int'  # uint32


class MemoriesThumbnailChunkPackageHeader(Message):
    # __init__
    memoryId: 'int'  # uint64
    simIds: 'RepeatedCompositeFieldContainer[int]'  # uint64
    householdId: 'int'  # uint64
    favorite: 'bool'


class NeighborhoodThumbnailChunkPackageHeader(Message):
    # __init__
    blueprintID: 'int'  # uint64
