from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer
from enum import IntEnum

from protocolbuffers.Consts_pb2 import *


class LocalizedStringToken(Message):
    class TokenType(IntEnum):
        INVALID: 'LocalizedStringToken.TokenType' = 0
        SIM: 'LocalizedStringToken.TokenType' = 1
        STRING: 'LocalizedStringToken.TokenType' = 2
        RAW_TEXT: 'LocalizedStringToken.TokenType' = 3
        NUMBER: 'LocalizedStringToken.TokenType' = 4
        OBJECT: 'LocalizedStringToken.TokenType' = 5
        DATE_AND_TIME: 'LocalizedStringToken.TokenType' = 6
        RICHDATA: 'LocalizedStringToken.TokenType' = 7
        STRING_LIST: 'LocalizedStringToken.TokenType' = 8
        SIM_LIST: 'LocalizedStringToken.TokenType' = 9

    INVALID = TokenType.INVALID
    SIM = TokenType.SIM
    STRING = TokenType.STRING
    RAW_TEXT = TokenType.RAW_TEXT
    NUMBER = TokenType.NUMBER
    OBJECT = TokenType.OBJECT
    DATE_AND_TIME = TokenType.DATE_AND_TIME
    RICHDATA = TokenType.RICHDATA
    STRING_LIST = TokenType.STRING_LIST
    SIM_LIST = TokenType.SIM_LIST

    class GenderFlags(IntEnum):
        GENDER_NEUTRAL: 'LocalizedStringToken.GenderFlags' = 0
        GENDER_MALE: 'LocalizedStringToken.GenderFlags' = 4096
        GENDER_FEMALE: 'LocalizedStringToken.GenderFlags' = 8192

    GENDER_NEUTRAL = GenderFlags.GENDER_NEUTRAL
    GENDER_MALE = GenderFlags.GENDER_MALE
    GENDER_FEMALE = GenderFlags.GENDER_FEMALE

    class SubTokenData():
        # __init__
        type: 'LocalizedStringToken.TokenType'
        first_name: 'str'
        last_name: 'str'
        full_name_key: 'int'  # uint32
        is_female: 'bool'
        gender_flags: 'LocalizedStringToken.GenderFlags'
        packed_pronouns: 'str'
        age_flags: 'int'  # uint32

    # __init__
    type: 'LocalizedStringToken.TokenType'
    rdl_type: 'SocialRichDataType'
    first_name: 'str'
    last_name: 'str'
    full_name_key: 'int'  # uint32
    is_female: 'bool'
    gender_flags: 'LocalizedStringToken.GenderFlags'
    age_flags: 'int'  # uint32
    sim_id: 'int'  # uint64
    packed_pronouns: 'str'
    name_prefix_key: 'int'  # uint32
    name_prefix_string: 'str'
    text_string: 'LocalizedString'
    number: 'float'  # float32
    persona_id: 'int'  # uint64
    account_id: 'int'  # uint64
    persona_string: 'str'
    zone_id: 'int'  # uint64
    world_id: 'int'  # uint32
    zone_name: 'str'
    event_id: 'int'  # uint64
    event_type_hash: 'int'  # uint32
    skill_name_hash: 'int'  # uint32
    skill_level: 'int'  # uint32
    skill_guid: 'int'  # uint64
    trait_name_hash: 'int'  # uint32
    trait_guid: 'int'  # uint64
    bit_name_hash: 'int'  # uint32
    bit_guid: 'int'  # uint64
    catalog_name_key: 'int'  # uint32
    catalog_description_key: 'int'  # uint32
    custom_name: 'str'
    custom_description: 'str'
    career_uid: 'int'  # uint64
    memory_id: 'int'  # uint64
    memory_string_hash: 'int'  # uint32
    raw_text: 'str'
    date_and_time: 'LocalizedDateAndTimeData'
    sim_list: 'RepeatedCompositeFieldContainer[LocalizedStringToken.SubTokenData]'
    type: 'LocalizedStringToken.TokenType'
    first_name: 'str'
    last_name: 'str'
    full_name_key: 'int'  # uint32
    is_female: 'bool'
    gender_flags: 'LocalizedStringToken.GenderFlags'
    packed_pronouns: 'str'
    age_flags: 'int'  # uint32


class LocalizedDateAndTimeData(Message):
    # __init__
    seconds: 'int'  # uint32
    minutes: 'int'  # uint32
    hours: 'int'  # uint32
    date: 'int'  # uint32
    month: 'int'  # uint32
    full_year: 'int'  # uint32
    date_and_time_format_hash: 'int'  # uint32


class LocalizedString(Message):
    # __init__
    hash: 'int'  # uint32
    tokens: 'RepeatedCompositeFieldContainer[LocalizedStringToken]'


class LocalizedStringValidate(Message):
    # __init__
    localized_strings: 'RepeatedCompositeFieldContainer[LocalizedString]'
