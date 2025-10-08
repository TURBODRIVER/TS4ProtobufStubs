from protocolbuffers._ProtobufTypes import Message

from protocolbuffers.Consts_pb2 import *
from protocolbuffers.Social_pb2 import *
from protocolbuffers.Exchange_pb2 import *


class RestControlMessage(Message):
    # __init__
    nucleus_id: 'int'  # uint64
    ref: 'int'  # uint64
    persona: 'str'
    social: 'SocialControlMessage'
    exchange: 'ExchangeControlMessage'
    error_message: 'RestApiErrorMessages'
    access_token: 'str'
