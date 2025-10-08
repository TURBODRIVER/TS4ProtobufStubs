from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer
from enum import IntEnum

from protocolbuffers.ResourceKey_pb2 import *
from protocolbuffers.Localization_pb2 import *
from protocolbuffers.UI_pb2 import *
from protocolbuffers.Consts_pb2 import *
from protocolbuffers.SimObjectAttributes_pb2 import *


class SentimentSignType(IntEnum):
    SIGN_INVALID: 'SentimentSignType' = 0
    SIGN_POSITIVE: 'SentimentSignType' = 1
    SIGN_NEGATIVE: 'SentimentSignType' = 2


SIGN_INVALID = SentimentSignType.SIGN_INVALID
SIGN_POSITIVE = SentimentSignType.SIGN_POSITIVE
SIGN_NEGATIVE = SentimentSignType.SIGN_NEGATIVE


class SentimentDurationType(IntEnum):
    DURATION_INVALID: 'SentimentDurationType' = 0
    DURATION_LONG: 'SentimentDurationType' = 1
    DURATION_SHORT: 'SentimentDurationType' = 2


DURATION_INVALID = SentimentDurationType.DURATION_INVALID
DURATION_LONG = SentimentDurationType.DURATION_LONG
DURATION_SHORT = SentimentDurationType.DURATION_SHORT


class RelationshipTrackType(IntEnum):
    TYPE_RELATIONSHIP: 'RelationshipTrackType' = 0
    TYPE_SENTIMENT: 'RelationshipTrackType' = 1


TYPE_RELATIONSHIP = RelationshipTrackType.TYPE_RELATIONSHIP
TYPE_SENTIMENT = RelationshipTrackType.TYPE_SENTIMENT


class Skill_Update(Message):
    # __init__
    skill_id: 'int'  # uint64
    curr_points: 'int'  # uint32
    sim_id: 'int'  # uint64


class SkillProgressUpdate(Message):
    # __init__
    skill_id: 'int'  # fixed uint64
    change_rate: 'float'  # float32
    curr_points: 'int'  # uint32
    hide_progress_bar: 'bool'


class SkillDelete(Message):
    # __init__
    skill_id: 'int'  # fixed uint64


class RelationshipTrack(Message):
    # __init__
    track_score: 'float'  # float32
    track_bit_id: 'int'  # uint32
    track_id: 'int'  # fixed uint64
    track_popup_priority: 'int'  # uint32
    change_rate: 'float'  # float32
    delta: 'float'  # float32
    visible_in_relationship_panel: 'bool'
    track_type: 'RelationshipTrackType'
    sign_type: 'SentimentSignType'
    duration_type: 'SentimentDurationType'
    archetype_name: 'LocalizedString'
    track_name: 'LocalizedString'


class RelationshipUpdate(Message):
    # __init__
    score: 'float'  # float32
    bit_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    track_bit_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    actor_sim_id: 'int'  # uint64
    target_sim_id: 'int'  # uint64
    handshake_bit_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    tracks: 'RepeatedCompositeFieldContainer[RelationshipTrack]'
    known_trait_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    target_id: 'ManagerObjectId'
    target_instance_id: 'int'  # uint64
    target_sim_significant_other_id: 'int'  # fixed uint64
    num_traits: 'int'  # uint32
    known_careertrack_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    last_update_time: 'int'  # uint64
    known_stat_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    target_icon_override: 'IconInfo'
    bit_updates: 'RepeatedCompositeFieldContainer[RelationshipBitUpdate]'
    known_major_id: 'int'  # uint64
    is_load: 'bool'
    target_sim_fiance_id: 'int'  # fixed uint64
    knows_romantic_preference: 'bool'
    knows_woohoo_preference: 'bool'
    known_romantic_genders: 'RepeatedCompositeFieldContainer[int]'  # uint32
    known_woohoo_genders: 'RepeatedCompositeFieldContainer[int]'  # uint32
    known_exploring_sexuality: 'bool'
    compatibility: 'CompatibilityUpdate'
    unconfronted_secret_id: 'int'  # uint64
    known_confronted_secrets: 'RepeatedCompositeFieldContainer[ConfrontedSimSecret]'
    relationship_label_data: 'RelationshipLabelDataUpdate'
    known_rel_track_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    known_relationship_expectations_ids: 'RepeatedCompositeFieldContainer[int]'  # uint32
    hidden: 'bool'


class CompatibilityUpdate(Message):
    # __init__
    level: 'int'  # uint64
    icon: 'ResourceKey'
    small_icon: 'ResourceKey'
    name: 'LocalizedString'
    desc: 'LocalizedString'


class RelationshipBitUpdate(Message):
    # __init__
    bit_id: 'int'  # fixed uint64
    end_time: 'int'  # uint64


class RelationshipDelete(Message):
    # __init__
    actor_sim_id: 'int'  # uint64
    target_id: 'int'  # uint64


class RelHandshakeUpdate(Message):
    class HandshakeStatus(IntEnum):
        NONE: 'RelHandshakeUpdate.HandshakeStatus' = 0
        PENDING: 'RelHandshakeUpdate.HandshakeStatus' = 1
        ACCEPTED: 'RelHandshakeUpdate.HandshakeStatus' = 2
        DENIED: 'RelHandshakeUpdate.HandshakeStatus' = 3
        PENDING_RECIEVER: 'RelHandshakeUpdate.HandshakeStatus' = 4

    NONE = HandshakeStatus.NONE
    PENDING = HandshakeStatus.PENDING
    ACCEPTED = HandshakeStatus.ACCEPTED
    DENIED = HandshakeStatus.DENIED
    PENDING_RECIEVER = HandshakeStatus.PENDING_RECIEVER

    # __init__
    actor_sim_id: 'int'  # uint64
    target_sim_id: 'int'  # uint64
    bit_ids: 'RepeatedCompositeFieldContainer[int]'  # uint32
    bit_status: 'RepeatedCompositeFieldContainer[RelHandshakeUpdate.HandshakeStatus]'


class RelationshipLabelDataUpdate(Message):
    # __init__
    label: 'str'
    icon: 'ResourceKey'


class CommodityStaticData(Message):
    # __init__
    commodity_id: 'int'  # uint32
    pos_icon_info: 'IconInfo'
    neutral_icon_info: 'IconInfo'
    neg_icon_info: 'IconInfo'
    commodity_name: 'LocalizedString'
    commodity_states: 'RepeatedCompositeFieldContainer[IconInfo]'
    threshold_index: 'int'  # uint32


class CommodityStaticDataList(Message):
    # __init__
    commodity_data: 'RepeatedCompositeFieldContainer[CommodityStaticData]'


class CommodityUpdate(Message):
    # __init__
    commodity_ids: 'RepeatedCompositeFieldContainer[int]'  # uint32
    change_rate: 'RepeatedCompositeFieldContainer[float]'  # float32
    commodity_image_index: 'RepeatedCompositeFieldContainer[int]'  # uint32
    commodity_guids: 'RepeatedCompositeFieldContainer[int]'  # uint64


class CommodityProgressUpdate(Message):
    class UpdateType(IntEnum):
        UPDATE: 'CommodityProgressUpdate.UpdateType' = 0
        REMOVE: 'CommodityProgressUpdate.UpdateType' = 1

    UPDATE = UpdateType.UPDATE
    REMOVE = UpdateType.REMOVE

    # __init__
    commodity_id: 'int'  # fixed uint64
    current_value: 'float'  # float32
    rate_of_change: 'float'  # float32
    commodity_state_index: 'int'  # uint32
    is_rate_change: 'bool'
    update_type: 'CommodityProgressUpdate.UpdateType'
    adjusted_state_index: 'int'  # uint32
    affects_plumbob_color: 'bool'


class CommodityProgressUpdateList(Message):
    # __init__
    commodities: 'RepeatedCompositeFieldContainer[CommodityProgressUpdate]'


class CommodityListUpdate(Message):
    # __init__
    sim_id: 'int'  # uint64
    commodities: 'RepeatedCompositeFieldContainer[CommodityProgressUpdate]'
    motive_commodity_index: 'int'  # uint32
    commodity_lists: 'RepeatedCompositeFieldContainer[CommodityProgressUpdateList]'


class MoodUpdate(Message):
    # __init__
    sim_id: 'int'  # uint64
    mood_key: 'int'  # uint64
    mood_intensity: 'int'  # uint32


class GenderPreferenceUpdate(Message):
    class GenderPreference(IntEnum):
        PREFER_NEITHER: 'GenderPreferenceUpdate.GenderPreference' = 0
        PREFER_GUYS: 'GenderPreferenceUpdate.GenderPreference' = 1
        PREFER_GIRLS: 'GenderPreferenceUpdate.GenderPreference' = 2
        PREFER_BOTH: 'GenderPreferenceUpdate.GenderPreference' = 3

    PREFER_NEITHER = GenderPreference.PREFER_NEITHER
    PREFER_GUYS = GenderPreference.PREFER_GUYS
    PREFER_GIRLS = GenderPreference.PREFER_GIRLS
    PREFER_BOTH = GenderPreference.PREFER_BOTH

    # __init__
    sim_id: 'int'  # uint64
    gender_preference: 'GenderPreferenceUpdate.GenderPreference'


class RankedStatisticProgressUpdate(Message):
    # __init__
    stat_id: 'int'  # fixed uint64
    change_rate: 'float'  # float32
    rank: 'int'  # uint32
    curr_rank_points: 'int'  # uint32
    is_rank_change: 'bool'


class RankedStatisticRankChangedUpdate(Message):
    # __init__
    stat_id: 'int'  # uint64
    previous_rank: 'int'  # uint32
    current_rank: 'int'  # uint32


class LifeSkillUpdate(Message):
    # __init__
    sim_id: 'int'  # uint64
    life_skill_id: 'int'  # uint64
    curr_value: 'float'  # float32
    rate_of_change: 'float'  # float32
    is_from_add: 'bool'


class LifeSkillDelete(Message):
    # __init__
    sim_id: 'int'  # uint64
    life_skill_id: 'int'  # uint64


class CooldownVisualEffectToggle(Message):
    # __init__
    sim_id: 'int'  # uint64
    cooldown_visual_effect_active: 'bool'
    edge_color_multiplier: 'float'  # float32
