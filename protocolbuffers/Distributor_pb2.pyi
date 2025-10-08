from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer

from protocolbuffers.Consts_pb2 import *
from protocolbuffers.DistributorOps_pb2 import *


class ViewUpdateEntry(Message):
    # __init__
    primary_channel: 'OperationChannel'
    operation_list: 'OperationList'


class ViewUpdate(Message):
    # __init__
    entries: 'RepeatedCompositeFieldContainer[ViewUpdateEntry]'
