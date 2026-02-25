from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer

from protocolbuffers.ResourceKey_pb2 import *
from protocolbuffers.S4Common_pb2 import *
from protocolbuffers.Localization_pb2 import *


class KingdomSimData(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    level: 'int'  # uint32
    priority: 'int'  # uint32
    inheriting_sim_id: 'int'  # fixed uint64


class KingdomSimCareerLevel(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    level: 'int'  # uint32


class KingdomDecree(Message):
    # __init__
    decree_type: 'int'  # fixed uint64
    icon_key: 'ResourceKey'
    title_key: 'LocalizedString'
    subtitle_key: 'LocalizedString'
    description_key: 'LocalizedString'
    gameplay_descriptions: 'RepeatedCompositeFieldContainer[LocalizedString]'


class KingdomTitle(Message):
    # __init__
    level: 'int'  # uint32
    priority: 'int'  # uint32
    male_title: 'str'
    female_title: 'str'
    neutral_title: 'str'


class KingdomNeighborhoodData(Message):
    # __init__
    neighborhood_id: 'int'  # fixed uint64
    sims: 'RepeatedCompositeFieldContainer[KingdomSimData]'
    enacted_decrees: 'RepeatedCompositeFieldContainer[KingdomDecree]'
    titles: 'RepeatedCompositeFieldContainer[KingdomTitle]'
    tax_level: 'int'  # uint32


class KingdomUpdatedSims(Message):
    # __init__
    added_sim_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    removed_sim_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    updated_sim_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class KingdomRequestDefaultPronouns(Message):
    # __init__


class KingdomRequestDefaultGenderPronouns(Message):
    # __init__
    gender: 'int'  # uint32
    packed_pronouns: 'str'


class KingdomRequestDefaultPronounsResponse(Message):
    # __init__
    gender_pronouns: 'RepeatedCompositeFieldContainer[KingdomRequestDefaultGenderPronouns]'
    empty_pronouns: 'str'


class KingdomUpdatedTitles(Message):
    # __init__
    neighborhood_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    titles: 'RepeatedCompositeFieldContainer[KingdomTitle]'


class AvailableTitles(Message):
    # __init__
    neighborhood_id: 'int'  # fixed uint64
    dead_sim_id: 'int'  # fixed uint64
    career_level: 'int'  # uint32
    candidate_sim_id: 'int'  # fixed uint64


class KingdomUpdate(Message):
    # __init__
    neighborhoods: 'RepeatedCompositeFieldContainer[KingdomNeighborhoodData]'
    sim_career_levels: 'RepeatedCompositeFieldContainer[KingdomSimCareerLevel]'
    affected_sim_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class KingdomSimVirtualNeighborhood(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    neighborhood_id: 'int'  # fixed uint64


class PersistableKingdomService(Message):
    # __init__
    neighborhoods: 'RepeatedCompositeFieldContainer[KingdomNeighborhoodData]'
    updated_sims: 'KingdomUpdatedSims'
    available_titles: 'RepeatedCompositeFieldContainer[AvailableTitles]'
    sim_career_levels: 'RepeatedCompositeFieldContainer[KingdomSimCareerLevel]'
    sim_virtual_neighborhoods: 'RepeatedCompositeFieldContainer[KingdomSimVirtualNeighborhood]'
    affected_sim_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    default_pronouns: 'KingdomRequestDefaultPronounsResponse'
