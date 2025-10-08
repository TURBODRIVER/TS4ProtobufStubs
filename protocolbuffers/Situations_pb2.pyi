from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer

from protocolbuffers.ResourceKey_pb2 import *
from protocolbuffers.Localization_pb2 import *
from protocolbuffers.DistributorOps_pb2 import *
from protocolbuffers.UI_pb2 import *
from protocolbuffers.Lot_pb2 import *
from protocolbuffers.Math_pb2 import *
from protocolbuffers.CustomSchedule_pb2 import *


class SimPickerItem(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    enabled: 'bool'


class SituationEditJobData(Message):
    # __init__
    job_id: 'int'  # uint64
    sim_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    hire_count: 'int'  # uint32


class SituationEditData(Message):
    # __init__
    drama_node_id: 'int'  # uint64
    zone_id: 'int'  # uint64
    selected_activity_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    guest_attire_style: 'int'  # uint64
    guest_attire_color: 'int'  # uint64
    job_data: 'RepeatedCompositeFieldContainer[SituationEditJobData]'
    special_object_icon_info: 'IconInfo'
    getaway_schedule: 'CustomSchedule'
    duration_nights: 'int'  # uint32
    recurring_days: 'RepeatedCompositeFieldContainer[int]'  # uint32
    end_time: 'int'  # uint64
    has_valid_zone_schedule: 'bool'


class SituationPrepare(Message):
    # __init__
    situation_session_id: 'int'  # uint32
    is_targeted: 'bool'
    sims: 'RepeatedCompositeFieldContainer[SimPickerItem]'
    target_id: 'int'  # fixed uint64
    sim_id: 'int'  # fixed uint64
    situation_resource_id: 'RepeatedCompositeFieldContainer[int]'  # uint64
    creation_time: 'int'  # uint64
    edit_data: 'SituationEditData'
    situation_category: 'int'  # uint32
    is_active: 'bool'
    is_new_from_tuning: 'bool'


class SituationIDBatch(Message):
    # __init__
    situation_session_id: 'int'  # uint32
    situation_resource_id: 'RepeatedCompositeFieldContainer[int]'  # uint64
    situation_name: 'RepeatedCompositeFieldContainer[LocalizedString]'
    category_id: 'RepeatedCompositeFieldContainer[int]'  # uint32
    mtx_id: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    highest_medal_earned: 'RepeatedCompositeFieldContainer[int]'  # int32
    scoring_enabled: 'bool'
    tooltip: 'RepeatedCompositeFieldContainer[LocalizedString]'
    allow_user_facing_goals: 'RepeatedCompositeFieldContainer[bool]'
    medal_icon_override: 'RepeatedCompositeFieldContainer[ResourceKey]'
    scoring_lock_reason: 'RepeatedCompositeFieldContainer[LocalizedString]'
    new_entry: 'RepeatedCompositeFieldContainer[bool]'


class SituationDataBatch(Message):
    # __init__
    situation_session_id: 'int'  # uint32
    situations: 'RepeatedCompositeFieldContainer[SituationData]'


class SituationGuestAttireColor(Message):
    # __init__
    color_tag: 'int'  # uint64
    color_name: 'LocalizedString'
    color_value: 'str'


class SituationGuestAttireStyle(Message):
    # __init__
    style_tag: 'int'  # uint64
    style_name: 'LocalizedString'


class SituationStyleData(Message):
    # __init__
    guest_attire_colors: 'RepeatedCompositeFieldContainer[SituationGuestAttireColor]'
    guest_attire_styles: 'RepeatedCompositeFieldContainer[SituationGuestAttireStyle]'
    special_object_help_tooltip: 'LocalizedString'
    no_special_object_icon: 'ResourceKey'
    no_special_object_label: 'LocalizedString'
    cas_edit_job_id: 'int'  # uint64
    cas_edit_outfit_category: 'int'  # uint32
    cas_edit_no_sim_icon: 'ResourceKey'
    visible_on_role_page: 'bool'


class SituationData(Message):
    # __init__
    icon_info: 'IconInfo'
    cost: 'int'  # uint32
    max_participants: 'int'  # uint32
    rewards: 'RepeatedCompositeFieldContainer[SituationLevelReward]'
    jobs: 'RepeatedCompositeFieldContainer[SituationJobData]'
    available_activity_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    required_activity_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    style_data: 'SituationStyleData'
    minimum_activities: 'int'  # uint32
    activities_disabled_tooltip: 'LocalizedString'
    challenge_reward_override: 'RepeatedCompositeFieldContainer[LocalizedString]'
    activity_goal_situation: 'bool'
    randomizable_activity_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    num_randomized: 'int'  # uint32
    unavailable_activity_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    jobs_per_row: 'int'  # uint32
    job_cell_padding: 'RepeatedCompositeFieldContainer[int]'  # uint32
    role_updates_activity_preferences: 'RepeatedCompositeFieldContainer[int]'  # uint64
    sim_filter_requesting_sim_override: 'int'  # uint64
    getaway_schedule: 'CustomSchedule'
    max_duration_nights: 'int'  # uint32
    default_duration_nights: 'int'  # uint32


class SituationJobData(Message):
    # __init__
    job_resource_id: 'int'  # uint64
    icon_info: 'IconInfo'
    is_hireable: 'bool'
    min_required: 'int'  # uint32
    max_allowed: 'int'  # uint32
    hire_cost: 'int'  # uint32
    help_tooltip: 'LocalizedString'
    is_guest: 'bool'
    border_image: 'ResourceKey'


class SituationLevelReward(Message):
    # __init__
    level: 'int'  # uint32
    display_name: 'RepeatedCompositeFieldContainer[LocalizedString]'


class SituationAssignJob(Message):
    # __init__
    situation_session_id: 'int'  # uint32
    sim_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    job_resource_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64


class SituationPreferredActivities(Message):
    # __init__
    activities: 'RepeatedCompositeFieldContainer[int]'  # uint64
    icon: 'ResourceKey'
    footer: 'LocalizedString'


class SituationJobSim(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    account_id: 'int'  # fixed uint64
    career_id: 'int'  # fixed uint64
    career_track_id: 'int'  # fixed uint64
    cell_disabled: 'bool'
    cell_disabled_tooltip: 'LocalizedString'


class SituationJobSims(Message):
    # __init__
    situation_session_id: 'int'  # uint32
    job_resource_id: 'int'  # uint64
    sim_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    lock_selection: 'bool'
    sims: 'RepeatedCompositeFieldContainer[SituationJobSim]'
    requirements: 'LocalizedString'


class SituationLocations(Message):
    # __init__
    situation_locations: 'RepeatedCompositeFieldContainer[LotInfoItem]'


class SituationGetawayRuleOption(Message):
    class RuleOptionGroup():
        # __init__
        category_id: 'int'  # uint32
        category_display_name: 'LocalizedString'
        is_multi_select: 'bool'
        disallowed_ages: 'RepeatedCompositeFieldContainer[int]'  # uint32
        disallowed_species: 'RepeatedCompositeFieldContainer[int]'  # uint32

    # __init__
    display_name: 'LocalizedString'
    description: 'LocalizedString'
    icon: 'ResourceKey'
    groups: 'RepeatedCompositeFieldContainer[SituationGetawayRuleOption.RuleOptionGroup]'
    rule_guid64: 'int'  # uint64
    is_track_based_challenge: 'bool'
    category_id: 'int'  # uint32
    category_display_name: 'LocalizedString'
    is_multi_select: 'bool'
    disallowed_ages: 'RepeatedCompositeFieldContainer[int]'  # uint32
    disallowed_species: 'RepeatedCompositeFieldContainer[int]'  # uint32


class SituationGetawayRules(Message):
    # __init__
    options: 'RepeatedCompositeFieldContainer[SituationGetawayRuleOption]'


class SituationSimScore(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    score: 'int'  # uint32
    job_icon_info: 'IconInfo'
    version_id: 'int'  # uint32


class SituationLevelData(Message):
    # __init__
    description: 'LocalizedString'
    max_threshold: 'int'  # uint32


class SituationLevelUpdate(Message):
    # __init__
    score_lower_bound: 'int'  # uint32
    score_upper_bound: 'int'  # uint32
    current_level: 'int'  # uint32
    level_icon: 'IconInfo'


class SituationJobAssignment(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    name: 'LocalizedString'
    desc: 'LocalizedString'
    tooltip: 'LocalizedString'


class SituationStart(Message):
    # __init__
    score: 'int'  # uint32
    participants: 'RepeatedCompositeFieldContainer[SituationSimScore]'
    icon_info: 'IconInfo'
    level_data: 'RepeatedCompositeFieldContainer[SituationLevelData]'
    operation_list: 'OperationList'
    end_time: 'int'  # uint64
    situation_id: 'int'  # uint64
    current_level: 'SituationLevelUpdate'
    sim_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    sim_jobs: 'RepeatedCompositeFieldContainer[SituationJobAssignment]'
    start_time: 'int'  # uint64
    start_audio_sting: 'ResourceKey'
    scoring_enabled: 'bool'
    is_active_career: 'bool'
    has_stayed_late: 'bool'
    meter_data: 'RepeatedCompositeFieldContainer[SituationMeterData]'
    display_type: 'int'  # uint32
    linked_sim_id: 'int'  # fixed uint64
    force_goals_enabled: 'bool'
    user_facing_type: 'int'  # uint32
    allow_non_prestige_events: 'bool'
    display_priority: 'int'  # uint32
    display_delay: 'int'  # uint64
    from_load: 'bool'
    situation_guid: 'int'  # uint64
    background_audio: 'ResourceKey'
    situation_display_flags: 'int'  # uint32
    situation_display_style: 'int'  # uint32
    situation_end_time_string: 'LocalizedString'
    cancel_tooltip_override: 'LocalizedString'
    live_event_id: 'int'  # uint64
    pivotal_moment_background_style: 'int'  # uint32
    situation_display_description: 'LocalizedString'
    tutorial_id: 'int'  # uint64
    pivotal_moment_guid: 'int'  # uint64
    reward_description: 'LocalizedString'
    custom_schedule: 'CustomSchedule'


class SituationSimJoined(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    job_assignment: 'SituationJobAssignment'


class SituationSimLeft(Message):
    # __init__
    sim_id: 'int'  # fixed uint64


class SituationScoreUpdate(Message):
    # __init__
    situation_id: 'int'  # uint64
    score: 'int'  # uint32
    sim_id: 'int'  # fixed uint64
    current_level: 'SituationLevelUpdate'


class SituationGoal(Message):
    # __init__
    goal_id: 'int'  # uint32
    icon_info: 'IconInfo'
    goal_name: 'LocalizedString'
    max_iterations: 'int'  # uint32
    current_iterations: 'int'  # uint32
    goal_tooltip: 'LocalizedString'
    audio_sting: 'ResourceKey'
    display_type: 'int'  # uint32
    highlight_goal: 'bool'
    goal_preference: 'int'  # uint32
    goal_preference_tooltip: 'LocalizedString'
    secondary_icon_info: 'IconInfo'
    tutorial_tip_group_guid: 'int'  # uint64
    is_complete: 'bool'
    is_mandatory: 'bool'
    expiration_time: 'int'  # uint64
    ui_element: 'int'  # uint64
    mtx_bundle_id: 'int'  # uint64


class SituationGoalsUpdate(Message):
    # __init__
    situation_id: 'int'  # uint64
    goals: 'RepeatedCompositeFieldContainer[SituationGoal]'
    completed_goal_id: 'int'  # uint32
    major_goal: 'SituationGoal'
    goal_status: 'int'  # uint32
    goal_sub_text: 'LocalizedString'
    goal_button_data: 'SituationGoalButtonData'
    pivotal_moment_guid64: 'int'  # uint64


class SituationGoalButtonData(Message):
    # __init__
    button_text: 'LocalizedString'
    is_enabled: 'bool'
    required_packs: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class SituationTimeUpdate(Message):
    # __init__
    situation_id: 'int'  # uint64
    end_time: 'int'  # uint64
    has_stayed_late: 'bool'


class SituationCallbackResponse(Message):
    # __init__
    situation_id: 'int'  # uint64
    situation_callback: 'str'


class SituationIconUpdate(Message):
    # __init__
    situation_id: 'int'  # uint64
    icon_info: 'IconInfo'


class AddMinimizedSituation(Message):
    # __init__
    pivotal_moment_guid: 'int'  # uint64
    display_type: 'int'  # uint64
    display_name: 'LocalizedString'
    situation_guid: 'int'  # uint64


class RemoveMinimizedSituation(Message):
    # __init__
    pivotal_moment_guid: 'int'  # uint64


class SituationMeterData(Message):
    # __init__
    meter_id: 'int'  # uint32
    minimum_value: 'int'  # fixed uint32
    maximum_value: 'int'  # fixed uint32
    meter_text: 'LocalizedString'
    meter_tooltip: 'LocalizedString'
    thresholds: 'RepeatedCompositeFieldContainer[SituationMeterThreshold]'


class SituationMeterThreshold(Message):
    # __init__
    threshold: 'int'  # fixed uint32
    color: 'int'  # uint32


class SituationMeterUpdate(Message):
    # __init__
    situation_id: 'int'  # uint64
    meter_id: 'int'  # uint32
    update_value: 'int'  # fixed uint32


class SituationOutcomeData(Message):
    # __init__
    situation_name: 'LocalizedString'
    outcome_title: 'LocalizedString'
    outcome_description: 'LocalizedString'
    next_steps_description: 'LocalizedString'
    reward_1_icon: 'ResourceKey'
    reward_1_name: 'LocalizedString'
    reward_1_tooltip: 'LocalizedString'
    situation_display_style: 'int'  # uint32


class SituationActiveScheduleUpdate(Message):
    # __init__
    situation_id: 'int'  # uint64
    custom_schedule: 'CustomSchedule'


class ScenarioGoalGroup(Message):
    # __init__
    header_icon: 'IconInfo'
    header_name: 'LocalizedString'
    goals: 'RepeatedCompositeFieldContainer[SituationGoal]'


class ScenarioGoalsUpdate(Message):
    # __init__
    scenario_id: 'int'  # uint64
    goal_groups: 'RepeatedCompositeFieldContainer[ScenarioGoalGroup]'
    completed_goal_id: 'int'  # uint32
    instance_id: 'int'  # uint64


class ScenarioEnded(Message):
    # __init__
    scenario_id: 'int'  # uint64


class ScenarioOutcomeData(Message):
    # __init__
    scenario_name: 'LocalizedString'
    outcome_title: 'LocalizedString'
    outcome_description: 'LocalizedString'
    next_steps_description: 'LocalizedString'
    outcome_icon: 'ResourceKey'
    reward_icon: 'ResourceKey'
    bonus_icon: 'ResourceKey'
    household_id: 'int'  # uint64
    reward_tooltip: 'LocalizedString'
    bonus_tooltip: 'LocalizedString'


class QuestGoalUpdate(Message):
    # __init__
    live_event_id: 'int'  # uint64
    quest_id: 'int'  # uint64
    situation_goal_id: 'int'  # uint64
