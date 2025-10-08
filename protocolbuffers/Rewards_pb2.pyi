from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer

from protocolbuffers.ResourceKey_pb2 import *


class Rewards(Message):
    class Reward():
        # __init__
        instance: 'int'  # uint64

    # __init__
    rewards: 'RepeatedCompositeFieldContainer[Rewards.Reward]'
    instance: 'int'  # uint64
