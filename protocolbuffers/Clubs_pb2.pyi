from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer
from enum import IntEnum

from protocolbuffers.ResourceKey_pb2 import *
from protocolbuffers.Localization_pb2 import *
from protocolbuffers.Lot_pb2 import *


class ClubCriteria(Message):
    class ClubCriteriaCategory(IntEnum):
        SKILL: 'ClubCriteria.ClubCriteriaCategory' = 0
        TRAIT: 'ClubCriteria.ClubCriteriaCategory' = 1
        RELATIONSHIP: 'ClubCriteria.ClubCriteriaCategory' = 2
        CAREER: 'ClubCriteria.ClubCriteriaCategory' = 3
        HOUSEHOLD_VALUE: 'ClubCriteria.ClubCriteriaCategory' = 4
        AGE: 'ClubCriteria.ClubCriteriaCategory' = 5
        CLUB_MEMBERSHIP: 'ClubCriteria.ClubCriteriaCategory' = 6
        FAME_RANK: 'ClubCriteria.ClubCriteriaCategory' = 7
        CARE_SIM_TYPE_SUPERVISED: 'ClubCriteria.ClubCriteriaCategory' = 8
        OCCULT: 'ClubCriteria.ClubCriteriaCategory' = 9
        GENDER: 'ClubCriteria.ClubCriteriaCategory' = 10
        REGION: 'ClubCriteria.ClubCriteriaCategory' = 11
        ROMANTIC_ATTRACTION: 'ClubCriteria.ClubCriteriaCategory' = 12
        RELATIONSHIP_STATUS: 'ClubCriteria.ClubCriteriaCategory' = 13

    SKILL = ClubCriteriaCategory.SKILL
    TRAIT = ClubCriteriaCategory.TRAIT
    RELATIONSHIP = ClubCriteriaCategory.RELATIONSHIP
    CAREER = ClubCriteriaCategory.CAREER
    HOUSEHOLD_VALUE = ClubCriteriaCategory.HOUSEHOLD_VALUE
    AGE = ClubCriteriaCategory.AGE
    CLUB_MEMBERSHIP = ClubCriteriaCategory.CLUB_MEMBERSHIP
    FAME_RANK = ClubCriteriaCategory.FAME_RANK
    CARE_SIM_TYPE_SUPERVISED = ClubCriteriaCategory.CARE_SIM_TYPE_SUPERVISED
    OCCULT = ClubCriteriaCategory.OCCULT
    GENDER = ClubCriteriaCategory.GENDER
    REGION = ClubCriteriaCategory.REGION
    ROMANTIC_ATTRACTION = ClubCriteriaCategory.ROMANTIC_ATTRACTION
    RELATIONSHIP_STATUS = ClubCriteriaCategory.RELATIONSHIP_STATUS

    # __init__
    category: 'ClubCriteria.ClubCriteriaCategory'
    criteria_infos: 'RepeatedCompositeFieldContainer[ClubCriteriaInfo]'
    multi_select: 'bool'
    criteria_id: 'int'  # uint32
    required: 'bool'
    supervised: 'bool'


class ClubCriteriaInfo(Message):
    # __init__
    name: 'LocalizedString'
    icon: 'ResourceKey'
    resource_value: 'ResourceKey'
    enum_value: 'int'  # uint32
    resource_id: 'int'  # uint64
    tooltip_name: 'LocalizedString'


class ClubConductRule(Message):
    # __init__
    encouraged: 'bool'
    interaction_group: 'ResourceKey'
    with_whom: 'ClubCriteria'


class ClubBuildingInfo(Message):
    # __init__
    criterias: 'RepeatedCompositeFieldContainer[ClubCriteria]'
    available_lots: 'RepeatedCompositeFieldContainer[LotInfoItem]'


class ClubInteractionRuleUpdate(Message):
    class ClubInteractionRuleStatus(IntEnum):
        ENCOURAGED: 'ClubInteractionRuleUpdate.ClubInteractionRuleStatus' = 0
        DISCOURAGED: 'ClubInteractionRuleUpdate.ClubInteractionRuleStatus' = 1
        NO_EFFECT: 'ClubInteractionRuleUpdate.ClubInteractionRuleStatus' = 2

    ENCOURAGED = ClubInteractionRuleStatus.ENCOURAGED
    DISCOURAGED = ClubInteractionRuleStatus.DISCOURAGED
    NO_EFFECT = ClubInteractionRuleStatus.NO_EFFECT

    # __init__
    rule_status: 'ClubInteractionRuleUpdate.ClubInteractionRuleStatus'


class ShowClubInfoUI(Message):
    # __init__
    club_id: 'int'  # uint64
