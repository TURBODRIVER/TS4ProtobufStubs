from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer

from protocolbuffers.Consts_pb2 import *
from protocolbuffers.S4Common_pb2 import *


class BlobSimFacialCustomizationData(Message):
    class Modifier():
        # __init__
        key: 'int'  # uint64
        amount: 'float'  # float32

    # __init__
    sculpts: 'RepeatedCompositeFieldContainer[int]'  # uint64
    face_modifiers: 'RepeatedCompositeFieldContainer[BlobSimFacialCustomizationData.Modifier]'
    body_modifiers: 'RepeatedCompositeFieldContainer[BlobSimFacialCustomizationData.Modifier]'
    aged_face_modifiers: 'RepeatedCompositeFieldContainer[BlobSimFacialCustomizationData.Modifier]'
    aged_body_modifiers: 'RepeatedCompositeFieldContainer[BlobSimFacialCustomizationData.Modifier]'
    key: 'int'  # uint64
    amount: 'float'  # float32
