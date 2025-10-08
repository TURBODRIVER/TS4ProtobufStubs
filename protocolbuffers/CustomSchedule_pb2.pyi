from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer
from enum import IntEnum

from protocolbuffers.Clubs_pb2 import *
from protocolbuffers.ResourceKey_pb2 import *
from protocolbuffers.SimObjectAttributes_pb2 import *
from protocolbuffers.Localization_pb2 import *


class ScheduleAssignmentOutfit(Message):
    class ScheduleOutfitSetting(IntEnum):
        NO_OUTFIT: 'ScheduleAssignmentOutfit.ScheduleOutfitSetting' = 0
        CATEGORY: 'ScheduleAssignmentOutfit.ScheduleOutfitSetting' = 1
        STYLE_COLOR: 'ScheduleAssignmentOutfit.ScheduleOutfitSetting' = 2
        OUTFIT_OVERRIDE: 'ScheduleAssignmentOutfit.ScheduleOutfitSetting' = 3

    NO_OUTFIT = ScheduleOutfitSetting.NO_OUTFIT
    CATEGORY = ScheduleOutfitSetting.CATEGORY
    STYLE_COLOR = ScheduleOutfitSetting.STYLE_COLOR
    OUTFIT_OVERRIDE = ScheduleOutfitSetting.OUTFIT_OVERRIDE

    # __init__
    outfit_setting: 'ScheduleAssignmentOutfit.ScheduleOutfitSetting'
    outfit_color: 'int'  # uint32
    outfit_style: 'int'  # uint32
    outfit_category: 'int'  # uint32
    assignment_uniform_adult_male: 'MannequinSimData'
    assignment_uniform_adult_female: 'MannequinSimData'
    assignment_uniform_child_male: 'MannequinSimData'
    assignment_uniform_child_female: 'MannequinSimData'
    style_enabled: 'bool'
    color_enabled: 'bool'


class ScheduleAssignment(Message):
    # __init__
    name: 'str'
    sim_count: 'int'  # uint32
    sim_criteria: 'RepeatedCompositeFieldContainer[ClubCriteria]'
    assignment_behaviors: 'RepeatedCompositeFieldContainer[ResourceKey]'
    assignment_outfit: 'ScheduleAssignmentOutfit'
    sim_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    is_new: 'bool'
    is_immutable: 'bool'
    id: 'int'  # uint32
    premade_name: 'LocalizedString'


class ScheduleTimeSlotAssignment(Message):
    # __init__
    assignment_id: 'int'  # uint32
    assignment_overrides: 'ScheduleAssignment'
    has_behavior_override: 'bool'
    has_sim_overrides: 'bool'
    has_outfit_override: 'bool'
    has_count_override: 'bool'


class ScheduleTimeSlot(Message):
    # __init__
    start_time: 'int'  # uint32
    default_behavior: 'ResourceKey'
    assignments: 'RepeatedCompositeFieldContainer[ScheduleTimeSlotAssignment]'
    shuffled_behavior: 'ResourceKey'


class GetawaySelectedRule(Message):
    class SelectedRuleGroup():
        # __init__
        group_id: 'int'  # uint32
        assignment_names: 'RepeatedCompositeFieldContainer[str]'
        assignment_ids: 'RepeatedCompositeFieldContainer[int]'  # uint32

    # __init__
    rule_guid64: 'int'  # uint64
    groups: 'RepeatedCompositeFieldContainer[GetawaySelectedRule.SelectedRuleGroup]'
    use_current_track_values: 'bool'
    group_id: 'int'  # uint32
    assignment_names: 'RepeatedCompositeFieldContainer[str]'
    assignment_ids: 'RepeatedCompositeFieldContainer[int]'  # uint32


class CustomSchedule(Message):
    # __init__
    name: 'str'
    assignment_presets: 'RepeatedCompositeFieldContainer[ScheduleAssignment]'
    time_slots: 'RepeatedCompositeFieldContainer[ScheduleTimeSlot]'
    rules: 'RepeatedCompositeFieldContainer[GetawaySelectedRule]'
    is_immutable: 'bool'
    premade_name: 'LocalizedString'
    has_started: 'bool'
    use_current_track_values: 'bool'


class AssignmentListData(Message):
    # __init__
    name: 'str'
    is_immutable: 'bool'
    premade_name: 'LocalizedString'


class AssignmentList(Message):
    # __init__
    assignments: 'RepeatedCompositeFieldContainer[AssignmentListData]'


class ScheduleListData(Message):
    # __init__
    name: 'str'
    is_immutable: 'bool'
    lot_current: 'bool'
    premade_name: 'LocalizedString'
    has_rules: 'bool'


class ScheduleList(Message):
    # __init__
    schedules: 'RepeatedCompositeFieldContainer[ScheduleListData]'


class CustomScheduleSetCustomSchedule(Message):
    # __init__
    schedule: 'CustomSchedule'


class CustomScheduleSetCustomAssignment(Message):
    # __init__
    assignment: 'ScheduleAssignment'


class CustomScheduleSetScheduleList(Message):
    # __init__
    schedule_list: 'ScheduleList'


class CustomScheduleSetAssignmentList(Message):
    # __init__
    assignment_list: 'AssignmentList'


class CustomScheduleSetMannequinData(Message):
    # __init__
    assignment_uniform: 'MannequinSimData'


class CustomScheduleSetAvailableSims(Message):
    # __init__
    sim_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    invalid_sim_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
