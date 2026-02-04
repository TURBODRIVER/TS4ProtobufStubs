from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer
from enum import IntEnum

from protocolbuffers.Loot_pb2 import *
from protocolbuffers.ResourceKey_pb2 import *
from protocolbuffers.Localization_pb2 import *
from protocolbuffers.Math_pb2 import *
from protocolbuffers.S4Common_pb2 import *
from protocolbuffers.UI_pb2 import *
from protocolbuffers.Consts_pb2 import *
from protocolbuffers.FileSerialization_pb2 import *
from protocolbuffers.Commodities_pb2 import *
from protocolbuffers.GameplaySaveData_pb2 import *


class MixerStateTypes(IntEnum):
    MIXER_STATE_AVAILABLE: 'MixerStateTypes' = 0
    MIXER_STATE_PENDING: 'MixerStateTypes' = 1
    MIXER_STATE_ACTIVE: 'MixerStateTypes' = 2
    MIXER_STATE_COOLDOWN: 'MixerStateTypes' = 3
    MIXER_STATE_DISABLED: 'MixerStateTypes' = 4
    MIXER_STATE_PENDING_FAIL: 'MixerStateTypes' = 5


MIXER_STATE_AVAILABLE = MixerStateTypes.MIXER_STATE_AVAILABLE
MIXER_STATE_PENDING = MixerStateTypes.MIXER_STATE_PENDING
MIXER_STATE_ACTIVE = MixerStateTypes.MIXER_STATE_ACTIVE
MIXER_STATE_COOLDOWN = MixerStateTypes.MIXER_STATE_COOLDOWN
MIXER_STATE_DISABLED = MixerStateTypes.MIXER_STATE_DISABLED
MIXER_STATE_PENDING_FAIL = MixerStateTypes.MIXER_STATE_PENDING_FAIL


class LoopingStates(IntEnum):
    NOT_APPLICABLE: 'LoopingStates' = 0
    ENABLED: 'LoopingStates' = 1
    DISABLED: 'LoopingStates' = 2
    DISABLED_LOCKED: 'LoopingStates' = 3


NOT_APPLICABLE = LoopingStates.NOT_APPLICABLE
ENABLED = LoopingStates.ENABLED
DISABLED = LoopingStates.DISABLED
DISABLED_LOCKED = LoopingStates.DISABLED_LOCKED


class Polarity(IntEnum):
    NEUTRAL: 'Polarity' = 0
    NEGATIVE: 'Polarity' = 1
    POSITIVE: 'Polarity' = 2


NEUTRAL = Polarity.NEUTRAL
NEGATIVE = Polarity.NEGATIVE
POSITIVE = Polarity.POSITIVE


class IQ_PipelineStage(IntEnum):
    NONE: 'IQ_PipelineStage' = 0
    QUEUED: 'IQ_PipelineStage' = 1
    PRE_TRANSITIONING: 'IQ_PipelineStage' = 2
    PREPARED: 'IQ_PipelineStage' = 3
    PROCESSING: 'IQ_PipelineStage' = 4
    STAGED: 'IQ_PipelineStage' = 5
    EXITED: 'IQ_PipelineStage' = 6


NONE = IQ_PipelineStage.NONE
QUEUED = IQ_PipelineStage.QUEUED
PRE_TRANSITIONING = IQ_PipelineStage.PRE_TRANSITIONING
PREPARED = IQ_PipelineStage.PREPARED
PROCESSING = IQ_PipelineStage.PROCESSING
STAGED = IQ_PipelineStage.STAGED
EXITED = IQ_PipelineStage.EXITED


class IQ_UI_State(IntEnum):
    IQ_QUEUED: 'IQ_UI_State' = 0
    IQ_TRANSITIONING: 'IQ_UI_State' = 1
    IQ_RUNNING: 'IQ_UI_State' = 2


IQ_QUEUED = IQ_UI_State.IQ_QUEUED
IQ_TRANSITIONING = IQ_UI_State.IQ_TRANSITIONING
IQ_RUNNING = IQ_UI_State.IQ_RUNNING


class BuffProgressArrow(IntEnum):
    BUFF_PROGRESS_NONE: 'BuffProgressArrow' = 0
    BUFF_PROGRESS_UP: 'BuffProgressArrow' = 1
    BUFF_PROGRESS_DOWN: 'BuffProgressArrow' = 2


BUFF_PROGRESS_NONE = BuffProgressArrow.BUFF_PROGRESS_NONE
BUFF_PROGRESS_UP = BuffProgressArrow.BUFF_PROGRESS_UP
BUFF_PROGRESS_DOWN = BuffProgressArrow.BUFF_PROGRESS_DOWN


class MotiveOverlayType(IntEnum):
    INVALID: 'MotiveOverlayType' = 0
    POWER_WARNING: 'MotiveOverlayType' = 1
    IMPACTING_MOTIVE: 'MotiveOverlayType' = 2


INVALID = MotiveOverlayType.INVALID
POWER_WARNING = MotiveOverlayType.POWER_WARNING
IMPACTING_MOTIVE = MotiveOverlayType.IMPACTING_MOTIVE


class UpdateClientSim(Message):
    class PB_Color(IntEnum):
        GREEN: 'UpdateClientSim.PB_Color' = 1
        BLUE: 'UpdateClientSim.PB_Color' = 2

    GREEN = PB_Color.GREEN
    BLUE = PB_Color.BLUE

    # __init__
    id: 'int'  # uint64
    active: 'bool'
    plumbbob_visible: 'bool'
    plumbbob_color: 'UpdateClientSim.PB_Color'


class AspirationTrackerUpdate(Message):
    # __init__
    sim_id: 'int'  # uint64
    aspirations_completed: 'RepeatedCompositeFieldContainer[int]'  # uint64
    objectives_completed: 'RepeatedCompositeFieldContainer[int]'  # uint64
    init_message: 'bool'
    unlocked_hidden_aspiration_tracks: 'RepeatedCompositeFieldContainer[int]'  # uint64
    objectives_reset: 'RepeatedCompositeFieldContainer[int]'  # uint64


class TimedAspirationUpdate(Message):
    class UpdateType(IntEnum):
        ADD: 'TimedAspirationUpdate.UpdateType' = 0
        REMOVE: 'TimedAspirationUpdate.UpdateType' = 1
        OBJECTIVE_UPDATE: 'TimedAspirationUpdate.UpdateType' = 2

    ADD = UpdateType.ADD
    REMOVE = UpdateType.REMOVE
    OBJECTIVE_UPDATE = UpdateType.OBJECTIVE_UPDATE

    # __init__
    update_type: 'TimedAspirationUpdate.UpdateType'
    sim_id: 'int'  # uint64
    timed_aspiration_id: 'int'  # uint64
    timed_aspiration_end_time: 'int'  # uint64
    timed_aspiration_type: 'int'  # uint64
    objectives: 'RepeatedCompositeFieldContainer[int]'  # uint64
    reward_trait_id: 'int'  # uint64


class UnfinishedBusinessAspirationUpdate(Message):
    # __init__
    sim_id: 'int'  # uint64
    objectives: 'RepeatedCompositeFieldContainer[int]'  # uint64
    objectives_completed: 'RepeatedCompositeFieldContainer[int]'  # uint64


class SuggestedAspirationUpdate(Message):
    # __init__
    sim_id: 'int'  # uint64
    visible_suggested_aspiration_list: 'RepeatedCompositeFieldContainer[int]'  # uint64


class GoalsStatusUpdate(Message):
    # __init__
    sim_id: 'int'  # uint64
    goals_updated: 'RepeatedCompositeFieldContainer[int]'  # uint64
    goal_values: 'RepeatedCompositeFieldContainer[int]'  # int64
    goal_objectives: 'RepeatedCompositeFieldContainer[int]'  # int64
    goals_that_are_money: 'RepeatedCompositeFieldContainer[bool]'
    cheats_used: 'bool'
    goals_that_show_progress: 'RepeatedCompositeFieldContainer[bool]'
    goals_with_update_tooltip_in_special_cases: 'RepeatedCompositeFieldContainer[bool]'


class SelectedAspirationUpdate(Message):
    # __init__
    sim_id: 'int'  # uint64
    aspiration_selected: 'int'  # uint64


class SatisfactionReward(Message):
    class REWARD_TYPE(IntEnum):
        MONEY: 'SatisfactionReward.REWARD_TYPE' = 0
        BUFF: 'SatisfactionReward.REWARD_TYPE' = 1
        OBJECT: 'SatisfactionReward.REWARD_TYPE' = 2
        TRAIT: 'SatisfactionReward.REWARD_TYPE' = 3
        CASPART: 'SatisfactionReward.REWARD_TYPE' = 4
        CHILDHOOD_INSPIRATION: 'SatisfactionReward.REWARD_TYPE' = 5

    MONEY = REWARD_TYPE.MONEY
    BUFF = REWARD_TYPE.BUFF
    OBJECT = REWARD_TYPE.OBJECT
    TRAIT = REWARD_TYPE.TRAIT
    CASPART = REWARD_TYPE.CASPART
    CHILDHOOD_INSPIRATION = REWARD_TYPE.CHILDHOOD_INSPIRATION

    # __init__
    reward_id: 'int'  # uint64
    cost: 'int'  # uint32
    affordable: 'bool'
    available: 'bool'
    type: 'SatisfactionReward.REWARD_TYPE'
    unavailable_tooltip: 'LocalizedString'


class SatisfactionRewards(Message):
    # __init__
    sim_id: 'int'  # uint64
    rewards: 'RepeatedCompositeFieldContainer[SatisfactionReward]'


class AccountFamilyData(Message):
    # __init__
    accountid: 'int'  # uint64
    familyid: 'int'  # uint64
    familyname: 'str'
    money: 'int'  # uint64
    dirty: 'bool'
    sim: 'RepeatedCompositeFieldContainer[SimData]'
    responsecode: 'int'  # uint32
    familyzoneid: 'int'  # uint64
    is_npc: 'bool'
    is_new: 'bool'
    description: 'str'
    hashtag_description: 'str'
    inventory: 'ObjectList'
    last_modified_time: 'int'  # uint64
    original_creator_id: 'int'  # uint64
    original_creator_string: 'str'
    original_creator_uuid: 'bytes'
    modifier_id: 'int'  # uint64
    modifier_string: 'str'
    hidden: 'bool'
    reward_inventory: 'RewardPartList'
    starter_ref_id: 'int'  # uint64
    is_player_protected: 'bool'
    pet_removed: 'bool'
    premade_household_template_id: 'int'  # fixed uint64
    original_creator_platform: 'ExchangeItemPlatform'
    original_creator_platform_name: 'str'
    original_creator_platform_id: 'int'  # uint64
    modifier_platform: 'ExchangeItemPlatform'
    modifier_platform_name: 'str'
    modifier_platform_id: 'int'  # uint64
    gameplay_data: 'GameplayHouseholdData'
    story_progression_rule_set: 'StoryProgressionRuleSet'


class FamilyData(Message):
    # __init__
    family_account: 'AccountFamilyData'
    lastplayed_idx: 'int'  # uint64
    lastplayed_simid: 'int'  # uint64
    lastplayed_simtime: 'float'  # float32
    homezone_id: 'int'  # uint64


class AccountFamilyDataPatch(Message):
    # __init__
    familyid: 'int'  # uint64
    oldfamilyid: 'int'  # uint64
    ispremade: 'bool'


class SimLoadInfoVector(Message):
    # __init__
    SimLoadInfoResponse: 'RepeatedCompositeFieldContainer[SimData]'


class UpdateClientActiveSim(Message):
    # __init__
    active_sim_id: 'int'  # uint64


class PlumbbobOverrideModelKey(Message):
    class PLUMBBOB_STATE(IntEnum):
        PlayerActive: 'PlumbbobOverrideModelKey.PLUMBBOB_STATE' = 0
        Social: 'PlumbbobOverrideModelKey.PLUMBBOB_STATE' = 1
        PlayerClubLeader: 'PlumbbobOverrideModelKey.PLUMBBOB_STATE' = 2
        NpcClub: 'PlumbbobOverrideModelKey.PLUMBBOB_STATE' = 3
        NpcClubLeader: 'PlumbbobOverrideModelKey.PLUMBBOB_STATE' = 4
        Ensemble: 'PlumbbobOverrideModelKey.PLUMBBOB_STATE' = 5

    PlayerActive = PLUMBBOB_STATE.PlayerActive
    Social = PLUMBBOB_STATE.Social
    PlayerClubLeader = PLUMBBOB_STATE.PlayerClubLeader
    NpcClub = PLUMBBOB_STATE.NpcClub
    NpcClubLeader = PLUMBBOB_STATE.NpcClubLeader
    Ensemble = PLUMBBOB_STATE.Ensemble

    # __init__
    state: 'PlumbbobOverrideModelKey.PLUMBBOB_STATE'
    key: 'int'  # uint64


class PlumbbobSetPlumbbobOverrideModelKey(Message):
    # __init__
    overrides: 'RepeatedCompositeFieldContainer[PlumbbobOverrideModelKey]'


class PlumbbobEnsembleTintOverride(Message):
    # __init__
    color: 'Vector3'
    alpha: 'float'  # float32


class PlumbbobEnsembleTextureOverride(Message):
    # __init__
    texture_id: 'int'  # uint64


class ServerResponseFailed(Message):
    class Reason(IntEnum):
        REJECT_CLIENT_SELECT_MIXERINTERACTION: 'ServerResponseFailed.Reason' = 1
        REJECT_CLIENT_CANCEL_SUPERINTERACTION: 'ServerResponseFailed.Reason' = 2
        REJECT_CLIENT_SELECT_MIXER_INVALID: 'ServerResponseFailed.Reason' = 3

    REJECT_CLIENT_SELECT_MIXERINTERACTION = Reason.REJECT_CLIENT_SELECT_MIXERINTERACTION
    REJECT_CLIENT_CANCEL_SUPERINTERACTION = Reason.REJECT_CLIENT_CANCEL_SUPERINTERACTION
    REJECT_CLIENT_SELECT_MIXER_INVALID = Reason.REJECT_CLIENT_SELECT_MIXER_INVALID

    # __init__
    handle: 'int'  # uint32
    reason: 'int'  # uint32


class SimPB(Message):
    class SelectorVisualType(IntEnum):
        NORMAL: 'SimPB.SelectorVisualType' = 0
        OTHER: 'SimPB.SelectorVisualType' = 1
        BABY: 'SimPB.SelectorVisualType' = 2
        AT_WORK: 'SimPB.SelectorVisualType' = 3
        LATE_FOR_WORK: 'SimPB.SelectorVisualType' = 4
        MISSING_ACTIVE_WORK: 'SimPB.SelectorVisualType' = 5
        AT_DAYCARE: 'SimPB.SelectorVisualType' = 6
        PET_MISSING: 'SimPB.SelectorVisualType' = 7

    NORMAL = SelectorVisualType.NORMAL
    OTHER = SelectorVisualType.OTHER
    BABY = SelectorVisualType.BABY
    AT_WORK = SelectorVisualType.AT_WORK
    LATE_FOR_WORK = SelectorVisualType.LATE_FOR_WORK
    MISSING_ACTIVE_WORK = SelectorVisualType.MISSING_ACTIVE_WORK
    AT_DAYCARE = SelectorVisualType.AT_DAYCARE
    PET_MISSING = SelectorVisualType.PET_MISSING

    # __init__
    id: 'int'  # uint64
    instance_info: 'GameInstanceInfoPB'
    firstname: 'str'
    lastname: 'str'
    at_work: 'bool'
    is_selectable: 'bool'
    selector_visual_type: 'SimPB.SelectorVisualType'
    career_category: 'int'  # uint32
    can_care_for_toddler_at_home: 'bool'


class UpdateSelectableSims(Message):
    # __init__
    sims: 'RepeatedCompositeFieldContainer[SimPB]'


class Interaction(Message):
    class VisualType(IntEnum):
        SIMPLE: 'Interaction.VisualType' = 0
        PARENT: 'Interaction.VisualType' = 1
        MIXER: 'Interaction.VisualType' = 2
        POSTURE: 'Interaction.VisualType' = 3

    SIMPLE = VisualType.SIMPLE
    PARENT = VisualType.PARENT
    MIXER = VisualType.MIXER
    POSTURE = VisualType.POSTURE

    # __init__
    interaction_id: 'int'  # uint64
    insert_after_id: 'int'  # uint64
    icon_info: 'IconInfo'
    canceled: 'bool'
    cancelable: 'bool'
    is_pending: 'bool'
    priority: 'int'  # uint32
    is_guaranteed: 'bool'
    visible: 'bool'
    super_id: 'int'  # uint64
    visual_type: 'Interaction.VisualType'
    initiating_id: 'int'  # fixed uint64
    interactions_to_be_canceled: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    skill_id: 'int'  # uint64
    is_primary: 'bool'
    pipeline_progress: 'IQ_PipelineStage'
    queue_ui_state: 'IQ_UI_State'
    target_manager_object_id: 'ManagerObjectId'
    participant_manager_object_ids: 'RepeatedCompositeFieldContainer[ManagerObjectId]'
    stc_bit_id: 'int'  # fixed uint64
    super_icon_info: 'IconInfo'
    mood_list: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class InteractionsAdd(Message):
    # __init__
    sim_id: 'int'  # uint64
    interactions: 'RepeatedCompositeFieldContainer[Interaction]'


class InteractionsUpdate(Message):
    # __init__
    sim_id: 'int'  # uint64
    interactions: 'RepeatedCompositeFieldContainer[Interaction]'


class InteractionMixerOptionAdd(Message):
    # __init__
    mixer_id: 'int'  # uint32
    icon_info: 'IconInfo'
    state: 'MixerStateTypes'
    interaction_id: 'int'  # uint64
    autonomy_pick: 'int'  # uint64
    skill_id: 'int'  # uint64
    mixer_target: 'int'  # uint64
    target_is_social_group: 'bool'
    insert_after_id: 'int'  # uint32
    success_chance: 'float'  # float32
    affordance_id: 'int'  # uint64
    display_name_multi_target: 'LocalizedString'
    target_is_group: 'bool'


class InteractionMixerOptionsAdd(Message):
    # __init__
    interaction_id: 'int'  # uint64
    server_reference_id: 'int'  # uint32
    mixer_option: 'RepeatedCompositeFieldContainer[InteractionMixerOptionAdd]'


class InteractionMixerOptionsUpdate(Message):
    # __init__
    interaction_id: 'int'  # uint64
    mixer_option: 'RepeatedCompositeFieldContainer[InteractionMixerOptionUpdate]'


class InteractionMixerOptionUpdate(Message):
    # __init__
    mixer_id: 'int'  # uint32
    state: 'MixerStateTypes'
    interaction_id: 'int'  # uint64
    mixer_target: 'int'  # uint64
    target_is_social_group: 'bool'
    success_chance: 'float'  # float32


class InteractionMixerOptionCommands(Message):
    # __init__
    sim_id: 'int'  # uint64
    interaction_id: 'int'  # uint64
    server_reference_id: 'int'  # uint32
    mixer_adds: 'RepeatedCompositeFieldContainer[InteractionMixerOptionAdd]'
    mixer_updates: 'RepeatedCompositeFieldContainer[InteractionMixerOptionUpdate]'


class InteractionMixerOptionsClear(Message):
    # __init__
    sim_id: 'int'  # uint64
    interaction_id: 'int'  # uint64
    server_reference_id: 'int'  # uint32


class InteractionMixerLock(Message):
    # __init__
    sim_id: 'int'  # fixed uint64


class InteractionQuickTimeMixerUpdate(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    mixer_id: 'int'  # uint64
    object_id: 'int'  # uint64
    server_reference_id: 'int'  # uint32
    display_name: 'LocalizedString'


class InteractionQueueViewAdd(Message):
    # __init__
    interactions: 'InteractionsAdd'
    mixer_options: 'RepeatedCompositeFieldContainer[InteractionMixerOptionsAdd]'


class InteractionsRemove(Message):
    # __init__
    sim_id: 'int'  # uint64
    interaction_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64


class InteractionsRemoveAll(Message):
    # __init__
    sim_id: 'int'  # uint64


class InteractionReplace(Message):
    # __init__
    sim_id: 'int'  # uint64
    old_interaction_id: 'int'  # uint64
    new_interaction: 'Interaction'


class InteractionOutcome(Message):
    class Result(IntEnum):
        NEUTRAL: 'InteractionOutcome.Result' = 0
        NEGATIVE: 'InteractionOutcome.Result' = 1
        POSITIVE: 'InteractionOutcome.Result' = 2

    NEUTRAL = Result.NEUTRAL
    NEGATIVE = Result.NEGATIVE
    POSITIVE = Result.POSITIVE

    # __init__
    sim_id: 'int'  # uint64
    result: 'InteractionOutcome.Result'
    display_message: 'LocalizedString'


class InteractionStart(Message):
    # __init__
    sim_id: 'int'  # uint64


class InteractionEnd(Message):
    # __init__
    sim_id: 'int'  # uint64


class InteractionTurnStart(Message):
    # __init__
    sim_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    social_group: 'int'  # uint64


class InteractionLiabilityUpdate(Message):
    class LiabilityType(IntEnum):
        CRAFTING_QUALITY: 'InteractionLiabilityUpdate.LiabilityType' = 1

    CRAFTING_QUALITY = LiabilityType.CRAFTING_QUALITY

    # __init__
    type: 'InteractionLiabilityUpdate.LiabilityType'
    sim_id: 'int'  # uint64
    liabilty_release: 'bool'
    skill_id: 'int'  # uint64
    skill_points: 'int'  # uint32
    crafting_item_name: 'LocalizedString'
    crafting_quality: 'int'  # int32


class CraftingLiabilityUpdate(Message):
    # __init__
    core_data: 'InteractionLiabilityUpdate'
    crafting_item_name: 'LocalizedString'
    crafting_quality: 'int'  # uint32
    phase_name: 'LocalizedString'
    phase_index: 'int'  # uint32
    total_phases: 'int'  # uint32
    turn_index: 'int'  # uint32
    total_turns: 'int'  # uint32
    quality_statistic_value: 'int'  # int32


class RequestNumberMessage(Message):
    # __init__
    request: 'int'  # uint64
    zone_id: 'int'  # uint64


class FocusCameraEvent(Message):
    # __init__
    id: 'int'  # uint64
    location: 'Vector3'
    follow_mode: 'bool'
    position: 'Vector3'


class EnablePendingInteractionHeadline(Message):
    # __init__
    sim_id: 'int'  # uint64
    si_id: 'int'  # uint64
    icon_info: 'IconInfo'


class DisablePendingInteractionHeadline(Message):
    # __init__
    sim_id: 'int'  # uint64
    group_id: 'int'  # uint64
    canceled: 'bool'


class AddBalloon(Message):
    class BalloonType(IntEnum):
        THOUGHT_TYPE: 'AddBalloon.BalloonType' = 0
        SPEECH_TYPE: 'AddBalloon.BalloonType' = 1
        DISTRESS_TYPE: 'AddBalloon.BalloonType' = 2
        SENTIMENT_TYPE: 'AddBalloon.BalloonType' = 3
        SENTIMENT_INFANT_TYPE: 'AddBalloon.BalloonType' = 4

    THOUGHT_TYPE = BalloonType.THOUGHT_TYPE
    SPEECH_TYPE = BalloonType.SPEECH_TYPE
    DISTRESS_TYPE = BalloonType.DISTRESS_TYPE
    SENTIMENT_TYPE = BalloonType.SENTIMENT_TYPE
    SENTIMENT_INFANT_TYPE = BalloonType.SENTIMENT_INFANT_TYPE

    class BalloonPriority(IntEnum):
        MOTIVE_FAILURE_PRIORITY: 'AddBalloon.BalloonPriority' = 0
        SPEECH_PRIORITY: 'AddBalloon.BalloonPriority' = 1
        THOUGHT_PRIORITY: 'AddBalloon.BalloonPriority' = 2
        SENTIMENT_PRIORITY: 'AddBalloon.BalloonPriority' = 3
        SENTIMENT_INFANT_PRIORITY: 'AddBalloon.BalloonPriority' = 4

    MOTIVE_FAILURE_PRIORITY = BalloonPriority.MOTIVE_FAILURE_PRIORITY
    SPEECH_PRIORITY = BalloonPriority.SPEECH_PRIORITY
    THOUGHT_PRIORITY = BalloonPriority.THOUGHT_PRIORITY
    SENTIMENT_PRIORITY = BalloonPriority.SENTIMENT_PRIORITY
    SENTIMENT_INFANT_PRIORITY = BalloonPriority.SENTIMENT_INFANT_PRIORITY

    # __init__
    sim_id: 'int'  # uint64
    icon: 'ResourceKey'
    icon_sim_id: 'int'  # uint64
    overlay: 'ResourceKey'
    type: 'AddBalloon.BalloonType'
    priority: 'AddBalloon.BalloonPriority'
    duration: 'float'  # float32
    icon_object: 'ManagerObjectId'
    category_icon: 'IconInfo'
    view_offset_override: 'Vector3'
    rel_track: 'RelationshipTrack'
    icon_info: 'IconInfo'


class ReslotPlumbbob(Message):
    # __init__
    sim_id: 'int'  # uint64
    obj_id: 'int'  # uint64
    bone: 'int'  # uint32
    offset: 'Vector3'
    balloon_view_offset: 'Vector3'


class BuffUpdate(Message):
    class BuffDisplayType(IntEnum):
        DEFAULT: 'BuffUpdate.BuffDisplayType' = 0
        BURNOUT: 'BuffUpdate.BuffDisplayType' = 1

    DEFAULT = BuffDisplayType.DEFAULT
    BURNOUT = BuffDisplayType.BURNOUT

    # __init__
    buff_id: 'int'  # uint64
    sim_id: 'int'  # uint64
    reason: 'LocalizedString'
    timeout: 'int'  # uint64
    is_mood_buff: 'bool'
    buff_progress: 'BuffProgressArrow'
    commodity_guid: 'int'  # fixed uint64
    rate_multiplier: 'float'  # float32
    mood_type_override: 'int'  # uint64
    transition_into_buff_id: 'int'  # uint64
    motive_overlays: 'RepeatedCompositeFieldContainer[MotiveOverlay]'
    update_type: 'int'  # uint32
    display_type: 'BuffUpdate.BuffDisplayType'
    pack_specific_description: 'LocalizedString'


class MotiveOverlay(Message):
    # __init__
    overlay_type: 'MotiveOverlayType'
    commodity_guid: 'int'  # fixed uint64


class BuffClearAll(Message):
    # __init__
    sim_id: 'int'  # uint64


class TutorialUpdate(Message):
    # __init__
    tutorial_id: 'int'  # uint64


class TutorialViewedList(Message):
    # __init__
    tutorial_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64


class MemoryTriggerUpdate(Message):
    # __init__
    sim_id: 'int'  # uint64
    trigger_memory: 'bool'
    timeout: 'int'  # uint64
    memory_id: 'int'  # uint64


class CheatStatusUpdate(Message):
    # __init__
    cheats_enabled: 'bool'


class SetLoan(Message):
    # __init__
    amount: 'int'  # int32


class CareerInfo(Message):
    # __init__
    uid: 'int'  # uint64
    career_track: 'int'  # uint64
    career_level: 'int'  # uint32
    company: 'LocalizedString'
    conflicted_schedule: 'bool'
    work_schedule: 'Schedule'
    is_active: 'bool'
    is_selectable: 'bool'
    hourly_pay: 'int'  # uint32
    benefit_description: 'LocalizedString'
    not_selectable_tooltip: 'LocalizedString'
    work_from_home_description: 'LocalizedString'
    enable_infants_tray_button: 'bool'


class CareerSelectionUI(Message):
    class SelectionReason(IntEnum):
        JOIN_CAREER: 'CareerSelectionUI.SelectionReason' = 0
        QUIT_CAREER: 'CareerSelectionUI.SelectionReason' = 1
        CALLED_IN_SICK: 'CareerSelectionUI.SelectionReason' = 2

    JOIN_CAREER = SelectionReason.JOIN_CAREER
    QUIT_CAREER = SelectionReason.QUIT_CAREER
    CALLED_IN_SICK = SelectionReason.CALLED_IN_SICK

    # __init__
    sim_id: 'int'  # uint64
    career_choices: 'RepeatedCompositeFieldContainer[CareerInfo]'
    is_branch_select: 'bool'
    reason: 'CareerSelectionUI.SelectionReason'
    current_shift: 'int'  # uint32
    default_career_select_uid: 'int'  # uint64
    career_selector_type: 'int'  # uint32


class CareerSituationEnable(Message):
    # __init__
    sim_id: 'int'  # uint64
    career_situation_id: 'int'  # uint64
    enable: 'bool'
    career_uid: 'int'  # uint64


class GigBudgetUpdate(Message):
    # __init__
    current_budget: 'int'  # int32
    vfx_amount: 'int'  # int32
    current_spent: 'int'  # int32


class RewardCount(Message):
    # __init__
    count: 'int'  # uint32


class RewardList(Message):
    # __init__
    instance_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    reward_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    sim_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class RewardPayout(Message):
    # __init__
    reward_id: 'int'  # uint64
    money: 'RepeatedCompositeFieldContainer[int]'  # uint32
    cas_part_keys: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    trait_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    object_names: 'RepeatedCompositeFieldContainer[LocalizedString]'


class SocialContextUpdate(Message):
    # __init__
    bit_id: 'int'  # fixed uint64


class DevelopmentalMilestoneUpdate(Message):
    class MilestoneState(IntEnum):
        ACTIVE: 'DevelopmentalMilestoneUpdate.MilestoneState' = 0
        UNLOCKED: 'DevelopmentalMilestoneUpdate.MilestoneState' = 1

    ACTIVE = MilestoneState.ACTIVE
    UNLOCKED = MilestoneState.UNLOCKED

    # __init__
    sim_id: 'int'  # uint64
    developmental_milestone_id: 'int'  # uint64
    state: 'DevelopmentalMilestoneUpdate.MilestoneState'
    new_in_ui: 'bool'
    unlocked_with_sim_id: 'int'  # uint64
    unlocked_with_object_name: 'LocalizedString'
    unlocked_in_lot_name: 'str'
    unlocked_in_region_id: 'int'  # uint64
    unlocked_career_name: 'LocalizedString'
    unlocked_career_level: 'LocalizedString'
    unlocked_death_type: 'LocalizedString'
    unlocked_trait_name: 'LocalizedString'
    goal_id: 'int'  # uint64
    completed_time: 'int'  # uint64
    age_completed: 'int'  # uint32
    unlocked_small_business_name: 'str'
    unlocked_dynasty_name: 'str'


class AllDevelopmentalMilestonesUpdate(Message):
    # __init__
    sim_id: 'int'  # uint64
    milestones: 'RepeatedCompositeFieldContainer[DevelopmentalMilestoneUpdate]'


class LifetimeMilestonesData(Message):
    # __init__
    category_id: 'int'  # uint32
    milestones: 'RepeatedCompositeFieldContainer[DevelopmentalMilestoneUpdate]'


class LuckUpdate(Message):
    # __init__
    sim_id: 'int'  # uint64
    current_level: 'int'  # uint64
