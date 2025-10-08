from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer


class UMMessage(Message):
    class AttributeList():
        # __init__
        attributes: 'RepeatedCompositeFieldContainer[str]'

    # __init__
    messages: 'RepeatedCompositeFieldContainer[UMMessage.AttributeList]'
    attributes: 'RepeatedCompositeFieldContainer[str]'


class RefreshFeatureParams(Message):
    # __init__
    key: 'int'  # uint64
