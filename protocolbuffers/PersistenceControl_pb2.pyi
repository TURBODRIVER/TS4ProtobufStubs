from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer

from protocolbuffers.Consts_pb2 import *
from protocolbuffers.FileSerialization_pb2 import *
from protocolbuffers.SimObjectAttributes_pb2 import *
from protocolbuffers.GameplaySaveData_pb2 import *
from protocolbuffers.Kingdom_pb2 import *


class CASInfoDataFragment(Message):
    # __init__
    save_slot: 'SaveSlotData'
    households: 'RepeatedCompositeFieldContainer[HouseholdData]'
    sims: 'RepeatedCompositeFieldContainer[SimData]'
    mannequins: 'RepeatedCompositeFieldContainer[MannequinSimData]'
    relgraph: 'SimRelationshipGraphData'
    custom_colors: 'PlayerCustomColors'
    account_nucleus_id: 'int'  # fixed uint64


class TutorialDataFragment(Message):
    # __init__
    tutorial_tips: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    tutorial_mode: 'int'  # int32


class NeighborhoodInfoCacheFragment(Message):
    # __init__
    save_game_data_guid: 'int'  # uint32
    object_fallbacks: 'ObjectFallbackDataList'
    gameplay_data: 'GameplaySaveSlotData'
    zones: 'RepeatedCompositeFieldContainer[ZoneData]'
    neighborhoods: 'RepeatedCompositeFieldContainer[NeighborhoodData]'
    kingdom_service: 'PersistableKingdomService'


class SimDataFragment(Message):
    # __init__
    sims: 'RepeatedCompositeFieldContainer[SimData]'


class ZonesDataFragment(Message):
    # __init__
    zones: 'RepeatedCompositeFieldContainer[ZoneData]'


class PersistenceControlMessageData(Message):
    # __init__
    slot_meta_data: 'RepeatedCompositeFieldContainer[SaveGameSlotMetaData]'
    save_data: 'SaveGameData'
    zone_object_data: 'RepeatedCompositeFieldContainer[ZoneObjectData]'
    errors: 'FeedbackContext'
    scratch_path: 'RepeatedCompositeFieldContainer[ZoneObjectDataScratchPair]'
    world_game_time_fragment: 'int'  # uint64
    accout_data_fragment: 'AccountData'
    protected_households_story_progression_rule_set_fragment: 'StoryProgressionRuleSet'
    unprotected_households_story_progression_rule_set_fragment: 'StoryProgressionRuleSet'
    cas_info_data_fragment: 'CASInfoDataFragment'
    tutorial_data_fragment: 'TutorialDataFragment'
    neighborhood_data_fragment: 'NeighborhoodDataMessage'
    neighborhood_info_cache_fragment: 'NeighborhoodInfoCacheFragment'
    sim_data_fragment: 'SimDataFragment'
    zones_data_fragment: 'ZonesDataFragment'


class PersistenceControlMessage(Message):
    # __init__
    callback: 'int'  # uint64
    userdata: 'int'  # uint64
    opcode: 'PersistenceOpTypes'
    data: 'PersistenceControlMessageData'
