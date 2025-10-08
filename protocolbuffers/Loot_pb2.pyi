from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer

from protocolbuffers.S4Common_pb2 import *
from protocolbuffers.ResourceKey_pb2 import *
from protocolbuffers.Situations_pb2 import *
from protocolbuffers.UI_pb2 import *


class SituationEnded(Message):
    # __init__
    icon_info: 'IconInfo'
    final_score: 'int'  # uint32
    final_level: 'SituationLevelUpdate'
    sim_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    audio_sting: 'ResourceKey'
