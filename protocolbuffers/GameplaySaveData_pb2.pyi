from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer
from enum import IntEnum

from protocolbuffers.ResourceKey_pb2 import *
from protocolbuffers.SituationPersistence_pb2 import *
from protocolbuffers.SimObjectAttributes_pb2 import *
from protocolbuffers.Dialog_pb2 import *
from protocolbuffers.Routing_pb2 import *
from protocolbuffers.Math_pb2 import *
from protocolbuffers.Localization_pb2 import *
from protocolbuffers.Clubs_pb2 import *
from protocolbuffers.SimsCustomOptions_pb2 import *
from protocolbuffers.Business_pb2 import *
from protocolbuffers.UI_pb2 import *
from protocolbuffers.WeatherSeasons_pb2 import *
from protocolbuffers.Roommates_pb2 import *
from protocolbuffers.Calendar_pb2 import *
from protocolbuffers.Outfits_pb2 import *
from protocolbuffers.CustomSchedule_pb2 import *


class EcoFootprintStateType(IntEnum):
    GREEN: 'EcoFootprintStateType' = 0
    NEUTRAL: 'EcoFootprintStateType' = 1
    INDUSTRIAL: 'EcoFootprintStateType' = 2


GREEN = EcoFootprintStateType.GREEN
NEUTRAL = EcoFootprintStateType.NEUTRAL
INDUSTRIAL = EcoFootprintStateType.INDUSTRIAL


class ZoneBedInfoData(Message):
    # __init__
    num_beds: 'int'  # uint32
    double_bed_exist: 'bool'
    kid_bed_exist: 'bool'
    alternative_sleeping_spots: 'int'  # uint32
    university_roommate_beds: 'int'  # uint32


class ZoneCurfewData(Message):
    # __init__
    time: 'int'  # int32
    curfew_type: 'int'  # int32


class LotLevelData(Message):
    # __init__
    commodity_tracker: 'PersistableCommodityTracker'
    level_index: 'int'  # int32


class GameplayZoneData(Message):
    # __init__
    game_time: 'int'  # uint64
    clock_speed_mode: 'int'  # uint32
    situations_data: 'AllSituationData'
    venue_data: 'VenueData'
    active_household_id_on_save: 'int'  # fixed uint64
    lot_owner_household_id_on_save: 'int'  # fixed uint64
    venue_type_id_on_save: 'int'  # fixed uint64
    bed_info_data: 'ZoneBedInfoData'
    commodity_tracker: 'PersistableCommodityTracker'
    statistics_tracker: 'PersistableStatisticsTracker'
    skill_tracker: 'PersistableSkillTracker'
    active_travel_group_id_on_save: 'int'  # fixed uint64
    ensemble_service_data: 'EnsembleServiceData'
    ranked_statistic_tracker: 'PersistableRankedStatisticTracker'
    curfew_setting: 'int'  # int32
    hidden_sim_service_data: 'HiddenSimServiceData'
    curfew_settings: 'RepeatedCompositeFieldContainer[ZoneCurfewData]'
    architectural_statistics: 'RepeatedCompositeFieldContainer[Statistic]'
    lot_level_data: 'RepeatedCompositeFieldContainer[LotLevelData]'


class LotUnpaidBillData(Message):
    # __init__
    money_amount: 'int'  # uint32
    zone_id: 'int'  # fixed uint64
    situation_id: 'int'  # fixed uint64
    sim_ids_on_lot: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class HouseholdMilestoneDataTracker(Message):
    # __init__
    milestones_completed: 'RepeatedCompositeFieldContainer[int]'  # uint32
    objectives_completed: 'RepeatedCompositeFieldContainer[int]'  # uint32
    data: 'EventDataObject'
    milestone_completion_counts: 'RepeatedCompositeFieldContainer[MilestoneCompletionCount]'


class Holiday(Message):
    # __init__
    holiday_type: 'int'  # fixed uint64
    name: 'str'
    icon: 'ResourceKey'
    time_off_for_work: 'bool'
    time_off_for_school: 'bool'
    traditions: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    lot_decoration_preset: 'int'  # fixed uint64


class HolidayTracker(Message):
    # __init__
    holidays: 'RepeatedCompositeFieldContainer[Holiday]'
    situations: 'RepeatedCompositeFieldContainer[SituationSeedData]'
    situation_holiday_type: 'int'  # fixed uint64
    situation_holiday_time: 'int'  # uint64
    cancelled_holiday_type: 'int'  # fixed uint64
    cancelled_holiday_time: 'int'  # uint64


class SimPreference(Message):
    # __init__
    sim_id: 'int'  # uint64
    object_id: 'int'  # uint64
    subroot_index: 'int'  # int64


class ZonePreferenceData(Message):
    # __init__
    zone_id: 'int'  # uint64
    preference_tag: 'int'  # uint64
    sim_preferences: 'RepeatedCompositeFieldContainer[SimPreference]'


class ObjectPreferenceTracker(Message):
    # __init__
    zone_preference_datas: 'RepeatedCompositeFieldContainer[ZonePreferenceData]'


class Delivery(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    delivery_tuning_guid: 'int'  # fixed uint64
    expected_arrival_time: 'int'  # uint64
    sender_sim_id: 'int'  # fixed uint64


class GameplayScenarioTrackerData(Message):
    # __init__
    active_scenario_data: 'GameplayScenarioData'


class HouseholdPivotalMomentTracker(Message):
    # __init__
    pivotal_moments: 'RepeatedCompositeFieldContainer[PivotalMoment]'
    completed_pivotal_moment_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    rewarded_pivotal_moment_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    situation_seeds: 'RepeatedCompositeFieldContainer[SituationSeedData]'


class GameplayScenarioData(Message):
    class ScenarioGoalData():
        # __init__
        goal_data: 'SituationGoalData'

    class IndexGoalMandatoryTriple():
        # __init__
        sequence_index: 'int'  # uint64
        completed_goal: 'GameplayScenarioData.ScenarioGoalData'
        is_mandatory: 'bool'

    class SimFilterInfoPair():
        # __init__
        sim_filter_id: 'int'  # uint64
        sim_info_id: 'int'  # uint64

    class PhaseOutputInfo():
        # __init__
        phase_guid64: 'int'  # uint64
        output_key: 'int'  # int64
        next_phase: 'str'
        output_time: 'int'  # uint64

    class CompletedGoalInfo():
        # __init__
        goal_guid64: 'int'  # uint64
        completion_time: 'int'  # uint64

    class TerminatedPhaseInfo():
        # __init__
        phase_guid64: 'int'  # uint64
        termination_time: 'int'  # uint64

    # __init__
    scenario_guid: 'int'  # uint64
    active_goals: 'RepeatedCompositeFieldContainer[GameplayScenarioData.ScenarioGoalData]'
    sim_time_lapsed: 'int'  # uint64
    active_phase_guid: 'int'  # uint64
    completed_goals: 'RepeatedCompositeFieldContainer[int]'  # uint64
    triggered_phases: 'RepeatedCompositeFieldContainer[int]'  # uint64
    last_completed_goal_sequence_pair: 'RepeatedCompositeFieldContainer[GameplayScenarioData.IndexGoalMandatoryTriple]'
    sim_filter_sim_info_pair: 'RepeatedCompositeFieldContainer[GameplayScenarioData.SimFilterInfoPair]'
    skipped_phases: 'RepeatedCompositeFieldContainer[int]'  # uint64
    terminated_phases: 'RepeatedCompositeFieldContainer[int]'  # uint64
    last_phase_outputs: 'RepeatedCompositeFieldContainer[GameplayScenarioData.PhaseOutputInfo]'
    completed_goal_infos: 'RepeatedCompositeFieldContainer[GameplayScenarioData.CompletedGoalInfo]'
    terminated_phase_infos: 'RepeatedCompositeFieldContainer[GameplayScenarioData.TerminatedPhaseInfo]'
    goal_data: 'SituationGoalData'
    sequence_index: 'int'  # uint64
    completed_goal: 'GameplayScenarioData.ScenarioGoalData'
    is_mandatory: 'bool'
    sim_filter_id: 'int'  # uint64
    sim_info_id: 'int'  # uint64
    phase_guid64: 'int'  # uint64
    output_key: 'int'  # int64
    next_phase: 'str'
    output_time: 'int'  # uint64
    goal_guid64: 'int'  # uint64
    completion_time: 'int'  # uint64
    phase_guid64: 'int'  # uint64
    termination_time: 'int'  # uint64


class GameplayHouseholdData(Message):
    class SimLifeSpan(IntEnum):
        SHORT: 'GameplayHouseholdData.SimLifeSpan' = 0
        NORMAL: 'GameplayHouseholdData.SimLifeSpan' = 1
        LONG: 'GameplayHouseholdData.SimLifeSpan' = 2
        UNKNOWN: 'GameplayHouseholdData.SimLifeSpan' = 3

    SHORT = SimLifeSpan.SHORT
    NORMAL = SimLifeSpan.NORMAL
    LONG = SimLifeSpan.LONG
    UNKNOWN = SimLifeSpan.UNKNOWN

    # __init__
    cheats_enabled: 'bool'
    owned_object_count: 'int'  # uint32
    service_npc_records: 'RepeatedCompositeFieldContainer[ServiceNpcRecord]'
    delinquent_utilities: 'RepeatedCompositeFieldContainer[int]'  # uint32
    can_deliver_bill: 'bool'
    current_payment_owed: 'int'  # int64
    bill_timer: 'int'  # uint64
    shutoff_timer: 'int'  # uint64
    warning_timer: 'int'  # uint64
    additional_bill_costs: 'RepeatedCompositeFieldContainer[AdditionalBillCost]'
    collection_data: 'RepeatedCompositeFieldContainer[CollectionData]'
    put_bill_in_hidden_inventory: 'bool'
    billable_household_value: 'int'  # uint64
    highest_earned_situation_medals: 'RepeatedCompositeFieldContainer[SituationEarnedMedals]'
    build_buy_unlocks: 'RepeatedCompositeFieldContainer[int]'  # uint64
    situation_scoring_enabled: 'bool'
    build_buy_unlock_list: 'ResourceKeyList'
    retail_data: 'RepeatedCompositeFieldContainer[RetailData]'
    bucks_data: 'RepeatedCompositeFieldContainer[BucksData]'
    additional_employee_slots: 'int'  # uint32
    lot_unpaid_bill_data: 'RepeatedCompositeFieldContainer[LotUnpaidBillData]'
    home_world_id: 'int'  # uint64
    last_played_home_zone_id: 'int'  # fixed uint64
    home_zone_move_in_ticks: 'int'  # uint64
    always_welcomed_sim_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    household_milestone_tracker: 'HouseholdMilestoneDataTracker'
    missing_pet_tracker_data: 'MissingPetTrackerData'
    laundry_data: 'LaundryData'
    holiday_tracker: 'HolidayTracker'
    deliveries: 'RepeatedCompositeFieldContainer[Delivery]'
    object_preference_tracker: 'ObjectPreferenceTracker'
    current_bill_details: 'RepeatedCompositeFieldContainer[CurrentBillDetail]'
    bill_utility_settings: 'RepeatedCompositeFieldContainer[BillUtilitySettings]'
    repo_man_due_time: 'int'  # uint64
    situation_new_entries: 'RepeatedCompositeFieldContainer[SituationNewEntry]'
    gameplay_scenario_tracker: 'GameplayScenarioTrackerData'
    story_progression_tracker: 'PersistableStoryProgressionTracker'
    non_housing_costs_owed: 'int'  # int64
    housing_costs_owed: 'int'  # int64
    rent_late_timer: 'int'  # uint64
    rent_warning_timer: 'int'  # uint64
    sim_life_span_on_last_game_save: 'GameplayHouseholdData.SimLifeSpan'
    household_pivotal_moment_tracker: 'HouseholdPivotalMomentTracker'


class SituationEarnedMedals(Message):
    # __init__
    situation_id: 'int'  # fixed uint64
    medal: 'int'  # uint32


class SituationNewEntry(Message):
    # __init__
    situation_id: 'int'  # fixed uint64
    new_entry: 'bool'


class CollectionData(Message):
    # __init__
    collectible_def_id: 'int'  # uint64
    collection_id: 'int'  # uint64
    new: 'bool'
    quality: 'int'  # uint32
    icon_info: 'IconInfo'
    order_discovered: 'int'  # uint32


class RetailData(Message):
    class RetailDataPayroll():
        # __init__
        sim_id: 'int'  # fixed uint64
        clock_in_time: 'int'  # uint64
        payroll_data: 'RepeatedCompositeFieldContainer[RetailData.RetailDataPayroll.RetailDataPayrollEntry]'
        career_level_guid: 'int'  # fixed uint64
        hours_worked: 'float'  # float64

    class RetailFundsCategoryEntry():
        # __init__
        funds_category: 'int'  # uint32
        amount: 'int'  # int32

    # __init__
    retail_zone_id: 'int'  # fixed uint64
    employee_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    is_open: 'bool'
    markup: 'float'  # float32
    funds: 'int'  # int32
    employee_uniform_data_male: 'MannequinSimData'
    employee_uniform_data_female: 'MannequinSimData'
    employee_payroll: 'RepeatedCompositeFieldContainer[RetailData.RetailDataPayroll]'
    open_time: 'int'  # uint64
    grand_opening: 'bool'
    funds_category_tracker_data: 'RepeatedCompositeFieldContainer[RetailData.RetailFundsCategoryEntry]'
    daily_revenue: 'int'  # int32
    daily_items_sold: 'int'  # int32
    daily_employee_wages: 'int'  # int32
    daily_household_employee_wages: 'int'  # int32
    sim_id: 'int'  # fixed uint64
    clock_in_time: 'int'  # uint64
    payroll_data: 'RepeatedCompositeFieldContainer[RetailData.RetailDataPayroll.RetailDataPayrollEntry]'
    career_level_guid: 'int'  # fixed uint64
    hours_worked: 'float'  # float64
    funds_category: 'int'  # uint32
    amount: 'int'  # int32


class PersistableClubService(Message):
    # __init__
    has_seeded_clubs: 'bool'
    club_count: 'int'  # uint32
    clubs: 'RepeatedCompositeFieldContainer[Club]'


class Club(Message):
    class ClubOutfitSetting(IntEnum):
        NO_OUTFIT: 'Club.ClubOutfitSetting' = 0
        STYLE: 'Club.ClubOutfitSetting' = 1
        COLOR: 'Club.ClubOutfitSetting' = 2
        OUTFIT_OVERRIDE: 'Club.ClubOutfitSetting' = 3

    NO_OUTFIT = ClubOutfitSetting.NO_OUTFIT
    STYLE = ClubOutfitSetting.STYLE
    COLOR = ClubOutfitSetting.COLOR
    OUTFIT_OVERRIDE = ClubOutfitSetting.OUTFIT_OVERRIDE

    class ClubHangoutSetting(IntEnum):
        NO_HANGOUT: 'Club.ClubHangoutSetting' = 0
        VENUE: 'Club.ClubHangoutSetting' = 1
        LOT: 'Club.ClubHangoutSetting' = 2

    NO_HANGOUT = ClubHangoutSetting.NO_HANGOUT
    VENUE = ClubHangoutSetting.VENUE
    LOT = ClubHangoutSetting.LOT

    # __init__
    club_id: 'int'  # uint64
    name: 'str'
    icon: 'ResourceKey'
    description: 'str'
    invite_only: 'bool'
    leader: 'int'  # fixed uint64
    members: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    venue_type: 'ResourceKey'
    membership_criteria: 'RepeatedCompositeFieldContainer[ClubCriteria]'
    club_rules: 'RepeatedCompositeFieldContainer[ClubConductRule]'
    associated_color: 'int'  # uint32
    club_seed: 'ResourceKey'
    bucks_data: 'RepeatedCompositeFieldContainer[BucksData]'
    associated_style: 'int'  # uint32
    club_uniform_adult_male: 'MannequinSimData'
    club_uniform_child_male: 'MannequinSimData'
    club_uniform_adult_female: 'MannequinSimData'
    club_uniform_child_female: 'MannequinSimData'
    outfit_setting: 'Club.ClubOutfitSetting'
    member_cap: 'int'  # uint32
    recent_members: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    hangout_setting: 'Club.ClubHangoutSetting'
    hangout_zone_id: 'int'  # fixed uint64


class PersistableSocialMediaService(Message):
    # __init__
    post_entries: 'RepeatedCompositeFieldContainer[SocialMediaPostEntry]'
    direct_messages: 'RepeatedCompositeFieldContainer[SocialMediaMessageEntry]'
    sims_with_new_posts: 'RepeatedCompositeFieldContainer[int]'  # uint64
    sims_with_new_messages: 'RepeatedCompositeFieldContainer[int]'  # uint64


class SocialMediaPostEntry(Message):
    # __init__
    sim_id: 'int'  # uint64
    posts: 'RepeatedCompositeFieldContainer[SocialMediaPost]'


class SocialMediaMessageEntry(Message):
    # __init__
    sim_id: 'int'  # uint64
    messages: 'RepeatedCompositeFieldContainer[SocialMediaDirectMessage]'


class SocialMediaDirectMessage(Message):
    # __init__
    message_id: 'int'  # uint64
    message_post: 'SocialMediaPost'
    reply_post: 'SocialMediaPost'


class SocialMediaPost(Message):
    # __init__
    post_id: 'int'  # uint64
    author_sim_id: 'int'  # fixed uint64
    target_sim_id: 'int'  # fixed uint64
    narrative: 'int'  # uint32
    post_type: 'int'  # uint32
    post_time: 'int'  # uint64
    post_text: 'LocalizedString'
    reactions: 'RepeatedCompositeFieldContainer[SocialMediaReaction]'


class SocialMediaReaction(Message):
    # __init__
    narrative_type: 'int'  # uint32
    polarity_type: 'int'  # uint32
    count: 'int'  # uint32
    reacted_sims: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class ServiceNpcRecord(Message):
    # __init__
    service_type: 'int'  # uint64
    preferred_sim_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    fired_sim_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    hired: 'bool'
    time_last_started_service: 'int'  # uint64
    recurring: 'bool'
    time_last_finished_service: 'int'  # uint64
    user_specified_data_id: 'int'  # uint64
    user_specified_data_selection: 'RepeatedCompositeFieldContainer[int]'  # uint64
    user_specified_data_selection_count: 'RepeatedCompositeFieldContainer[int]'  # uint64
    hiring_sim_id: 'int'  # uint64


class AdditionalBillCost(Message):
    # __init__
    bill_source: 'int'  # uint32
    cost: 'int'  # uint64


class CurrentBillStatisticDelta(Message):
    # __init__
    stat_id: 'int'  # fixed uint64
    delta: 'float'  # float32


class CurrentBillDetail(Message):
    # __init__
    utility: 'int'  # uint64
    billable_amount: 'int'  # int64
    statistic_deltas: 'RepeatedCompositeFieldContainer[CurrentBillStatisticDelta]'
    net_consumption: 'float'  # float32


class BillUtilitySettings(Message):
    # __init__
    utility: 'int'  # uint64
    end_of_bill_action: 'int'  # uint32


class PersistableStoryProgressionParticipant(Message):
    # __init__
    participant_type: 'int'  # uint32
    participant: 'int'  # uint64
    participant_str: 'str'
    participant_loc_str: 'LocalizedString'


class PersistableDramaNode(Message):
    # __init__
    uid: 'int'  # fixed uint64
    node_type: 'int'  # fixed uint64
    receiver_sim_id: 'int'  # fixed uint64
    receiver_score: 'float'  # float32
    sender_sim_id: 'int'  # fixed uint64
    sender_score: 'float'  # float32
    selected_time: 'int'  # uint64
    custom_data: 'bytes'
    picked_sim_id: 'int'  # fixed uint64
    club_id: 'int'  # uint64
    stored_situation: 'SituationSeedData'
    story_progression_participants: 'RepeatedCompositeFieldContainer[PersistableStoryProgressionParticipant]'


class PersistableCallToActionService(Message):
    # __init__
    permanently_disabled_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class PersistableLandlordService(Message):
    # __init__
    landlord_id: 'int'  # fixed uint64


class PersistableTrendService(Message):
    # __init__
    current_trend_tags: 'RepeatedCompositeFieldContainer[int]'  # uint32
    next_update_ticks: 'int'  # uint64


class FashionMarketplaceSoldOutfits(Message):
    # __init__
    sim_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    outfit_info_data: 'MannequinSimData'


class PersistableFashionTrendService(Message):
    # __init__
    thrift_store_inventory: 'RepeatedCompositeFieldContainer[int]'  # uint64
    thrift_store_mannequin: 'MannequinSimData'
    next_trend_shift_ticks: 'int'  # uint64
    commodity_tracker: 'PersistableCommodityTracker'
    statistics_tracker: 'PersistableStatisticsTracker'
    sold_fashion_outfits: 'RepeatedCompositeFieldContainer[FashionMarketplaceSoldOutfits]'


class CooldownDramaNode(Message):
    # __init__
    node_type: 'int'  # fixed uint64
    completed_time: 'int'  # uint64


class DramaNodeCooldownGroup(Message):
    # __init__
    group: 'int'  # uint64
    completed_time: 'int'  # uint64


class PersistableDramaScheduleService(Message):
    # __init__
    drama_nodes: 'RepeatedCompositeFieldContainer[PersistableDramaNode]'
    cooldown_nodes: 'RepeatedCompositeFieldContainer[CooldownDramaNode]'
    running_nodes: 'RepeatedCompositeFieldContainer[PersistableDramaNode]'
    drama_nodes_on_permanent_cooldown: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    startup_drama_node_buckets_used: 'RepeatedCompositeFieldContainer[int]'  # uint64
    cooldown_groups: 'RepeatedCompositeFieldContainer[DramaNodeCooldownGroup]'
    cooldown_groups_on_permanent_cooldown: 'RepeatedCompositeFieldContainer[int]'  # uint64


class PersistableRelationshipBitLock(Message):
    # __init__
    relationship_bit_lock_type: 'int'  # fixed uint64
    locked_time: 'int'  # uint64


class PersistableUnidirectionalRelationshipData(Message):
    # __init__
    bits: 'RepeatedCompositeFieldContainer[int]'  # uint64
    timeouts: 'RepeatedCompositeFieldContainer[Timeout]'
    knowledge: 'SimKnowledge'
    bit_added_buffs: 'RepeatedCompositeFieldContainer[int]'  # uint64
    relationship_bit_locks: 'RepeatedCompositeFieldContainer[PersistableRelationshipBitLock]'
    sentiment_proximity_cooldown_end: 'int'  # uint64
    tracks: 'RepeatedCompositeFieldContainer[PersistableRelationshipTrack]'


class PersistableBidirectionalRelationshipData(Message):
    # __init__
    bits: 'RepeatedCompositeFieldContainer[int]'  # uint64
    timeouts: 'RepeatedCompositeFieldContainer[Timeout]'
    tracks: 'RepeatedCompositeFieldContainer[PersistableRelationshipTrack]'
    relationship_bit_locks: 'RepeatedCompositeFieldContainer[PersistableRelationshipBitLock]'
    compatibility_score: 'float'  # float32
    compatibility_level: 'int'  # uint32


class PersistableRelationshipLabelData(Message):
    # __init__
    label: 'str'
    icon: 'ResourceKey'


class PersistableServiceRelationship(Message):
    # __init__
    sim_id_a: 'int'  # uint64
    sim_id_b: 'int'  # uint64
    bidirectional_relationship_data: 'PersistableBidirectionalRelationshipData'
    sim_a_relationship_data: 'PersistableUnidirectionalRelationshipData'
    sim_b_relationship_data: 'PersistableUnidirectionalRelationshipData'
    last_update_time: 'int'  # uint64
    target_object_id: 'int'  # uint64
    target_object_manager_id: 'int'  # uint64
    target_object_instance_id: 'int'  # uint64
    object_relationship_name: 'str'
    relationship_label_data: 'PersistableRelationshipLabelData'
    hidden: 'bool'


class PersistableRelationshipService(Message):
    # __init__
    relationships: 'RepeatedCompositeFieldContainer[PersistableServiceRelationship]'
    object_relationships: 'RepeatedCompositeFieldContainer[PersistableServiceRelationship]'


class PersistableGlobalPolicy(Message):
    # __init__
    progress_state: 'int'  # uint32
    progress_value: 'int'  # uint32
    decay_days: 'int'  # uint32
    snippet: 'int'  # uint64


class PersistableGlobalPolicyBillReduction(Message):
    # __init__
    bill_reduction_reason: 'int'  # uint32
    bill_reduction_amount: 'float'  # float32


class PersistableGlobalUtilityEffect(Message):
    # __init__
    global_policy_snippet_guid64: 'int'  # uint64


class PersistableGlobalPolicyService(Message):
    # __init__
    global_policies: 'RepeatedCompositeFieldContainer[PersistableGlobalPolicy]'
    bill_reductions: 'RepeatedCompositeFieldContainer[PersistableGlobalPolicyBillReduction]'
    utility_effects: 'RepeatedCompositeFieldContainer[PersistableGlobalUtilityEffect]'


class AdoptableSimData(Message):
    # __init__
    adoptable_sim_id: 'int'  # fixed uint64
    creation_time: 'int'  # uint64


class PersistableAdoptionService(Message):
    # __init__
    adoptable_sim_data: 'RepeatedCompositeFieldContainer[AdoptableSimData]'


class HiddenSimData(Message):
    # __init__
    sim_id: 'int'  # uint64
    away_action: 'int'  # uint64


class PersistableHiddenSimService(Message):
    # __init__
    hidden_sim_data: 'RepeatedCompositeFieldContainer[HiddenSimData]'


class PersistableSeasonService(Message):
    # __init__
    current_season: 'int'  # uint64
    season_start_time: 'int'  # uint64


class DecorationState(Message):
    # __init__
    decoration_type_id: 'int'  # uint64
    decorated_locations: 'RepeatedCompositeFieldContainer[DecoratedLocation]'


class LotDecorationSetting(Message):
    # __init__
    zone_id: 'int'  # uint64
    decoration_states: 'RepeatedCompositeFieldContainer[DecorationState]'
    active_decoration_state: 'int'  # uint64


class DecoratedLocation(Message):
    # __init__
    location: 'int'  # uint32
    decoration: 'int'  # uint64


class HolidayDecorationSetting(Message):
    # __init__
    holiday: 'int'  # uint64
    decoration_preset: 'int'  # uint64


class WorldDecorationSetting(Message):
    # __init__
    world_id: 'int'  # uint64
    set_decorations: 'int'  # uint64


class PersistableLotDecorationService(Message):
    # __init__
    lot_decorations: 'RepeatedCompositeFieldContainer[LotDecorationSetting]'
    holiday_preferences: 'RepeatedCompositeFieldContainer[HolidayDecorationSetting]'
    world_decorations_set: 'RepeatedCompositeFieldContainer[WorldDecorationSetting]'


class HolidayTimeData(Message):
    # __init__
    holiday_id: 'int'  # fixed uint64
    day: 'int'  # uint32
    season: 'int'  # uint32


class HolidayCalendar(Message):
    # __init__
    season_length: 'int'  # uint32
    holidays: 'RepeatedCompositeFieldContainer[HolidayTimeData]'


class PersistableHolidayService(Message):
    # __init__
    holidays: 'RepeatedCompositeFieldContainer[Holiday]'
    calendars: 'RepeatedCompositeFieldContainer[HolidayCalendar]'


class StyleOutfitInfo(Message):
    # __init__
    outfit_info_data: 'MannequinSimData'


class PersistableStyleService(Message):
    # __init__
    outfit_infos: 'RepeatedCompositeFieldContainer[StyleOutfitInfo]'


class RabbitHoleData(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    rabbit_hole_id: 'int'  # uint64
    time_remaining: 'int'  # uint64
    linked_sim_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    picked_stat_id: 'int'  # uint64
    rabbit_hole_instance_id: 'int'  # uint64
    linked_rabbit_hole_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    phase: 'int'  # uint64
    career_uid: 'int'  # uint64
    all_participant_sim_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64


class PersistableRabbitHoleService(Message):
    # __init__
    rabbit_holes: 'RepeatedCompositeFieldContainer[RabbitHoleData]'


class HorseCompetitionData(Message):
    # __init__
    competition_id: 'int'  # uint64
    rabbit_hole_id: 'int'  # uint64
    sim_id: 'int'  # fixed uint64
    horse_id: 'int'  # fixed uint64


class HorseCompetitionHighestPlacementData(Message):
    # __init__
    competition_id: 'int'  # uint64
    highest_placement: 'int'  # uint64


class HorseCompetitionHorsePlacementData(Message):
    # __init__
    horse_id: 'int'  # fixed uint64
    placements: 'RepeatedCompositeFieldContainer[HorseCompetitionHighestPlacementData]'


class PersistableHorseCompetitionService(Message):
    # __init__
    competitions: 'RepeatedCompositeFieldContainer[HorseCompetitionData]'
    horse_placements: 'RepeatedCompositeFieldContainer[HorseCompetitionHorsePlacementData]'


class NarrativeProgressionData(Message):
    # __init__
    event: 'int'  # uint32
    progression: 'int'  # uint64


class NarrativeData(Message):
    # __init__
    narrative_id: 'int'  # uint64
    introduction_shown: 'bool'
    narrative_progression_entries: 'RepeatedCompositeFieldContainer[NarrativeProgressionData]'


class NarrativeLayerData(Message):
    # __init__
    street_id: 'int'  # uint64
    layers: 'RepeatedCompositeFieldContainer[int]'  # uint64


class PersistableNarrativeService(Message):
    # __init__
    active_narratives: 'RepeatedCompositeFieldContainer[int]'  # uint64
    completed_narratives: 'RepeatedCompositeFieldContainer[int]'  # uint64
    narratives: 'RepeatedCompositeFieldContainer[NarrativeData]'
    layer_data: 'RepeatedCompositeFieldContainer[NarrativeLayerData]'
    streets_need_cleanup: 'bool'
    streets_to_cleanup: 'RepeatedCompositeFieldContainer[int]'  # uint64


class PersistableOrganizationService(Message):
    # __init__
    organizations: 'RepeatedCompositeFieldContainer[OrganizationData]'
    org_festival_events: 'RepeatedCompositeFieldContainer[OrganizationEventData]'
    org_venue_events: 'RepeatedCompositeFieldContainer[OrganizationEventData]'
    schedule_cancelled_event_data: 'RepeatedCompositeFieldContainer[ScheduleEventCallbackData]'


class ScheduleEventCallbackData(Message):
    # __init__
    org_event_id: 'int'  # uint64
    schedule_venue_event_time: 'int'  # uint64


class OrganizationEventData(Message):
    # __init__
    org_uid: 'int'  # uint64
    org_name: 'str'


class OrganizationData(Message):
    # __init__
    organization_id: 'int'  # uint64
    organization_members: 'RepeatedCompositeFieldContainer[OrganizationMemberData]'


class OrganizationMemberData(Message):
    # __init__
    organization_member_id: 'int'  # uint64


class PersistableObjectLocator(Message):
    # __init__
    object: 'bytes'
    zone_id: 'int'  # fixed uint64
    open_street_id: 'int'  # fixed uint64
    sim_id: 'int'  # fixed uint64
    household_id: 'int'  # fixed uint64
    time_before_lost: 'float'  # float32
    time_stamp: 'float'  # float32
    return_to_individual_sim: 'bool'


class ClonedObjectsLocator(Message):
    # __init__
    zone_id: 'int'  # fixed uint64
    open_street_id: 'int'  # fixed uint64
    object_id: 'int'  # fixed uint64


class PersistableObjectLostAndFound(Message):
    # __init__
    locators: 'RepeatedCompositeFieldContainer[PersistableObjectLocator]'
    clones_to_delete: 'RepeatedCompositeFieldContainer[ClonedObjectsLocator]'


class PersistableCullingServiceInteractingSim(Message):
    # __init__
    sim_id: 'int'  # uint64
    time_stamp: 'float'  # float32


class PersistableCullingService(Message):
    # __init__
    interacting_sims: 'RepeatedCompositeFieldContainer[PersistableCullingServiceInteractingSim]'
    sims_to_cull: 'RepeatedCompositeFieldContainer[int]'  # uint64


class PersistableUniversityStoryProgressionAction(Message):
    # __init__
    next_update_time: 'int'  # uint64


class PersistableStoryProgressionService(Message):
    # __init__
    university_action: 'PersistableUniversityStoryProgressionAction'


class PersistableCivicPolicyCustomData(Message):
    # __init__
    policy_id: 'int'  # uint64
    custom_data: 'bytes'


class PersistableDefaultConditionalLayerData(Message):
    # __init__
    layer: 'int'  # uint64
    policies: 'RepeatedCompositeFieldContainer[int]'  # uint64


class PersistableCivicPolicyProviderData(Message):
    # __init__
    policy_data: 'RepeatedCompositeFieldContainer[PersistableCivicPolicyCustomData]'
    commodity_tracker: 'PersistableCommodityTracker'
    statistics_tracker: 'PersistableStatisticsTracker'
    ranked_statistic_tracker: 'PersistableRankedStatisticTracker'
    balloted_policy_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    up_for_repeal_policy_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    loaded_conditional_layers: 'RepeatedCompositeFieldContainer[int]'  # uint64
    turned_off_default_conditional_layers: 'RepeatedCompositeFieldContainer[PersistableDefaultConditionalLayerData]'
    requires_initial_layer_setup: 'bool'


class PersistableStreetEcoFootprintData(Message):
    # __init__
    current_eco_footprint_state: 'EcoFootprintStateType'
    effects_are_simulated: 'bool'
    convergence: 'float'  # float32


class PersistableStreetData(Message):
    # __init__
    street_id: 'int'  # uint64
    civic_provider_data: 'PersistableCivicPolicyProviderData'
    street_eco_footprint_data: 'PersistableStreetEcoFootprintData'


class PersistableStreetService(Message):
    # __init__
    street_data: 'RepeatedCompositeFieldContainer[PersistableStreetData]'


class PersistableCivicPolicyStreetPolicyData(Message):
    # __init__
    enacted: 'bool'
    effect_data: 'RepeatedCompositeFieldContainer[PersistableCivicPolicyCustomData]'


class PersistableCivicPolicyStreetConditionalLayerEffectData(Message):
    # __init__
    start_tick: 'int'  # uint64


class PersistableRegionData(Message):
    # __init__
    region_id: 'int'  # uint64
    commodity_tracker: 'PersistableCommodityTracker'


class PersistableRegionService(Message):
    # __init__
    region_data: 'RepeatedCompositeFieldContainer[PersistableRegionData]'


class PersistableLifestyleService(Message):
    # __init__
    has_seen_daily_cap_notification: 'bool'
    has_seen_in_progress_notification: 'bool'
    has_seen_hidden_notification: 'bool'
    hidden_lifestyles: 'RepeatedCompositeFieldContainer[int]'  # uint64


class PersistableABTestService(Message):
    class ABTestState(IntEnum):
        COMPLETED: 'PersistableABTestService.ABTestState' = 0
        ACTIVE: 'PersistableABTestService.ABTestState' = 1

    COMPLETED = ABTestState.COMPLETED
    ACTIVE = ABTestState.ACTIVE

    class ABTestData():
        # __init__
        name: 'str'
        state: 'PersistableABTestService.ABTestData.ABTestState'

        class ABTestState(IntEnum):
            COMPLETED: 'PersistableABTestService.ABTestData.ABTestState' = 0
            ACTIVE: 'PersistableABTestService.ABTestData.ABTestState' = 1

    # __init__
    ab_test_data: 'RepeatedCompositeFieldContainer[PersistableABTestService.ABTestData]'
    name: 'str'
    state: 'PersistableABTestService.ABTestData.ABTestState'


class PersistableLiveEventService(Message):
    class LiveEventState(IntEnum):
        COMPLETED: 'PersistableLiveEventService.LiveEventState' = 0
        ACTIVE: 'PersistableLiveEventService.LiveEventState' = 1

    COMPLETED = LiveEventState.COMPLETED
    ACTIVE = LiveEventState.ACTIVE

    class LiveEventData():
        # __init__
        event_id: 'int'  # uint32
        state: 'PersistableLiveEventService.LiveEventData.LiveEventState'

        class LiveEventState(IntEnum):
            COMPLETED: 'PersistableLiveEventService.LiveEventData.LiveEventState' = 0
            ACTIVE: 'PersistableLiveEventService.LiveEventData.LiveEventState' = 1

    # __init__
    live_event_data: 'RepeatedCompositeFieldContainer[PersistableLiveEventService.LiveEventData]'
    event_id: 'int'  # uint32
    state: 'PersistableLiveEventService.LiveEventData.LiveEventState'


class PersistableAssignedAnimals(Message):
    # __init__
    obj_id: 'int'  # uint64
    home_id: 'int'  # uint64
    animal_type: 'int'  # uint64
    owner_household_id: 'int'  # uint64
    zone_id: 'int'  # uint64
    open_street_id: 'int'  # uint64


class PersistableAnimalService(Message):
    # __init__
    animal_data: 'RepeatedCompositeFieldContainer[PersistableAssignedAnimals]'


class PresistablePurchasePickerGroupItem(Message):
    # __init__
    quantity: 'int'  # uint32
    object_definition: 'int'  # uint64


class PersistablePurchasePickerGroupData(Message):
    # __init__
    timestamp: 'int'  # uint64
    items: 'RepeatedCompositeFieldContainer[PresistablePurchasePickerGroupItem]'
    picker_group: 'int'  # uint32


class PersistablePurchasePickerService(Message):
    # __init__
    picker_group_data: 'RepeatedCompositeFieldContainer[PersistablePurchasePickerGroupData]'


class PersistableLunarCycleService(Message):
    # __init__
    current_phase: 'int'  # uint32
    phase_start_time: 'int'  # uint64


class PersistableClanService(Message):
    # __init__
    clan_leaders: 'RepeatedCompositeFieldContainer[ClanLeaderData]'
    clan_members: 'RepeatedCompositeFieldContainer[ClanMembersData]'


class ClanLeaderData(Message):
    # __init__
    clan_guid: 'int'  # uint64
    leader_sim_id: 'int'  # fixed uint64


class ClanMembersData(Message):
    # __init__
    clan_guid: 'int'  # uint64
    member_sim_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class PersistableGraduationService(Message):
    # __init__
    graduating_sim_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    waiting_to_graduate_sim_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    current_valedictorian_id: 'int'  # fixed uint64
    waiting_valedictorian_id: 'int'  # fixed uint64


class PersistableVenueGameService(Message):
    # __init__
    venue_restore_zone_id: 'int'  # uint64
    venue_restore_alarm_time: 'int'  # uint64
    venue_restore_type_id: 'int'  # uint64


class PersistablePromService(Message):
    # __init__
    prom_attendee_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    cleanup_prom_alarm_time: 'int'  # uint64
    prom_zone_id: 'int'  # uint64
    skipping_prom_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class PersistableSimSecretsService(Message):
    # __init__
    unavailable_secrets: 'RepeatedCompositeFieldContainer[int]'  # uint64


class PersistableCareerService(Message):
    # __init__
    subvenue_zone_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    disabled_gig_data: 'RepeatedCompositeFieldContainer[GigPickerDisabledGigData]'
    gig_associated_sim_data: 'RepeatedCompositeFieldContainer[GigPickerAssociatedSimData]'


class GigPickerDisabledGigData(Message):
    # __init__
    gig_uid: 'int'  # uint64
    sim_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64


class GigPickerAssociatedSimData(Message):
    # __init__
    gig_uid: 'int'  # uint64
    associated_sim_id: 'int'  # uint64


class ActivationTriggerStatus(Message):
    # __init__
    trigger_id: 'int'  # uint32
    satisfied: 'bool'


class PivotalMoment(Message):
    # __init__
    household_id: 'int'  # fixed uint64
    remaining_ticks: 'int'  # uint64
    situation_seed: 'SituationSeedData'
    activation_status: 'int'  # uint32
    triggers: 'RepeatedCompositeFieldContainer[ActivationTriggerStatus]'
    pivotal_moment_id: 'int'  # uint64
    activation_trigger_id: 'int'  # uint64


class PivotalMomentsData(Message):
    # __init__
    pivotal_moments: 'RepeatedCompositeFieldContainer[PivotalMoment]'


class PersistableTutorialService(Message):
    # __init__
    pivotal_moments: 'RepeatedCompositeFieldContainer[PivotalMoment]'


class UserAccountGameplayData(Message):
    # __init__
    key: 'str'
    value: 'str'


class UserAccountStoredGameplayData(Message):
    # __init__
    stored_data: 'RepeatedCompositeFieldContainer[UserAccountGameplayData]'


class GameplaySaveSlotData(Message):
    # __init__
    world_game_time: 'int'  # uint64
    travel_situation_seed: 'SituationSeedData'
    camera_data: 'GameplayCameraData'
    is_phone_silenced: 'bool'
    career_choices_seed: 'int'  # fixed uint64
    enable_autogeneration_same_sex_preference: 'bool'
    club_service: 'PersistableClubService'
    drama_schedule_service: 'PersistableDramaScheduleService'
    relgraph_service: 'PersistableRelgraphService'
    business_service_data: 'BusinessServiceData'
    call_to_action_service: 'PersistableCallToActionService'
    once_only_drama_nodes: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    relationship_service: 'PersistableRelationshipService'
    adoption_service: 'PersistableAdoptionService'
    hidden_sim_service: 'PersistableHiddenSimService'
    season_service: 'PersistableSeasonService'
    weather_service: 'PersistableWeatherService'
    lot_decoration_service: 'PersistableLotDecorationService'
    holiday_service: 'PersistableHolidayService'
    style_service: 'PersistableStyleService'
    trend_service: 'PersistableTrendService'
    rabbit_hole_service: 'PersistableRabbitHoleService'
    narrative_service: 'PersistableNarrativeService'
    object_lost_and_found: 'PersistableObjectLostAndFound'
    landlord_service: 'PersistableLandlordService'
    global_policy_service: 'PersistableGlobalPolicyService'
    roommate_service: 'PersistableRoommateService'
    organization_service: 'PersistableOrganizationService'
    culling_service: 'PersistableCullingService'
    story_progression_service: 'PersistableStoryProgressionService'
    street_service: 'PersistableStreetService'
    region_service: 'PersistableRegionService'
    lifestyle_service: 'PersistableLifestyleService'
    ab_test_service: 'PersistableABTestService'
    live_event_service: 'PersistableLiveEventService'
    animal_service: 'PersistableAnimalService'
    purchase_picker_service: 'PersistablePurchasePickerService'
    calendar_service: 'PersistableCalendarService'
    social_media_service: 'PersistableSocialMediaService'
    graduation_service: 'PersistableGraduationService'
    venue_game_service: 'PersistableVenueGameService'
    prom_service: 'PersistablePromService'
    fashion_trend_service: 'PersistableFashionTrendService'
    lunar_cycle_service: 'PersistableLunarCycleService'
    clan_service: 'PersistableClanService'
    career_service: 'PersistableCareerService'
    horse_competition_service: 'PersistableHorseCompetitionService'
    tutorial_service: 'PersistableTutorialService'
    sim_secrets_service: 'PersistableSimSecretsService'
    multi_unit_event_service: 'PersistableMultiUnitEventService'
    multi_unit_ownership_service: 'PersistableMultiUnitOwnershipService'
    tenant_applications_data: 'TenantApplicationServicePersistence'
    matchmaking_service: 'PersistableMatchmakingService'
    ui_dialog_service: 'PersistableUiDialogService'
    will_service: 'PersistableWillService'
    wisp_service: 'PersistableWispService'
    imaginary_friend_service: 'PersistableImaginaryFriendService'
    custom_schedule_service: 'PersistableCustomScheduleService'


class PersistableRelgraphService(Message):
    # __init__
    relgraph_data: 'bytes'


class GameplayCameraData(Message):
    # __init__
    target_id: 'int'  # fixed uint64
    target_position: 'Vector3'
    camera_position: 'Vector3'
    follow_mode: 'bool'
    zone_id: 'int'  # fixed uint64
    household_id: 'int'  # fixed uint64


class GameplayNeighborhoodData(Message):
    class NpcPopulationState(IntEnum):
        NOT_STARTED: 'GameplayNeighborhoodData.NpcPopulationState' = 0
        STARTED: 'GameplayNeighborhoodData.NpcPopulationState' = 1
        DIALOG_DISPLAYED: 'GameplayNeighborhoodData.NpcPopulationState' = 2
        COMPLETED: 'GameplayNeighborhoodData.NpcPopulationState' = 3

    NOT_STARTED = NpcPopulationState.NOT_STARTED
    STARTED = NpcPopulationState.STARTED
    DIALOG_DISPLAYED = NpcPopulationState.DIALOG_DISPLAYED
    COMPLETED = NpcPopulationState.COMPLETED

    # __init__
    npc_population_state: 'GameplayNeighborhoodData.NpcPopulationState'


class GameplayAccountData(Message):
    # __init__
    achievement_data: 'AccountEventDataTracker'
    gameplay_options: 'GameplayOptions'
    game_notification: 'RepeatedCompositeFieldContainer[UiDialogMessage]'
    cheats_enabled: 'bool'
    cheats_ever_enabled: 'bool'


class AccountEventDataTracker(Message):
    # __init__
    milestones_completed: 'RepeatedCompositeFieldContainer[int]'  # uint32
    objectives_completed: 'RepeatedCompositeFieldContainer[int]'  # uint32
    data: 'EventDataObject'
    milestone_completion_counts: 'RepeatedCompositeFieldContainer[MilestoneCompletionCount]'


class GameplayOptions(Message):
    class AutonomyLevel(IntEnum):
        OFF: 'GameplayOptions.AutonomyLevel' = 0
        LIMITED: 'GameplayOptions.AutonomyLevel' = 1
        MEDIUM: 'GameplayOptions.AutonomyLevel' = 2
        FULL: 'GameplayOptions.AutonomyLevel' = 3
        UNDEFINED: 'GameplayOptions.AutonomyLevel' = 4

    OFF = AutonomyLevel.OFF
    LIMITED = AutonomyLevel.LIMITED
    MEDIUM = AutonomyLevel.MEDIUM
    FULL = AutonomyLevel.FULL
    UNDEFINED = AutonomyLevel.UNDEFINED

    class SimLifeSpan(IntEnum):
        SHORT: 'GameplayOptions.SimLifeSpan' = 0
        NORMAL: 'GameplayOptions.SimLifeSpan' = 1
        LONG: 'GameplayOptions.SimLifeSpan' = 2
        UNKNOWN: 'GameplayOptions.SimLifeSpan' = 3

    SHORT = SimLifeSpan.SHORT
    NORMAL = SimLifeSpan.NORMAL
    LONG = SimLifeSpan.LONG
    UNKNOWN = SimLifeSpan.UNKNOWN

    class SimAgeEnabled(IntEnum):
        DISABLED: 'GameplayOptions.SimAgeEnabled' = 0
        ENABLED: 'GameplayOptions.SimAgeEnabled' = 1
        FOR_ACTIVE_FAMILY: 'GameplayOptions.SimAgeEnabled' = 2

    DISABLED = SimAgeEnabled.DISABLED
    ENABLED = SimAgeEnabled.ENABLED
    FOR_ACTIVE_FAMILY = SimAgeEnabled.FOR_ACTIVE_FAMILY

    class SeasonLength(IntEnum):
        NORMAL_SEASON: 'GameplayOptions.SeasonLength' = 0
        LONG_SEASON: 'GameplayOptions.SeasonLength' = 1
        VERY_LONG_SEASON: 'GameplayOptions.SeasonLength' = 2

    NORMAL_SEASON = SeasonLength.NORMAL_SEASON
    LONG_SEASON = SeasonLength.LONG_SEASON
    VERY_LONG_SEASON = SeasonLength.VERY_LONG_SEASON

    class WeatherOption(IntEnum):
        WEATHER_ENABLED: 'GameplayOptions.WeatherOption' = 0
        DISABLE_STORMS: 'GameplayOptions.WeatherOption' = 1
        WEATHER_DISABLED: 'GameplayOptions.WeatherOption' = 2

    WEATHER_ENABLED = WeatherOption.WEATHER_ENABLED
    DISABLE_STORMS = WeatherOption.DISABLE_STORMS
    WEATHER_DISABLED = WeatherOption.WEATHER_DISABLED

    class SeasonType(IntEnum):
        SUMMER: 'GameplayOptions.SeasonType' = 0
        FALL: 'GameplayOptions.SeasonType' = 1
        WINTER: 'GameplayOptions.SeasonType' = 2
        SPRING: 'GameplayOptions.SeasonType' = 3

    SUMMER = SeasonType.SUMMER
    FALL = SeasonType.FALL
    WINTER = SeasonType.WINTER
    SPRING = SeasonType.SPRING

    class LunarCycleLength(IntEnum):
        TWO_DAY: 'GameplayOptions.LunarCycleLength' = 0
        FOUR_DAY: 'GameplayOptions.LunarCycleLength' = 1
        FULL_LENGTH: 'GameplayOptions.LunarCycleLength' = 2
        DOUBLE_LENGTH: 'GameplayOptions.LunarCycleLength' = 3
        TRIPLE_LENGTH: 'GameplayOptions.LunarCycleLength' = 4

    TWO_DAY = LunarCycleLength.TWO_DAY
    FOUR_DAY = LunarCycleLength.FOUR_DAY
    FULL_LENGTH = LunarCycleLength.FULL_LENGTH
    DOUBLE_LENGTH = LunarCycleLength.DOUBLE_LENGTH
    TRIPLE_LENGTH = LunarCycleLength.TRIPLE_LENGTH

    class LunarPhaseLocked(IntEnum):
        NEW_MOON: 'GameplayOptions.LunarPhaseLocked' = 0
        WAXING_CRESCENT: 'GameplayOptions.LunarPhaseLocked' = 1
        FIRST_QUARTER: 'GameplayOptions.LunarPhaseLocked' = 2
        WAXING_GIBBOUS: 'GameplayOptions.LunarPhaseLocked' = 3
        FULL_MOON: 'GameplayOptions.LunarPhaseLocked' = 4
        WANING_GIBBOUS: 'GameplayOptions.LunarPhaseLocked' = 5
        THIRD_QUARTER: 'GameplayOptions.LunarPhaseLocked' = 6
        WANING_CRESCENT: 'GameplayOptions.LunarPhaseLocked' = 7
        NO_LUNAR_PHASE_LOCK: 'GameplayOptions.LunarPhaseLocked' = 8

    NEW_MOON = LunarPhaseLocked.NEW_MOON
    WAXING_CRESCENT = LunarPhaseLocked.WAXING_CRESCENT
    FIRST_QUARTER = LunarPhaseLocked.FIRST_QUARTER
    WAXING_GIBBOUS = LunarPhaseLocked.WAXING_GIBBOUS
    FULL_MOON = LunarPhaseLocked.FULL_MOON
    WANING_GIBBOUS = LunarPhaseLocked.WANING_GIBBOUS
    THIRD_QUARTER = LunarPhaseLocked.THIRD_QUARTER
    WANING_CRESCENT = LunarPhaseLocked.WANING_CRESCENT
    NO_LUNAR_PHASE_LOCK = LunarPhaseLocked.NO_LUNAR_PHASE_LOCK

    # __init__
    autonomy_level: 'GameplayOptions.AutonomyLevel'
    selected_sim_autonomy_enabled: 'bool'
    sim_life_span: 'GameplayOptions.SimLifeSpan'
    aging_enabled: 'bool'
    lessons_enabled: 'bool'
    tutorial_situation_enabled: 'bool'
    reset_lessons: 'bool'
    allow_aging: 'GameplayOptions.SimAgeEnabled'
    unplayed_aging_enabled: 'bool'
    npc_population_enabled: 'bool'
    max_player_population: 'int'  # uint32
    show_wants: 'bool'
    season_length: 'GameplayOptions.SeasonLength'
    rain_options: 'GameplayOptions.WeatherOption'
    snow_options: 'GameplayOptions.WeatherOption'
    temperature_effects_enabled: 'bool'
    initial_season: 'GameplayOptions.SeasonType'
    start_all_sims_opted_out_of_fame: 'bool'
    npc_civic_voting_enabled: 'bool'
    eco_footprint_gameplay_enabled: 'bool'
    build_eco_effects_enabled: 'bool'
    icy_conditions_enabled: 'bool'
    thunder_snow_storms_enabled: 'bool'
    lifestyles_effects_enabled: 'bool'
    dust_system_enabled: 'bool'
    creature_aging_enabled: 'bool'
    story_progression_effects_enabled: 'bool'
    restrict_npc_werewolves: 'bool'
    acne_enabled: 'bool'
    lunar_cycle_length: 'GameplayOptions.LunarCycleLength'
    lunar_phase_lock: 'GameplayOptions.LunarPhaseLocked'
    disable_lunar_effects: 'bool'
    npc_relationship_autonomy_enabled: 'bool'
    self_discovery_enabled: 'bool'
    career_lay_off_enabled: 'bool'
    multi_unit_events_enabled: 'bool'
    reset_pivotal_moments: 'bool'
    pivotal_moments_enabled: 'bool'
    matchmaking_gallery_sims_enabled: 'bool'
    matchmaking_occult_sims_enabled: 'bool'
    matchmaking_gallery_sims_favorites_only_enabled: 'bool'
    npc_autonomy_friendly_enabled: 'bool'
    npc_autonomy_romantic_enabled: 'bool'
    npc_autonomy_breakups_enabled: 'bool'
    automatic_death_inventory_handling_enabled: 'bool'
    heirloom_objects_enabled: 'bool'
    small_business_events_enabled: 'bool'
    burglar_enabled: 'bool'
    cheat_sheet_enabled: 'bool'
    guidance_auto_enabled: 'bool'
    restrict_npc_fairies: 'bool'
    balance_system_enabled: 'bool'
    luck_enabled: 'bool'
    ailments_enabled: 'bool'


class RestaurantZoneDirectorData(Message):
    class TableGroup():
        # __init__
        table_id: 'int'  # uint64
        sim_seats: 'RepeatedCompositeFieldContainer[RestaurantZoneDirectorData.TableGroup.SimSeat]'
        sim_id: 'int'  # uint64
        part_index: 'int'  # uint32

    class SavedDailySpecial():
        # __init__
        course_tag: 'int'  # uint32
        recipe_id: 'int'  # uint64

    class GroupOrder():
        # __init__
        order_id: 'int'  # uint32
        situation_id: 'int'  # fixed uint64
        order_status: 'int'  # uint32
        current_bucket: 'int'  # uint32
        table_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
        sim_orders: 'RepeatedCompositeFieldContainer[RestaurantZoneDirectorData.GroupOrder.FoodAndDrink]'
        assigned_waitstaff_id: 'int'  # fixed uint64
        assigned_chef_id: 'int'  # fixed uint64
        serving_object_id: 'int'  # fixed uint64
        is_complimentary: 'bool'
        sim_id: 'int'  # fixed uint64
        food_recipe_id: 'int'  # fixed uint64
        drink_recipe_id: 'int'  # fixed uint64
        recommendation_state: 'int'  # uint32

    # __init__
    table_group: 'RepeatedCompositeFieldContainer[RestaurantZoneDirectorData.TableGroup]'
    last_daily_special_absolute_day: 'int'  # int32
    saved_daily_specials: 'RepeatedCompositeFieldContainer[RestaurantZoneDirectorData.SavedDailySpecial]'
    group_orders: 'RepeatedCompositeFieldContainer[RestaurantZoneDirectorData.GroupOrder]'
    table_id: 'int'  # uint64
    sim_seats: 'RepeatedCompositeFieldContainer[RestaurantZoneDirectorData.TableGroup.SimSeat]'
    sim_id: 'int'  # uint64
    part_index: 'int'  # uint32
    course_tag: 'int'  # uint32
    recipe_id: 'int'  # uint64
    order_id: 'int'  # uint32
    situation_id: 'int'  # fixed uint64
    order_status: 'int'  # uint32
    current_bucket: 'int'  # uint32
    table_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    sim_orders: 'RepeatedCompositeFieldContainer[RestaurantZoneDirectorData.GroupOrder.FoodAndDrink]'
    assigned_waitstaff_id: 'int'  # fixed uint64
    assigned_chef_id: 'int'  # fixed uint64
    serving_object_id: 'int'  # fixed uint64
    is_complimentary: 'bool'
    sim_id: 'int'  # fixed uint64
    food_recipe_id: 'int'  # fixed uint64
    drink_recipe_id: 'int'  # fixed uint64
    recommendation_state: 'int'  # uint32


class ZoneDirectorCleanupActionData(Message):
    # __init__
    guid: 'int'  # uint32
    object_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    resource_keys: 'RepeatedCompositeFieldContainer[ResourceKey]'
    states: 'RepeatedCompositeFieldContainer[StateComponentState]'
    location: 'Location'


class ZoneDirectorSituationData(Message):
    # __init__
    situation_list_guid: 'int'  # uint32
    situation_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64


class ObjectBasedSituationZoneDirectorData(Message):
    # __init__
    object_tag: 'int'  # uint32
    situation_list_guid: 'int'  # uint32
    situation_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64


class ZoneDirectorData(Message):
    # __init__
    resource_key: 'ResourceKey'
    cleanup_actions: 'RepeatedCompositeFieldContainer[ZoneDirectorCleanupActionData]'
    situations: 'RepeatedCompositeFieldContainer[ZoneDirectorSituationData]'
    custom_data: 'bytes'
    restaurant_data: 'RestaurantZoneDirectorData'
    object_situations: 'RepeatedCompositeFieldContainer[ObjectBasedSituationZoneDirectorData]'


class VenueDataUpdate(Message):
    # __init__
    zone_id: 'int'  # fixed uint64
    venue_data: 'VenueData'


class VenueBusinessData(Message):
    # __init__
    business_rules: 'RepeatedCompositeFieldContainer[BusinessRule]'
    plex_rating_offset: 'int'  # int32


class VenueData(Message):
    # __init__
    background_situation_id: 'int'  # fixed uint64
    special_event_id: 'int'  # fixed uint64
    zone_director: 'ZoneDirectorData'
    civic_provider_data: 'PersistableCivicPolicyProviderData'
    business_data: 'VenueBusinessData'


class OpenStreetDirectorData(Message):
    # __init__
    resource_key: 'ResourceKey'
    created_objects: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    situation_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    custom_data: 'bytes'
    loaded_layers: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    situations: 'RepeatedCompositeFieldContainer[ZoneDirectorSituationData]'
    loaded_layer_guids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class ConditionalLayerInfo(Message):
    # __init__
    layer_hash: 'int'  # uint64
    object_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    conditional_layer: 'int'  # uint64


class ConditionalLayerServiceData(Message):
    # __init__
    layer_infos: 'RepeatedCompositeFieldContainer[ConditionalLayerInfo]'


class AmbientSourceData(Message):
    # __init__
    source_type: 'int'  # uint32
    situation_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    situations: 'RepeatedCompositeFieldContainer[ZoneDirectorSituationData]'


class AmbientServiceData(Message):
    # __init__
    sources: 'RepeatedCompositeFieldContainer[AmbientSourceData]'


class InteractionSaveData(Message):
    # __init__
    interaction: 'int'  # fixed uint64
    target_id: 'int'  # fixed uint64
    source: 'int'  # uint32
    priority: 'int'  # uint32
    target_part_group_index: 'int'  # uint32
    start_time: 'int'  # uint64


class TransitioningInteraction(Message):
    # __init__
    base_interaction_data: 'InteractionSaveData'
    posture_aspect_body: 'int'  # fixed uint64
    posture_carry_left: 'int'  # fixed uint64
    posture_carry_right: 'int'  # fixed uint64
    posture_carry_back: 'int'  # fixed uint64


class SuperInteractionSaveState(Message):
    # __init__
    interactions: 'RepeatedCompositeFieldContainer[InteractionSaveData]'
    transitioning_interaction: 'TransitioningInteraction'
    queued_interactions: 'RepeatedCompositeFieldContainer[InteractionSaveData]'


class WorldLocation(Message):
    # __init__
    x: 'float'  # float32
    y: 'float'  # float32
    z: 'float'  # float32
    rot_x: 'float'  # float32
    rot_y: 'float'  # float32
    rot_z: 'float'  # float32
    rot_w: 'float'  # float32
    level: 'int'  # int32
    surface_id: 'int'  # uint32


class ZoneTimeStamp(Message):
    # __init__
    game_time_expire: 'int'  # fixed uint64
    time_sim_info_was_saved: 'int'  # fixed uint64
    time_sim_was_saved: 'int'  # fixed uint64


class WhimsetTrackerData(Message):
    class WhimData():
        # __init__
        whimset_guid: 'int'  # uint64
        goal_data: 'SituationGoalData'
        duration: 'int'  # uint64
        index: 'int'  # uint32
        whim_guid: 'int'  # uint64
        commodity: 'Commodity'

    # __init__
    active_whims: 'RepeatedCompositeFieldContainer[WhimsetTrackerData.WhimData]'
    recently_completed_whims: 'RepeatedCompositeFieldContainer[WhimsetTrackerData.WhimData]'
    active_whimset_guids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    initial_whimset_history_guids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    whimset_guid: 'int'  # uint64
    goal_data: 'SituationGoalData'
    duration: 'int'  # uint64
    index: 'int'  # uint32
    whim_guid: 'int'  # uint64
    commodity: 'Commodity'


class AwayActionData(Message):
    # __init__
    away_action_id: 'int'  # fixed uint64
    target_sim_id: 'int'  # fixed uint64


class AwayActionTrackerData(Message):
    # __init__
    away_action: 'AwayActionData'


class SimFavoriteData(Message):
    # __init__
    recipe_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class GameplaySimData(Message):
    # __init__
    location: 'WorldLocation'
    inventory_value: 'int'  # uint64
    zone_time_stamp: 'ZoneTimeStamp'
    additional_bonus_days: 'int'  # uint64
    interaction_state: 'SuperInteractionSaveState'
    whim_bucks: 'int'  # uint32
    spawn_point_id: 'int'  # fixed uint64
    spawner_tags: 'RepeatedCompositeFieldContainer[int]'  # uint32
    spawn_point_option: 'int'  # uint32
    whim_tracker: 'WhimsetTrackerData'
    collection_data: 'RepeatedCompositeFieldContainer[CollectionData]'
    build_buy_unlocks: 'RepeatedCompositeFieldContainer[int]'  # uint64
    away_action_tracker: 'AwayActionTrackerData'
    serialization_option: 'int'  # uint32
    time_alive: 'int'  # uint64
    build_buy_unlock_list: 'ResourceKeyList'
    old_household_id: 'int'  # fixed uint64
    premade_sim_template_id: 'int'  # fixed uint64
    favorite_data: 'SimFavoriteData'
    bucks_data: 'RepeatedCompositeFieldContainer[BucksData]'
    creation_source_data: 'str'
    creation_source: 'int'  # uint64
    gameplay_options: 'int'  # uint64
    squad_members: 'RepeatedCompositeFieldContainer[int]'  # uint64
    vehicle_id: 'int'  # uint64
    developmental_milestone_tracker: 'DevelopmentalMilestoneTrackerData'
    premade_sim_fixup_completed: 'bool'
    reincarnation_data: 'ReincarnationData'
    extra_personality_trait_slot: 'RepeatedCompositeFieldContainer[int]'  # uint64
    restore_wings: 'bool'


class PremadeLotStatus(Message):
    # __init__
    lot_id: 'int'  # uint64
    is_premade: 'bool'


class EnsembleServiceData(Message):
    # __init__
    ensemble_datas: 'RepeatedCompositeFieldContainer[EnsembleData]'


class EnsembleData(Message):
    # __init__
    ensemble_type_id: 'int'  # fixed uint64
    sim_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class MissingPetTrackerData(Message):
    # __init__
    missing_pet_id: 'int'  # uint64
    test_alarm_finishing_time: 'int'  # uint64
    return_alarm_finishing_time: 'int'  # uint64
    cooldown_alarm_finishing_time: 'int'  # uint64
    return_pet_on_zone_load: 'bool'
    running_away: 'bool'
    motive_test_results: 'RepeatedCompositeFieldContainer[MotiveTestResults]'
    alert_posted: 'bool'


class MotiveTestResults(Message):
    # __init__
    pet_id: 'int'  # uint64
    test_results: 'RepeatedCompositeFieldContainer[int]'  # uint32


class LaundryData(Message):
    # __init__
    last_unload_time: 'int'  # uint64
    laundry_conditions: 'RepeatedCompositeFieldContainer[LaundryConditions]'


class LaundryConditions(Message):
    # __init__
    timestamp: 'int'  # uint64
    state_value_name_hash: 'int'  # uint64


class HiddenSimServiceData(Message):
    # __init__
    hidden_sim_data: 'RepeatedCompositeFieldContainer[HiddenSimData]'


class PreviousGoalData(Message):
    # __init__
    goal_data: 'SituationGoalData'
    new_in_ui: 'bool'
    age_completed: 'int'  # uint32


class DevelopmentalMilestoneTrackerData(Message):
    class DevelopmentalMilestoneStates(IntEnum):
        ACTIVE: 'DevelopmentalMilestoneTrackerData.DevelopmentalMilestoneStates' = 0
        UNLOCKED: 'DevelopmentalMilestoneTrackerData.DevelopmentalMilestoneStates' = 1

    ACTIVE = DevelopmentalMilestoneStates.ACTIVE
    UNLOCKED = DevelopmentalMilestoneStates.UNLOCKED

    class DevelopmentalMilestoneData():
        # __init__
        milestone_id: 'int'  # uint64
        state: 'DevelopmentalMilestoneTrackerData.DevelopmentalMilestoneData.DevelopmentalMilestoneStates'
        goal_data: 'SituationGoalData'
        new_in_ui: 'bool'
        previous_goals: 'RepeatedCompositeFieldContainer[PreviousGoalData]'
        age_completed: 'int'  # uint32

        class DevelopmentalMilestoneStates(IntEnum):
            ACTIVE: 'DevelopmentalMilestoneTrackerData.DevelopmentalMilestoneData.DevelopmentalMilestoneStates' = 0
            UNLOCKED: 'DevelopmentalMilestoneTrackerData.DevelopmentalMilestoneData.DevelopmentalMilestoneStates' = 1

    # __init__
    active_milestones: 'RepeatedCompositeFieldContainer[DevelopmentalMilestoneTrackerData.DevelopmentalMilestoneData]'
    initial_loot_applied: 'bool'
    archived_milestones: 'RepeatedCompositeFieldContainer[DevelopmentalMilestoneTrackerData.DevelopmentalMilestoneData]'
    milestone_id: 'int'  # uint64
    state: 'DevelopmentalMilestoneTrackerData.DevelopmentalMilestoneData.DevelopmentalMilestoneStates'
    goal_data: 'SituationGoalData'
    new_in_ui: 'bool'
    previous_goals: 'RepeatedCompositeFieldContainer[PreviousGoalData]'
    age_completed: 'int'  # uint32


class PersistableMultiUnitEventService(Message):
    # __init__
    zone_event_data: 'RepeatedCompositeFieldContainer[MultiUnitZoneEventData]'
    property_owner_event_data: 'RepeatedCompositeFieldContainer[PropertyOwnerEventData]'
    event_loot_data: 'RepeatedCompositeFieldContainer[MultiUnitEventLootData]'


class MultiUnitZoneEventData(Message):
    # __init__
    zone_id: 'int'  # uint64
    property_owner_event_drama_node_guid64: 'int'  # uint64
    active_event_drama_node_guid64: 'int'  # uint64
    tenant_alarm_time: 'int'  # uint64
    tested_zone_modifier_guid64s: 'RepeatedCompositeFieldContainer[int]'  # uint64


class PropertyOwnerEventData(Message):
    # __init__
    property_owner_hh_id: 'int'  # uint64
    event_alarm_time: 'int'  # uint64


class MultiUnitEventLootData(Message):
    # __init__
    household_id: 'int'  # uint64
    zone_id: 'int'  # uint64
    drama_node_guid64: 'int'  # uint64


class PersistableMultiUnitOwnershipService(Message):
    # __init__
    npc_property_owner_id: 'int'  # fixed uint64


class PersistableMatchmakingService(Message):
    # __init__
    actor_sim_data: 'RepeatedCompositeFieldContainer[MatchmakingActorData]'
    existing_npc_data: 'RepeatedCompositeFieldContainer[MatchmakingCandidateData]'
    gallery_kill_switch_enabled: 'bool'
    created_gallery_sims: 'RepeatedCompositeFieldContainer[MatchmakingCreatedGallerySim]'


class MatchmakingCreatedGallerySim(Message):
    # __init__
    exchange_data_remote_id: 'str'
    sim_id: 'int'  # fixed uint64


class MatchmakingNpcsOnCooldown(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    absolute_ticks: 'int'  # uint64


class MatchmakingGalleryIdsOnCooldown(Message):
    # __init__
    remote_id: 'str'
    absolute_ticks: 'int'  # uint64


class MatchmakingActorData(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    candidate_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    selected_ages: 'RepeatedCompositeFieldContainer[int]'  # uint64
    displayed_trait_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    time_last_refreshed: 'int'  # uint64
    num_contact_actions: 'int'  # uint64
    time_num_contact_action_reset: 'int'  # uint64
    saved_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    selfie_res_key: 'ResourceKey'
    bg_res_key: 'ResourceKey'
    is_first_refresh: 'bool'
    npcs_on_cooldown: 'RepeatedCompositeFieldContainer[MatchmakingNpcsOnCooldown]'
    gallery_sims_on_cooldown: 'RepeatedCompositeFieldContainer[MatchmakingGalleryIdsOnCooldown]'


class MatchmakingCandidateData(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    gender: 'int'  # uint32
    age: 'int'  # uint32
    extended_species: 'int'  # uint32
    real_sim_id: 'int'  # fixed uint64
    first_name: 'str'
    displayed_trait_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    contacted: 'bool'
    reported: 'bool'
    profile_type: 'int'  # int32
    region_name: 'str'
    physique: 'str'
    facial_attributes: 'bytes'
    skin_tone: 'int'  # uint64
    skin_tone_val_shift: 'float'  # float32
    is_from_template: 'bool'
    household_template_id: 'int'  # uint64
    pose_index: 'int'  # int32
    outfits: 'OutfitList'
    current_outfit_type: 'int'  # uint32
    current_outfit_index: 'int'  # uint32
    previous_outfit_type: 'int'  # uint32
    previous_outfit_index: 'int'  # uint32
    trait_ids: 'RepeatedCompositeFieldContainer[int]'  # uint32
    profile_bg_res_key: 'ResourceKey'
    exchange_data_creator_name: 'str'
    exchange_data_remote_id: 'str'
    exchange_data_type: 'int'  # uint32
    exchange_data_household_id: 'int'  # uint64
    family_info_msg: 'bytes'


class PersistableUiDialogService(Message):
    class SuppressionEntry():
        # __init__
        group_id: 'int'  # uint32
        suppression_count: 'int'  # int32

    # __init__
    suppression_entries: 'RepeatedCompositeFieldContainer[PersistableUiDialogService.SuppressionEntry]'
    group_id: 'int'  # uint32
    suppression_count: 'int'  # int32


class ReincarnationData(Message):
    # __init__
    previous_sim_id: 'int'  # fixed uint64
    trait_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    has_shown_reincarnation_animation: 'bool'


class PersistableWillService(Message):
    # __init__
    sim_wills: 'RepeatedCompositeFieldContainer[SimWillData]'
    household_wills: 'RepeatedCompositeFieldContainer[HouseholdWillData]'


class SimWillData(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    active: 'bool'
    claimant_sim_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    burial_preference_id: 'int'  # uint64
    funeral_activity_preferences: 'RepeatedCompositeFieldContainer[int]'  # uint64
    emotion_mood_id: 'int'  # fixed uint64
    note: 'LocalizedString'
    heirloom_distribution: 'RepeatedCompositeFieldContainer[SimWillHeirloomData]'
    heirloom_obj_data: 'RepeatedCompositeFieldContainer[SimWillHeirloomObjectData]'
    household_id: 'int'  # fixed uint64


class HouseholdWillData(Message):
    # __init__
    household_id: 'int'  # fixed uint64
    active: 'bool'
    claimant_hh_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    dependent_distribution: 'RepeatedCompositeFieldContainer[HouseholdWillDependentData]'
    simoleon_distribution: 'RepeatedCompositeFieldContainer[HouseholdWillSimoleonData]'
    charity_percentage: 'float'  # float32
    simoleon_amount: 'int'  # uint32


class SimWillHeirloomData(Message):
    # __init__
    object_id: 'int'  # fixed uint64
    recipient_sim_id: 'int'  # fixed uint64


class SimWillHeirloomObjectData(Message):
    # __init__
    object_id: 'int'  # fixed uint64
    object_data: 'bytes'


class HouseholdWillDependentData(Message):
    # __init__
    dependent_sim_id: 'int'  # fixed uint64
    recipient_hh_id: 'int'  # fixed uint64


class HouseholdWillSimoleonData(Message):
    # __init__
    recipient_hh_id: 'int'  # fixed uint64
    percentage: 'float'  # float32


class PersistableWispService(Message):
    # __init__
    wisp_data: 'WispData'


class WispData(Message):
    # __init__
    cycle_state_id: 'int'  # uint32
    plant_object_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class PersistableImaginaryFriendService(Message):
    # __init__
    friend_child_data: 'RepeatedCompositeFieldContainer[ImaginaryFriendChildData]'
    friend_status_data: 'RepeatedCompositeFieldContainer[ImaginaryFriendStatusData]'
    friend_doll_data: 'RepeatedCompositeFieldContainer[ImaginaryFriendDollData]'


class ImaginaryFriendChildData(Message):
    # __init__
    imaginary_friend_sim_id: 'int'  # fixed uint64
    child_sim_id: 'int'  # fixed uint64


class ImaginaryFriendStatusData(Message):
    # __init__
    imaginary_friend_sim_id: 'int'  # fixed uint64
    imaginary_friend_status: 'int'  # uint32


class ImaginaryFriendDollData(Message):
    # __init__
    imaginary_friend_sim_id: 'int'  # fixed uint64
    doll_obj_id: 'int'  # fixed uint64


class PersistableCustomScheduleService(Message):
    class ScheduledGetawayEntry():
        # __init__
        start_time: 'int'  # uint64
        zone_id: 'int'  # uint64
        duration: 'int'  # uint32
        schedule: 'CustomSchedule'
        owner_id: 'int'  # uint64

    # __init__
    custom_schedules: 'RepeatedCompositeFieldContainer[CustomSchedule]'
    custom_assignments: 'RepeatedCompositeFieldContainer[ScheduleAssignment]'
    scheduled_getaways: 'RepeatedCompositeFieldContainer[PersistableCustomScheduleService.ScheduledGetawayEntry]'
    mannequin_id: 'int'  # fixed uint64
    current_schedule_zone_id: 'int'  # uint64
    start_time: 'int'  # uint64
    zone_id: 'int'  # uint64
    duration: 'int'  # uint32
    schedule: 'CustomSchedule'
    owner_id: 'int'  # uint64
