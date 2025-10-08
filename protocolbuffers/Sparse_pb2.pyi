from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer
from enum import IntEnum

from protocolbuffers.Localization_pb2 import *


class SparseMessageData(Message):
    class FieldNumbers(IntEnum):
        kFN_0: 'SparseMessageData.FieldNumbers' = 1
        kFN_1: 'SparseMessageData.FieldNumbers' = 15
        kFN_2: 'SparseMessageData.FieldNumbers' = 2002

    kFN_0 = FieldNumbers.kFN_0
    kFN_1 = FieldNumbers.kFN_1
    kFN_2 = FieldNumbers.kFN_2

    # __init__
    set_fields: 'RepeatedCompositeFieldContainer[int]'  # int32


class TestSparseMessage(Message):
    # __init__
    sparse_data: 'SparseMessageData'
    int_field_a: 'int'  # int32
    int_field_b: 'int'  # int32
    int_field_c: 'int'  # int32
    int_field_d: 'int'  # int32
    int_rep_a: 'RepeatedCompositeFieldContainer[int]'  # int32
    int_rep_b: 'RepeatedCompositeFieldContainer[int]'  # int32
    str_field: 'str'
    str_rep: 'RepeatedCompositeFieldContainer[str]'
    sparse_msg_opt: 'TestSparseMessage2'
    sparse_msg_rep: 'RepeatedCompositeFieldContainer[TestSparseMessage2]'


class TestSparseMessage2(Message):
    # __init__
    sparse_data: 'SparseMessageData'
    str_field: 'str'
