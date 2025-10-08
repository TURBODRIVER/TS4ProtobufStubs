from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer


class ChunkPersistenceEntry(Message):
    # __init__
    dataCRC: 'int'  # uint32
    fileName: 'str'


class ChunkPersistenceFile(Message):
    # __init__
    entries: 'RepeatedCompositeFieldContainer[ChunkPersistenceEntry]'
