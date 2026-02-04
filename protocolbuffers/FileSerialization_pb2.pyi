from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer
from enum import IntEnum

from protocolbuffers.GameplaySaveData_pb2 import *
from protocolbuffers.SituationPersistence_pb2 import *
from protocolbuffers.SimObjectAttributes_pb2 import *
from protocolbuffers.UI_pb2 import *
from protocolbuffers.Dialog_pb2 import *
from protocolbuffers.Math_pb2 import *
from protocolbuffers.ResourceKey_pb2 import *
from protocolbuffers.SimsCustomOptions_pb2 import *
from protocolbuffers.Outfits_pb2 import *
from protocolbuffers.S4Common_pb2 import *
from protocolbuffers.Venue_pb2 import *
from protocolbuffers.Consts_pb2 import *
from protocolbuffers.CustomSchedule_pb2 import *
from protocolbuffers.Kingdom_pb2 import *


class PersistenceActions(IntEnum):
    BASE_ACTION: 'PersistenceActions' = 0
    LOG_ACTION: 'PersistenceActions' = 1
    COMPOSITE_ACTION: 'PersistenceActions' = 2
    GENERIC_ACTION_BINARY_STORE: 'PersistenceActions' = 3
    GENERIC_ACTION_BINARY_LOAD: 'PersistenceActions' = 4
    GENERIC_ACTION_LOCAL_BINARY_LOAD: 'PersistenceActions' = 5
    GENERIC_ACTION_LOCAL_TEXT_LOAD: 'PersistenceActions' = 6
    GENERIC_ACTION_FILE_RENAME: 'PersistenceActions' = 7
    GENERIC_ACTION_FILE_DELETE: 'PersistenceActions' = 8
    GENERIC_ACTION_FILE_EDIT: 'PersistenceActions' = 9
    GENERIC_ACTION_SLOT_NEW: 'PersistenceActions' = 10
    GENERIC_ACTION_SLOT_COPY: 'PersistenceActions' = 11
    GENERIC_ACTION_SLOT_DELETE: 'PersistenceActions' = 12
    GENERIC_ACTION_SLOT_RENAME: 'PersistenceActions' = 13
    GENERIC_ACTION_LIST_SLOTS: 'PersistenceActions' = 14
    GENERIC_ACTION_OP_BEGIN: 'PersistenceActions' = 15
    GENERIC_ACTION_OP_END: 'PersistenceActions' = 16
    MOCKACTIONUINT: 'PersistenceActions' = 17
    MOCKACTIONFLOAT: 'PersistenceActions' = 18


BASE_ACTION = PersistenceActions.BASE_ACTION
LOG_ACTION = PersistenceActions.LOG_ACTION
COMPOSITE_ACTION = PersistenceActions.COMPOSITE_ACTION
GENERIC_ACTION_BINARY_STORE = PersistenceActions.GENERIC_ACTION_BINARY_STORE
GENERIC_ACTION_BINARY_LOAD = PersistenceActions.GENERIC_ACTION_BINARY_LOAD
GENERIC_ACTION_LOCAL_BINARY_LOAD = PersistenceActions.GENERIC_ACTION_LOCAL_BINARY_LOAD
GENERIC_ACTION_LOCAL_TEXT_LOAD = PersistenceActions.GENERIC_ACTION_LOCAL_TEXT_LOAD
GENERIC_ACTION_FILE_RENAME = PersistenceActions.GENERIC_ACTION_FILE_RENAME
GENERIC_ACTION_FILE_DELETE = PersistenceActions.GENERIC_ACTION_FILE_DELETE
GENERIC_ACTION_FILE_EDIT = PersistenceActions.GENERIC_ACTION_FILE_EDIT
GENERIC_ACTION_SLOT_NEW = PersistenceActions.GENERIC_ACTION_SLOT_NEW
GENERIC_ACTION_SLOT_COPY = PersistenceActions.GENERIC_ACTION_SLOT_COPY
GENERIC_ACTION_SLOT_DELETE = PersistenceActions.GENERIC_ACTION_SLOT_DELETE
GENERIC_ACTION_SLOT_RENAME = PersistenceActions.GENERIC_ACTION_SLOT_RENAME
GENERIC_ACTION_LIST_SLOTS = PersistenceActions.GENERIC_ACTION_LIST_SLOTS
GENERIC_ACTION_OP_BEGIN = PersistenceActions.GENERIC_ACTION_OP_BEGIN
GENERIC_ACTION_OP_END = PersistenceActions.GENERIC_ACTION_OP_END
MOCKACTIONUINT = PersistenceActions.MOCKACTIONUINT
MOCKACTIONFLOAT = PersistenceActions.MOCKACTIONFLOAT


class ActionOperationType(IntEnum):
    ACTION_READ: 'ActionOperationType' = 0
    ACTION_WRITE: 'ActionOperationType' = 1
    ACTION_FLUSH: 'ActionOperationType' = 2


ACTION_READ = ActionOperationType.ACTION_READ
ACTION_WRITE = ActionOperationType.ACTION_WRITE
ACTION_FLUSH = ActionOperationType.ACTION_FLUSH


class ActionErrorType(IntEnum):
    FILE_ERROR_TYPE_NONE: 'ActionErrorType' = 0
    FILE_ERROR_TYPE_SLOT_SAVE: 'ActionErrorType' = 1127087018
    FILE_ERROR_TYPE_SLOT_COPY: 'ActionErrorType' = 1652429822
    FILE_ERROR_TYPE_SLOT_LOAD: 'ActionErrorType' = 650303489


FILE_ERROR_TYPE_NONE = ActionErrorType.FILE_ERROR_TYPE_NONE
FILE_ERROR_TYPE_SLOT_SAVE = ActionErrorType.FILE_ERROR_TYPE_SLOT_SAVE
FILE_ERROR_TYPE_SLOT_COPY = ActionErrorType.FILE_ERROR_TYPE_SLOT_COPY
FILE_ERROR_TYPE_SLOT_LOAD = ActionErrorType.FILE_ERROR_TYPE_SLOT_LOAD


class ActionResponseCodes(IntEnum):
    ACTION_NOT_INITIALIZED: 'ActionResponseCodes' = 0
    ACTION_SUCCESS: 'ActionResponseCodes' = 1
    ACTION_FAILED: 'ActionResponseCodes' = 2


ACTION_NOT_INITIALIZED = ActionResponseCodes.ACTION_NOT_INITIALIZED
ACTION_SUCCESS = ActionResponseCodes.ACTION_SUCCESS
ACTION_FAILED = ActionResponseCodes.ACTION_FAILED


class ActionFailureCodes(IntEnum):
    AFC_NONE: 'ActionFailureCodes' = 0
    AFC_FILESYSTEM_MISSING: 'ActionFailureCodes' = 1
    AFC_SYSTEM_SHUTDOWN: 'ActionFailureCodes' = 2
    AFC_SYSTEM_FAILURE: 'ActionFailureCodes' = 3
    AFC_SYSTEM_DISK_FULL: 'ActionFailureCodes' = 4
    AFC_FILE_NOT_FOUND: 'ActionFailureCodes' = 10
    AFC_FILE_DENIED: 'ActionFailureCodes' = 11
    AFC_FILE_OPEN_FAILED: 'ActionFailureCodes' = 12
    AFC_FILE_READ_FAILED: 'ActionFailureCodes' = 13
    AFC_FILE_WRITE_FAILED: 'ActionFailureCodes' = 14
    AFC_FILE_NOT_FULLY_READ: 'ActionFailureCodes' = 15
    AFC_FILE_SIZE_ZERO: 'ActionFailureCodes' = 16
    AFC_FILE_SIZE_MAX: 'ActionFailureCodes' = 17
    AFC_FILE_REMOVE_FAILED: 'ActionFailureCodes' = 20
    AFC_FILE_MOVE_FAILED: 'ActionFailureCodes' = 21
    AFC_FILE_COPY_FAILED: 'ActionFailureCodes' = 22
    AFC_FILE_CREATE_VERSION_NAME_FAILED: 'ActionFailureCodes' = 23
    AFC_SLOT_GET_NAME_FAILED: 'ActionFailureCodes' = 30
    AFC_SLOT_SET_NAME_FAILED: 'ActionFailureCodes' = 31
    AFC_SLOT_GET_GUID_FAILED: 'ActionFailureCodes' = 32
    AFC_SLOT_SET_GUID_FAILED: 'ActionFailureCodes' = 33
    AFC_SLOT_GET_KEY_FAILED: 'ActionFailureCodes' = 34
    AFC_NO_ACCOUNT: 'ActionFailureCodes' = 40
    AFC_SYSTEM_OS_HANDLED_ERROR: 'ActionFailureCodes' = 50


AFC_NONE = ActionFailureCodes.AFC_NONE
AFC_FILESYSTEM_MISSING = ActionFailureCodes.AFC_FILESYSTEM_MISSING
AFC_SYSTEM_SHUTDOWN = ActionFailureCodes.AFC_SYSTEM_SHUTDOWN
AFC_SYSTEM_FAILURE = ActionFailureCodes.AFC_SYSTEM_FAILURE
AFC_SYSTEM_DISK_FULL = ActionFailureCodes.AFC_SYSTEM_DISK_FULL
AFC_FILE_NOT_FOUND = ActionFailureCodes.AFC_FILE_NOT_FOUND
AFC_FILE_DENIED = ActionFailureCodes.AFC_FILE_DENIED
AFC_FILE_OPEN_FAILED = ActionFailureCodes.AFC_FILE_OPEN_FAILED
AFC_FILE_READ_FAILED = ActionFailureCodes.AFC_FILE_READ_FAILED
AFC_FILE_WRITE_FAILED = ActionFailureCodes.AFC_FILE_WRITE_FAILED
AFC_FILE_NOT_FULLY_READ = ActionFailureCodes.AFC_FILE_NOT_FULLY_READ
AFC_FILE_SIZE_ZERO = ActionFailureCodes.AFC_FILE_SIZE_ZERO
AFC_FILE_SIZE_MAX = ActionFailureCodes.AFC_FILE_SIZE_MAX
AFC_FILE_REMOVE_FAILED = ActionFailureCodes.AFC_FILE_REMOVE_FAILED
AFC_FILE_MOVE_FAILED = ActionFailureCodes.AFC_FILE_MOVE_FAILED
AFC_FILE_COPY_FAILED = ActionFailureCodes.AFC_FILE_COPY_FAILED
AFC_FILE_CREATE_VERSION_NAME_FAILED = ActionFailureCodes.AFC_FILE_CREATE_VERSION_NAME_FAILED
AFC_SLOT_GET_NAME_FAILED = ActionFailureCodes.AFC_SLOT_GET_NAME_FAILED
AFC_SLOT_SET_NAME_FAILED = ActionFailureCodes.AFC_SLOT_SET_NAME_FAILED
AFC_SLOT_GET_GUID_FAILED = ActionFailureCodes.AFC_SLOT_GET_GUID_FAILED
AFC_SLOT_SET_GUID_FAILED = ActionFailureCodes.AFC_SLOT_SET_GUID_FAILED
AFC_SLOT_GET_KEY_FAILED = ActionFailureCodes.AFC_SLOT_GET_KEY_FAILED
AFC_NO_ACCOUNT = ActionFailureCodes.AFC_NO_ACCOUNT
AFC_SYSTEM_OS_HANDLED_ERROR = ActionFailureCodes.AFC_SYSTEM_OS_HANDLED_ERROR


class EntitlementData(Message):
    # __init__
    transaction_id: 'int'  # uint64
    payload: 'bytes'
    initiation_time: 'int'  # uint64
    completion_time: 'int'  # uint64


class GameContentData(Message):
    # __init__
    required_pack_ids: 'RepeatedCompositeFieldContainer[int]'  # uint32
    cds_patch_base_changelists: 'RepeatedCompositeFieldContainer[int]'  # uint32
    cds_content_patch_mounted: 'bool'
    saved_by_feature_preview_build: 'bool'


class UiOptionsData(Message):
    # __init__
    is_new_game: 'bool'
    was_notification_alert_shown: 'bool'


class AccountData(Message):
    # __init__
    nucleus_id: 'int'  # fixed uint64
    persona_name: 'str'
    email: 'str'
    created: 'int'  # uint64
    last_login: 'int'  # uint64
    entitlements: 'RepeatedCompositeFieldContainer[EntitlementData]'
    ui_options: 'UiOptionsData'
    client_version: 'str'
    save_slot_id: 'int'  # fixed uint64
    gameplay_account_data: 'GameplayAccountData'
    game_notification: 'RepeatedCompositeFieldContainer[UiDialogMessage]'
    client_version_at_creation: 'str'
    number_of_saves: 'int'  # uint64
    number_of_saves_mods: 'int'  # uint64
    number_of_saves_script_mods: 'int'  # uint64
    is_pack_usage_telemetry_version: 'bool'


class NotificationSaveData(Message):
    # __init__
    game_notification: 'RepeatedCompositeFieldContainer[UiDialogMessage]'


class SaveSlotData(Message):
    # __init__
    slot_id: 'int'  # fixed uint64
    neighboorhoods: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    last_neighborhood: 'int'  # fixed uint64
    zones: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    last_zone: 'int'  # fixed uint64
    households: 'IdList'
    is_migrated: 'bool'
    gameplay_data: 'GameplaySaveSlotData'
    slot_name: 'str'
    timestamp: 'int'  # uint64
    active_household_id: 'int'  # uint64
    nucleus_id: 'int'  # fixed uint64
    s4_guid_seed: 'int'  # fixed uint64
    compatibility_version: 'int'  # uint32
    trigger_tutorial_drama_node: 'bool'
    tutorial_mode: 'int'  # int32
    game_content_data: 'GameContentData'
    applied_aging_fixup: 'bool'
    kingdom_service: 'PersistableKingdomService'


class SaveSlotDataDescOnly(Message):
    # __init__
    slot_id: 'int'  # fixed uint64
    slot_name: 'str'
    timestamp: 'int'  # uint64
    active_household_id: 'int'  # uint64
    compatibility_version: 'int'  # uint32
    game_content_data: 'GameContentData'


class SaveListData(Message):
    # __init__
    nucleus_id: 'int'  # fixed uint64
    slot_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class LotCoord(Message):
    # __init__
    x: 'float'  # float32
    y: 'float'  # float32
    z: 'float'  # float32
    rot_x: 'float'  # float32
    rot_y: 'float'  # float32
    rot_z: 'float'  # float32
    rot_w: 'float'  # float32


class ObjectData(Message):
    # __init__
    object_id: 'int'  # fixed uint64
    owner_id: 'int'  # fixed uint64
    parent_id: 'int'  # fixed uint64
    slot_id: 'int'  # uint32
    position: 'LotCoord'
    loc_type: 'int'  # uint32
    container_id: 'int'  # fixed uint64
    type: 'int'  # uint32
    level: 'int'  # int32
    scale: 'float'  # float32
    state_index: 'int'  # uint32
    attributes: 'bytes'
    cost: 'int'  # uint32
    baby_sim_id: 'int'  # fixed uint64
    ui_metadata: 'UiObjectMetadata'
    has_been_depreciated: 'bool'
    needs_depreciation: 'bool'
    created_from_lot_template: 'bool'
    is_new: 'bool'
    texture_id: 'int'  # fixed uint64
    material_variant: 'int'  # uint32
    stack_sort_order: 'int'  # uint32
    light_color: 'Vector3'
    material_state: 'int'  # uint32
    geometry_state: 'int'  # uint32
    object_parent_type: 'int'  # uint32
    encoded_parent_location: 'int'  # uint64
    light_dimmer_value: 'float'  # float32
    model_override_resource_key: 'ResourceKey'
    guid: 'int'  # uint64
    unique_inventory: 'ObjectList'
    needs_post_bb_fixup: 'bool'
    buildbuy_use_flags: 'int'  # uint32
    texture_effect: 'int'  # uint32
    multicolor: 'RepeatedCompositeFieldContainer[Vector3]'
    inventory_plex_id: 'int'  # int32
    is_new_object: 'bool'
    persisted_tags: 'RepeatedCompositeFieldContainer[int]'  # uint32
    canvas_state_type: 'IconInfo.CanvasStateType'


class ObjectList(Message):
    # __init__
    objects: 'RepeatedCompositeFieldContainer[ObjectData]'


class ObjectFallbackData(Message):
    # __init__
    guid: 'int'  # uint64
    fallback_guid: 'int'  # uint64


class ObjectFallbackDataList(Message):
    # __init__
    fallbacks: 'RepeatedCompositeFieldContainer[ObjectFallbackData]'


class ZoneData(Message):
    # __init__
    zone_id: 'int'  # fixed uint64
    name: 'str'
    world_id: 'int'  # uint32
    lot_id: 'int'  # uint32
    lot_template_id: 'int'  # uint32
    household_id: 'int'  # fixed uint64
    nucleus_id: 'int'  # fixed uint64
    permissions: 'int'  # uint32
    neighborhood_id: 'int'  # fixed uint64
    gameplay_zone_data: 'GameplayZoneData'
    lot_description_id: 'int'  # fixed uint64
    front_door_id: 'int'  # fixed uint64
    description: 'str'
    spawn_point_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    bedroom_count: 'int'  # uint32
    bathroom_count: 'int'  # uint32
    active_plex: 'int'  # uint32
    master_zone_object_data_id: 'int'  # fixed uint64
    lot_traits: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    pending_house_desc_id: 'int'  # uint32
    university_housing_configuration: 'UniversityHousingConfiguration'
    pending_plex_exterior_house_desc_id: 'int'  # uint32
    custom_schedule: 'CustomSchedule'


class ZoneObjectData(Message):
    # __init__
    zone_id: 'int'  # fixed uint64
    architecture_data: 'RepeatedCompositeFieldContainer[bytes]'
    objects: 'RepeatedCompositeFieldContainer[ObjectList]'
    sub_venue_keys: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    active_data_index: 'int'  # int32
    is_modified_from_lot_template: 'bool'


class ZoneObjectDataScratchPair(Message):
    # __init__
    zone_id: 'int'  # fixed uint64
    zone_object_data_scratch_path: 'str'


class SituationConditionalLayerData(Message):
    # __init__
    layer_guid: 'int'  # fixed uint64
    situation_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class OpenStreetsData(Message):
    # __init__
    world_id: 'int'  # uint64
    nbh_id: 'int'  # uint64
    objects: 'ObjectList'
    situation_seeds: 'RepeatedCompositeFieldContainer[SituationSeedData]'
    active_household_id_on_save: 'int'  # fixed uint64
    active_zone_id_on_save: 'int'  # fixed uint64
    sim_time_on_save: 'int'  # uint64
    open_street_director: 'OpenStreetDirectorData'
    conditional_layer_service: 'ConditionalLayerServiceData'
    ambient_service: 'AmbientServiceData'
    situation_conditional_layers: 'RepeatedCompositeFieldContainer[SituationConditionalLayerData]'


class SteadySimIdList(Message):
    # __init__
    sim_id: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class SimData(Message):
    class SimCreationPath(IntEnum):
        SIMCREATION_NONE: 'SimData.SimCreationPath' = 0
        SIMCREATION_INIT: 'SimData.SimCreationPath' = 1
        SIMCREATION_REENTRY_ADDSIM: 'SimData.SimCreationPath' = 2
        SIMCREATION_GALLERY: 'SimData.SimCreationPath' = 3
        SIMCREATION_PRE_MADE: 'SimData.SimCreationPath' = 4
        SIMCREATION_CLONED: 'SimData.SimCreationPath' = 5

    SIMCREATION_NONE = SimCreationPath.SIMCREATION_NONE
    SIMCREATION_INIT = SimCreationPath.SIMCREATION_INIT
    SIMCREATION_REENTRY_ADDSIM = SimCreationPath.SIMCREATION_REENTRY_ADDSIM
    SIMCREATION_GALLERY = SimCreationPath.SIMCREATION_GALLERY
    SIMCREATION_PRE_MADE = SimCreationPath.SIMCREATION_PRE_MADE
    SIMCREATION_CLONED = SimCreationPath.SIMCREATION_CLONED

    # __init__
    sim_id: 'int'  # fixed uint64
    zone_id: 'int'  # fixed uint64
    world_id: 'int'  # uint32
    zone_name: 'str'
    household_id: 'int'  # fixed uint64
    first_name: 'str'
    last_name: 'str'
    gender: 'int'  # uint32
    age: 'int'  # uint32
    voice_pitch: 'float'  # float32
    skin_tone: 'int'  # uint64
    voice_actor: 'int'  # uint32
    physique: 'str'
    age_progress: 'float'  # float32
    significant_other: 'int'  # fixed uint64
    deprecated_attributes: 'bytes'
    facial_attr: 'bytes'
    created: 'int'  # uint64
    inventory: 'ObjectList'
    outfits: 'OutfitList'
    household_name: 'str'
    nucleus_id: 'int'  # fixed uint64
    deprecated_money: 'int'  # uint32
    money: 'int'  # uint64
    genetic_data: 'GeneticData'
    flags: 'int'  # uint32
    attributes: 'PersistableSimInfoAttributes'
    revision: 'int'  # uint32
    location: 'LotCoord'
    deprecated_change_number: 'int'  # uint32
    primary_aspiration: 'int'  # uint64
    last_instantiated_time: 'int'  # uint64
    additional_bonus_days: 'int'  # uint64
    interaction_state: 'SuperInteractionSaveState'
    current_outfit_type: 'int'  # uint32
    current_outfit_index: 'int'  # uint32
    fix_relationship: 'bool'
    current_mood: 'int'  # fixed uint64
    current_mood_intensity: 'int'  # uint32
    zone_time_stamp: 'ZoneTimeStamp'
    whim_bucks: 'int'  # uint32
    level: 'int'  # uint32
    inventory_value: 'int'  # uint64
    gameplay_data: 'GameplaySimData'
    pregnancy_progress: 'float'  # float32
    full_name_key: 'int'  # uint32
    last_inzone_outfit_type: 'int'  # uint32
    last_inzone_outfit_index: 'int'  # uint32
    sim_creation_path: 'SimData.SimCreationPath'
    initial_fitness_value: 'float'  # float32
    voice_effect: 'int'  # uint64
    first_name_key: 'int'  # uint32
    last_name_key: 'int'  # uint32
    generation: 'int'  # uint32
    previous_outfit_type: 'int'  # uint32
    previous_outfit_index: 'int'  # uint32
    extended_species: 'int'  # uint32
    sim_lod: 'int'  # uint32
    custom_texture: 'int'  # uint64
    pelt_layers: 'PeltLayerDataList'
    breed_name: 'str'
    breed_name_key: 'int'  # uint32
    age_progress_randomized: 'bool'
    skin_tone_val_shift: 'float'  # float32
    fiance: 'int'  # fixed uint64
    pronouns: 'SimPronounList'
    fix_traits_knowledge: 'bool'
    needs_age_progress_randomized: 'bool'
    steadies: 'SteadySimIdList'
    ghost_base_color: 'int'  # uint32
    ghost_edge_color: 'int'  # uint32
    parts_custom_tattoos: 'RepeatedCompositeFieldContainer[SimPartCustomTattooData]'
    parts_creator_data: 'RepeatedCompositeFieldContainer[SimPartCreatorData]'


class SimList(Message):
    # __init__
    sims: 'RepeatedCompositeFieldContainer[SimData]'


class RewardPartData(Message):
    # __init__
    part_id: 'int'  # uint64
    is_new_reward: 'bool'
    sim_id: 'int'  # uint64
    reward_part_type: 'int'  # uint32


class RewardPartList(Message):
    # __init__
    reward_parts: 'RepeatedCompositeFieldContainer[RewardPartData]'


class HouseholdDataDescOnly(Message):
    # __init__
    household_id: 'int'  # fixed uint64
    name: 'str'
    scenario_data: 'ScenarioDataDescOnly'


class SimRolePair(Message):
    # __init__
    sim_id: 'int'  # uint64
    role_id: 'int'  # uint64


class ScenarioDataDescOnly(Message):
    # __init__
    scenario_id: 'int'  # uint64


class ScenarioData(Message):
    # __init__
    scenario_id: 'int'  # uint64
    sim_role_pairs: 'RepeatedCompositeFieldContainer[SimRolePair]'
    instance_id: 'int'  # uint64
    scenario_entry_method: 'int'  # uint32


class HouseholdData(Message):
    # __init__
    account_id: 'int'  # fixed uint64
    household_id: 'int'  # fixed uint64
    name: 'str'
    home_zone: 'int'  # fixed uint64
    money: 'int'  # uint64
    inventory: 'ObjectList'
    last_played_sim_id: 'int'  # fixed uint64
    creation_time: 'int'  # uint64
    sims: 'IdList'
    owned_lots: 'IdList'
    instanced_object_count: 'int'  # uint32
    revision: 'int'  # uint32
    gameplay_data: 'GameplayHouseholdData'
    cas_inventory: 'RepeatedCompositeFieldContainer[int]'  # uint64
    description: 'str'
    last_modified_time: 'int'  # uint64
    creator_id: 'int'  # fixed uint64
    creator_name: 'str'
    creator_uuid: 'bytes'
    modifier_id: 'int'  # fixed uint64
    modifier_name: 'str'
    reward_inventory: 'RewardPartList'
    hidden: 'bool'
    cheats_enabled: 'bool'
    needs_welcome_wagon: 'bool'
    premade_household_id: 'int'  # uint64
    pending_urnstones: 'IdList'
    is_unplayed: 'bool'
    is_player: 'bool'
    premade_household_template_id: 'int'  # fixed uint64
    scenario_data: 'ScenarioData'
    story_progression_rule_set: 'StoryProgressionRuleSet'
    dependent: 'bool'


class HouseholdAccountPair(Message):
    # __init__
    nucleus_id: 'int'  # fixed uint64
    persona_name: 'str'
    household_id: 'int'  # uint64
    household_name: 'str'
    is_npc: 'bool'


class LotTraitUpdateInfo(Message):
    # __init__
    lot_traits: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    lot_owner_info: 'LotOwnerInfo'


class SubVenueInfo(Message):
    # __init__
    sub_venue_key: 'int'  # fixed uint64
    sub_venue_eligible: 'bool'
    sub_venue_lot_traits: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class LotOwnerInfo(Message):
    # __init__
    lot_description_id: 'int'  # uint64
    zone_instance_id: 'int'  # fixed uint64
    lot_name: 'str'
    lot_owner: 'RepeatedCompositeFieldContainer[HouseholdAccountPair]'
    lot_template_id: 'int'  # uint32
    venue_key: 'int'  # fixed uint64
    venue_eligible: 'bool'
    lot_description: 'str'
    venue_tier: 'int'  # int32
    eco_footprint_state: 'EcoFootprintStateType'
    sub_venue_infos: 'RepeatedCompositeFieldContainer[SubVenueInfo]'


class TravelGroupData(Message):
    class GroupType(IntEnum):
        GROUPTYPE_VACATION: 'TravelGroupData.GroupType' = 0
        GROUPTYPE_STAYOVER: 'TravelGroupData.GroupType' = 1
        GROUPTYPE_GETAWAY: 'TravelGroupData.GroupType' = 2

    GROUPTYPE_VACATION = GroupType.GROUPTYPE_VACATION
    GROUPTYPE_STAYOVER = GroupType.GROUPTYPE_STAYOVER
    GROUPTYPE_GETAWAY = GroupType.GROUPTYPE_GETAWAY

    # __init__
    travel_group_id: 'int'  # fixed uint64
    household_sim_ids: 'RepeatedCompositeFieldContainer[HouseholdSimIds]'
    zone_id: 'int'  # fixed uint64
    played: 'bool'
    create_time: 'int'  # uint64
    end_time: 'int'  # uint64
    object_preference_tracker: 'ObjectPreferenceTracker'
    group_type: 'TravelGroupData.GroupType'
    situation_id: 'int'  # uint64
    claimed_object_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    initiating_sim_id: 'int'  # uint64
    lot_value: 'int'  # uint32
    custom_data: 'bytes'


class TravelGroupList(Message):
    # __init__
    travel_groups: 'RepeatedCompositeFieldContainer[TravelGroupData]'


class ObjectCleanUpData(Message):
    # __init__
    zone_id: 'int'  # fixed uint64
    world_id: 'int'  # fixed uint64
    object_data: 'ObjectData'


class GameplayDestinationCleanUpData(Message):
    # __init__
    household_id: 'int'  # fixed uint64
    travel_group_id: 'int'  # fixed uint64
    object_clean_up_data_list: 'RepeatedCompositeFieldContainer[ObjectCleanUpData]'


class StreetInfoData(Message):
    # __init__
    world_id: 'int'  # fixed uint64
    map_overlays: 'RepeatedCompositeFieldContainer[int]'  # uint32
    eco_footprint_state: 'EcoFootprintStateType'
    normalized_eco_footprint_state_progress: 'float'  # float32
    eco_footprint_delta: 'float'  # float32


class NeighborhoodData(Message):
    # __init__
    neighborhood_id: 'int'  # fixed uint64
    owner_id: 'int'  # fixed uint64
    name: 'str'
    region_id: 'int'  # uint64
    lots: 'RepeatedCompositeFieldContainer[LotOwnerInfo]'
    permissions: 'int'  # uint32
    households: 'RepeatedCompositeFieldContainer[HouseholdAccountPair]'
    npc_households: 'RepeatedCompositeFieldContainer[HouseholdAccountPair]'
    gameplay_data: 'GameplayNeighborhoodData'
    description: 'str'
    bedroom_count: 'int'  # uint32
    bathroom_count: 'int'  # uint32
    street_data: 'RepeatedCompositeFieldContainer[StreetInfoData]'


class NeighborhoodDataMessage(Message):
    # __init__
    neighborhoods: 'RepeatedCompositeFieldContainer[NeighborhoodData]'
    travel_groups: 'RepeatedCompositeFieldContainer[TravelGroupData]'
    uninstalled_region_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64


class AccountSettingsData(Message):
    # __init__
    data: 'str'


class GameplayData(Message):
    # __init__
    premade_lot_status: 'RepeatedCompositeFieldContainer[PremadeLotStatus]'
    daily_sim_info_creation_count: 'int'  # uint32


class ErrorFeedback(Message):
    # __init__
    failure_code: 'ActionFailureCodes'
    element_name: 'str'
    function: 'str'
    filename: 'str'
    linenumber: 'int'  # uint32
    last_error: 'int'  # uint32
    system_error_code: 'int'  # uint32


class SourceFunctionFileLine(Message):
    # __init__
    function: 'str'
    filename: 'str'
    linenumber: 'int'  # uint32


class FeedbackContext(Message):
    # __init__
    action_response_code: 'int'  # uint32
    error_list: 'RepeatedCompositeFieldContainer[ErrorFeedback]'
    source_action: 'PersistenceActions'
    source_lines: 'RepeatedCompositeFieldContainer[SourceFunctionFileLine]'


class SaveGameSlotMetaData(Message):
    # __init__
    slot_id: 'int'  # uint32
    slot_name: 'str'
    force_override: 'bool'
    include_backups: 'bool'
    timestamp: 'int'  # uint64
    last_household_name: 'str'
    isValid: 'bool'
    scratch_id: 'int'  # int32
    slot_version: 'int'  # int32
    incompatible: 'bool'
    required_pack_ids: 'RepeatedCompositeFieldContainer[int]'  # uint32
    cds_patch_base_changelists: 'RepeatedCompositeFieldContainer[int]'  # uint32
    cds_content_patch_mounted: 'bool'
    scenario_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    saved_by_feature_preview_build: 'bool'


class SaveGameSlotList(Message):
    # __init__
    slots: 'RepeatedCompositeFieldContainer[SaveGameSlotMetaData]'
    allow_incompatible: 'bool'


class PlayerCustomColorList(Message):
    # __init__
    part_id: 'ResourceKey'
    color_shifts: 'RepeatedCompositeFieldContainer[int]'  # uint64


class PlayerCustomColors(Message):
    # __init__
    color_mapping: 'RepeatedCompositeFieldContainer[PlayerCustomColorList]'


class GigObjectInfo(Message):
    # __init__
    obj_id: 'int'  # uint64
    obj_def: 'int'  # uint64


class GigTagCount(Message):
    # __init__
    tag_id: 'int'  # uint64
    tag_count: 'int'  # int32


class GigObjectsTrackingData(Message):
    # __init__
    zone_id: 'int'  # uint64
    tag_counts: 'RepeatedCompositeFieldContainer[GigTagCount]'
    tile_count: 'int'  # int32
    block_ids: 'RepeatedCompositeFieldContainer[int]'  # uint32
    objects: 'RepeatedCompositeFieldContainer[GigObjectInfo]'
    max_level: 'int'  # int32
    min_level: 'int'  # int32


class GigRestrictionsData(Message):
    # __init__
    zone_id: 'int'  # uint64
    level_restricted: 'bool'
    level_limit: 'int'  # int32
    tile_limit: 'int'  # int32


class SaveGameData(Message):
    # __init__
    guid: 'int'  # uint32
    save_slot: 'SaveSlotData'
    account: 'AccountData'
    neighborhoods: 'RepeatedCompositeFieldContainer[NeighborhoodData]'
    households: 'RepeatedCompositeFieldContainer[HouseholdData]'
    sims: 'RepeatedCompositeFieldContainer[SimData]'
    zones: 'RepeatedCompositeFieldContainer[ZoneData]'
    streets: 'RepeatedCompositeFieldContainer[OpenStreetsData]'
    travel_groups: 'RepeatedCompositeFieldContainer[TravelGroupData]'
    uninstalled_region_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    object_fallbacks: 'ObjectFallbackDataList'
    destination_clean_up_data: 'RepeatedCompositeFieldContainer[GameplayDestinationCleanUpData]'
    gameplay_data: 'GameplayData'
    mannequins: 'RepeatedCompositeFieldContainer[MannequinSimData]'
    relgraph: 'SimRelationshipGraphData'
    tutorial_tips: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    sims_removed_from_travel_groups: 'RepeatedCompositeFieldContainer[int]'  # uint64
    custom_colors: 'PlayerCustomColors'
    gig_start_objects_tracking_data: 'RepeatedCompositeFieldContainer[GigObjectsTrackingData]'
    gig_end_objects_tracking_data: 'RepeatedCompositeFieldContainer[GigObjectsTrackingData]'
    gig_restrictions_data: 'RepeatedCompositeFieldContainer[GigRestrictionsData]'
    protected_households_story_progression_rule_set: 'StoryProgressionRuleSet'
    unprotected_households_story_progression_rule_set: 'StoryProgressionRuleSet'


class SaveGameDataDescOnly(Message):
    # __init__
    guid: 'int'  # uint32
    save_slot: 'SaveSlotDataDescOnly'
    households: 'RepeatedCompositeFieldContainer[HouseholdDataDescOnly]'


class GenusData(Message):
    # __init__
    gender: 'int'  # uint32
    age: 'int'  # uint32
    extended_species: 'int'  # uint32
    occult_type: 'int'  # uint32


class SimRelationshipEdge(Message):
    # __init__
    target_node_id: 'int'  # uint64
    edge_data: 'int'  # uint64


class SimRelationshipNode(Message):
    # __init__
    node_id: 'int'  # uint64
    sim_id: 'int'  # uint64
    genus: 'GenusData'
    first_name: 'str'
    last_name: 'str'
    outgoing_edges: 'RepeatedCompositeFieldContainer[SimRelationshipEdge]'


class SimRelationshipGraphData(Message):
    # __init__
    nodes: 'RepeatedCompositeFieldContainer[SimRelationshipNode]'


class StoryProgressionRule(Message):
    # __init__
    rule_id: 'int'  # uint64
    enabled: 'bool'


class StoryProgressionRuleSet(Message):
    # __init__
    rules: 'RepeatedCompositeFieldContainer[StoryProgressionRule]'
    enabled: 'bool'
