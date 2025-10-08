from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer
from enum import IntEnum

from protocolbuffers.UI_pb2 import *
from protocolbuffers.Localization_pb2 import *


class SituationGoalData(Message):
    # __init__
    goal_type_id: 'int'  # fixed uint64
    actor_id: 'int'  # fixed uint64
    count: 'int'  # uint32
    completed: 'bool'
    chain_id: 'int'  # fixed uint64
    custom_data: 'bytes'
    locked: 'bool'
    completed_time: 'int'  # uint64
    target_id: 'int'  # fixed uint64
    secondary_target_id: 'int'  # fixed uint64
    sub_goals: 'RepeatedCompositeFieldContainer[SituationGoalData]'


class CompletedSituationGoalData(Message):
    # __init__
    situation_goal: 'SituationGoalData'
    chosen_goal_set_type_id: 'int'  # fixed uint64


class SituationGoalChainData(Message):
    # __init__
    starting_goal_set_type_id: 'int'  # fixed uint64
    chosen_goal_set_type_id: 'int'  # fixed uint64
    chain_id: 'int'  # fixed uint64
    display_position: 'int'  # int32


class SituationGoalTrackerData(Message):
    class GoalTrackerType(IntEnum):
        STANDARD_GOAL_TRACKER: 'SituationGoalTrackerData.GoalTrackerType' = 0
        DYNAMIC_GOAL_TRACKER: 'SituationGoalTrackerData.GoalTrackerType' = 1
        SIMPLE_GOAL_TRACKER: 'SituationGoalTrackerData.GoalTrackerType' = 2
        ACTIVITY_GOAL_TRACKER: 'SituationGoalTrackerData.GoalTrackerType' = 3
        STANDARD_GRAPHED_GOAL_TRACKER: 'SituationGoalTrackerData.GoalTrackerType' = 4

    STANDARD_GOAL_TRACKER = GoalTrackerType.STANDARD_GOAL_TRACKER
    DYNAMIC_GOAL_TRACKER = GoalTrackerType.DYNAMIC_GOAL_TRACKER
    SIMPLE_GOAL_TRACKER = GoalTrackerType.SIMPLE_GOAL_TRACKER
    ACTIVITY_GOAL_TRACKER = GoalTrackerType.ACTIVITY_GOAL_TRACKER
    STANDARD_GRAPHED_GOAL_TRACKER = GoalTrackerType.STANDARD_GRAPHED_GOAL_TRACKER

    # __init__
    has_offered_goals: 'bool'
    inherited_target_id: 'int'  # fixed uint64
    chains: 'RepeatedCompositeFieldContainer[SituationGoalChainData]'
    minor_goals: 'RepeatedCompositeFieldContainer[SituationGoalData]'
    main_goal: 'SituationGoalData'
    completed_goals: 'RepeatedCompositeFieldContainer[CompletedSituationGoalData]'
    goal_tracker_type: 'SituationGoalTrackerData.GoalTrackerType'
    graphed_goal_tracker_data: 'SituationGraphedGoalTrackerData'


class SituationGraphedGoalTrackerData(Message):
    # __init__
    completed_goals_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    unlocked_goals_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64


class SituationAssignmentData(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    job_type_id: 'int'  # fixed uint64
    purpose: 'int'  # uint32
    role_state_type_id: 'int'  # fixed uint64
    spawning_option: 'int'  # uint32
    request_priority: 'int'  # uint32
    expectation_preference: 'bool'
    accept_alternate_sim: 'bool'
    common_blacklist_categories: 'int'  # uint32
    elevated_importance_override: 'bool'
    reservation: 'bool'


class SituationSimpleSeedlingData(Message):
    # __init__
    phase_index: 'int'  # uint32
    remaining_phase_time: 'float'  # float32


class SituationComplexSeedlingData(Message):
    # __init__
    situation_custom_data: 'bytes'
    state_custom_data: 'bytes'


class SituationJobAndRoleState(Message):
    # __init__
    job_type_id: 'int'  # fixed uint64
    role_state_type_id: 'int'  # fixed uint64
    emotional_loot_actions_type_id: 'int'  # fixed uint64


class SituationSpecialObject(Message):
    # __init__
    definition_id: 'int'  # uint64
    name: 'LocalizedString'


class SituationSeedData(Message):
    # __init__
    situation_type_id: 'int'  # fixed uint64
    situation_id: 'int'  # fixed uint64
    seed_purpose: 'int'  # uint32
    invite_only: 'bool'
    host_sim_id: 'int'  # fixed uint64
    assignments: 'RepeatedCompositeFieldContainer[SituationAssignmentData]'
    user_facing: 'bool'
    duration: 'float'  # float32
    zone_id: 'int'  # fixed uint64
    jobs_and_role_states: 'RepeatedCompositeFieldContainer[SituationJobAndRoleState]'
    create_time: 'int'  # uint64
    score: 'float'  # float32
    simple_data: 'SituationSimpleSeedlingData'
    complex_data: 'SituationComplexSeedlingData'
    filter_requesting_sim_id: 'int'  # fixed uint64
    goal_tracker_data: 'SituationGoalTrackerData'
    start_time: 'int'  # uint64
    active_household_id: 'int'  # fixed uint64
    scoring_enabled: 'bool'
    main_goal_visibility: 'bool'
    linked_sim_id: 'int'  # fixed uint64
    special_object_icon: 'IconInfo'
    situation_activity_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    special_object: 'SituationSpecialObject'
    guest_attire_color: 'int'  # uint64
    guest_attire_style: 'int'  # uint64
    spawn_sims_during_zone_spin_up: 'bool'


class SituationBlacklistTagData(Message):
    # __init__
    tag: 'int'  # uint64
    time: 'int'  # uint64


class SituationBlacklistData(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    tag_data: 'RepeatedCompositeFieldContainer[SituationBlacklistTagData]'


class AllSituationData(Message):
    # __init__
    seeds: 'RepeatedCompositeFieldContainer[SituationSeedData]'
    leave_situation_id: 'int'  # fixed uint64
    leave_now_situation_id: 'int'  # fixed uint64
    blacklist_data: 'RepeatedCompositeFieldContainer[SituationBlacklistData]'
