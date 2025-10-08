from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer
from enum import IntEnum


class UserState(IntEnum):
    userstate_pending: 'UserState' = 1
    userstate_logged_in: 'UserState' = 2
    userstate_logged_out: 'UserState' = 3
    userstate_timedout_out: 'UserState' = 4
    userstate_bad_login: 'UserState' = 5
    connected_to_mtx_server: 'UserState' = 100
    connected_to_exchange_server: 'UserState' = 200
    connected_to_social_server: 'UserState' = 300


userstate_pending = UserState.userstate_pending
userstate_logged_in = UserState.userstate_logged_in
userstate_logged_out = UserState.userstate_logged_out
userstate_timedout_out = UserState.userstate_timedout_out
userstate_bad_login = UserState.userstate_bad_login
connected_to_mtx_server = UserState.connected_to_mtx_server
connected_to_exchange_server = UserState.connected_to_exchange_server
connected_to_social_server = UserState.connected_to_social_server


class IdList(Message):
    # __init__
    ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class GameInstanceInfoPB(Message):
    # __init__
    zone_id: 'int'  # uint64
    world_id: 'int'  # uint32
    neighborhood_name: 'str'
    zone_name: 'str'
    zone_session_id: 'int'  # uint64


class UserEntitlement(Message):
    class TrialStateMask(IntEnum):
        MASK_TRIAL_ENTITLEMENT: 'UserEntitlement.TrialStateMask' = 16

    MASK_TRIAL_ENTITLEMENT = TrialStateMask.MASK_TRIAL_ENTITLEMENT

    class TrialState(IntEnum):
        TRIAL_STATE_NONE: 'UserEntitlement.TrialState' = 0
        TRIAL_STATE_CONVERTED: 'UserEntitlement.TrialState' = 1
        TRIAL_STATE_TRIAL_ACTIVE: 'UserEntitlement.TrialState' = 16
        TRIAL_STATE_TRIAL_EXPIRED: 'UserEntitlement.TrialState' = 17

    TRIAL_STATE_NONE = TrialState.TRIAL_STATE_NONE
    TRIAL_STATE_CONVERTED = TrialState.TRIAL_STATE_CONVERTED
    TRIAL_STATE_TRIAL_ACTIVE = TrialState.TRIAL_STATE_TRIAL_ACTIVE
    TRIAL_STATE_TRIAL_EXPIRED = TrialState.TRIAL_STATE_TRIAL_EXPIRED

    # __init__
    entitlement_id: 'int'  # uint64
    version: 'int'  # uint32
    product_id: 'int'  # uint64
    last_modified_date: 'int'  # uint64
    product_sku: 'int'  # uint64
    view_state: 'int'  # uint32
    install_state: 'int'  # uint32
    terminate_date: 'int'  # uint64
    trial_state: 'int'  # uint32
    grant_date: 'int'  # uint64
    trial_view_state: 'int'  # uint32


class UserEntitlementMap(Message):
    # __init__
    entitlements: 'RepeatedCompositeFieldContainer[UserEntitlement]'
    last_modified_date: 'int'  # uint64


class AchievementItem(Message):
    # __init__
    id: 'int'  # uint32
    progress: 'int'  # uint32
    totalpoints: 'int'  # uint32
    repeatcount: 'int'  # uint32
    name: 'str'
    desc: 'str'
    howto: 'str'
    imageid: 'str'
    grantdate: 'int'  # uint64
    expiredate: 'int'  # uint64


class AchievementList(Message):
    # __init__
    name: 'str'
    gamename: 'str'
    achievements: 'RepeatedCompositeFieldContainer[AchievementItem]'


class AchievementMsg(Message):
    # __init__
    resultcode: 'int'  # int32
    mode: 'int'  # uint32
    lists: 'RepeatedCompositeFieldContainer[AchievementList]'


class UserShoppingCartItem(Message):
    # __init__
    entitlement_tag: 'str'
    offer_id: 'str'
    quantity: 'int'  # uint32
    override_price: 'float'  # float64
    unit_price: 'float'  # float64
    ientitlement_tag: 'int'  # uint64
    entry_id: 'int'  # uint64


class UserShoppingCart(Message):
    # __init__
    items: 'RepeatedCompositeFieldContainer[UserShoppingCartItem]'
    last_modified_date: 'str'


class Uint64Value(Message):
    # __init__
    value: 'int'  # uint64


class Uint64List(Message):
    # __init__
    values: 'RepeatedCompositeFieldContainer[Uint64Value]'


class BoolValue(Message):
    # __init__
    value: 'bool'


class HouseholdSimIds(Message):
    # __init__
    household_id: 'int'  # fixed uint64
    sim_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class Schedule(Message):
    class ScheduleDay(IntEnum):
        SUNDAY: 'Schedule.ScheduleDay' = 0
        MONDAY: 'Schedule.ScheduleDay' = 1
        TUESDAY: 'Schedule.ScheduleDay' = 2
        WEDNESDAY: 'Schedule.ScheduleDay' = 3
        THURSDAY: 'Schedule.ScheduleDay' = 4
        FRIDAY: 'Schedule.ScheduleDay' = 5
        SATURDAY: 'Schedule.ScheduleDay' = 6

    SUNDAY = ScheduleDay.SUNDAY
    MONDAY = ScheduleDay.MONDAY
    TUESDAY = ScheduleDay.TUESDAY
    WEDNESDAY = ScheduleDay.WEDNESDAY
    THURSDAY = ScheduleDay.THURSDAY
    FRIDAY = ScheduleDay.FRIDAY
    SATURDAY = ScheduleDay.SATURDAY

    class ScheduleShiftType(IntEnum):
        ALL_DAY: 'Schedule.ScheduleShiftType' = 0
        MORNING: 'Schedule.ScheduleShiftType' = 1
        EVENING: 'Schedule.ScheduleShiftType' = 2
        MULTI_DAY: 'Schedule.ScheduleShiftType' = 3

    ALL_DAY = ScheduleShiftType.ALL_DAY
    MORNING = ScheduleShiftType.MORNING
    EVENING = ScheduleShiftType.EVENING
    MULTI_DAY = ScheduleShiftType.MULTI_DAY

    class ScheduleEntry():
        # __init__
        days: 'RepeatedCompositeFieldContainer[ScheduleEntry.ScheduleDay]'
        start_hour: 'int'  # uint32
        start_minute: 'int'  # uint32
        duration: 'float'  # float32
        schedule_shift_type: 'ScheduleEntry.ScheduleShiftType'
        multi_day_start_day: 'int'  # uint32
        multi_day_end_day: 'int'  # uint32

        class ScheduleDay(IntEnum):
            SUNDAY: 'Schedule.ScheduleEntry.ScheduleDay' = 0
            MONDAY: 'Schedule.ScheduleEntry.ScheduleDay' = 1
            TUESDAY: 'Schedule.ScheduleEntry.ScheduleDay' = 2
            WEDNESDAY: 'Schedule.ScheduleEntry.ScheduleDay' = 3
            THURSDAY: 'Schedule.ScheduleEntry.ScheduleDay' = 4
            FRIDAY: 'Schedule.ScheduleEntry.ScheduleDay' = 5
            SATURDAY: 'Schedule.ScheduleEntry.ScheduleDay' = 6

        class ScheduleShiftType(IntEnum):
            ALL_DAY: 'Schedule.ScheduleEntry.ScheduleShiftType' = 0
            MORNING: 'Schedule.ScheduleEntry.ScheduleShiftType' = 1
            EVENING: 'Schedule.ScheduleEntry.ScheduleShiftType' = 2
            MULTI_DAY: 'Schedule.ScheduleEntry.ScheduleShiftType' = 3

    # __init__
    schedule_entries: 'RepeatedCompositeFieldContainer[ScheduleEntry]'
    days: 'RepeatedCompositeFieldContainer[ScheduleEntry.ScheduleDay]'
    start_hour: 'int'  # uint32
    start_minute: 'int'  # uint32
    duration: 'float'  # float32
    schedule_shift_type: 'ScheduleEntry.ScheduleShiftType'
    multi_day_start_day: 'int'  # uint32
    multi_day_end_day: 'int'  # uint32


class SimPronoun(Message):
    class GrammaticalCase(IntEnum):
        UNKNOWN: 'SimPronoun.GrammaticalCase' = 0
        SUBJECTIVE: 'SimPronoun.GrammaticalCase' = 1
        OBJECTIVE: 'SimPronoun.GrammaticalCase' = 2
        POSSESSIVE_DEPENDENT: 'SimPronoun.GrammaticalCase' = 3
        POSSESSIVE_INDEPENDENT: 'SimPronoun.GrammaticalCase' = 4
        REFLEXIVE: 'SimPronoun.GrammaticalCase' = 5

    UNKNOWN = GrammaticalCase.UNKNOWN
    SUBJECTIVE = GrammaticalCase.SUBJECTIVE
    OBJECTIVE = GrammaticalCase.OBJECTIVE
    POSSESSIVE_DEPENDENT = GrammaticalCase.POSSESSIVE_DEPENDENT
    POSSESSIVE_INDEPENDENT = GrammaticalCase.POSSESSIVE_INDEPENDENT
    REFLEXIVE = GrammaticalCase.REFLEXIVE

    # __init__
    case: 'SimPronoun.GrammaticalCase'
    pronoun: 'str'


class SimPronounList(Message):
    # __init__
    pronouns: 'RepeatedCompositeFieldContainer[SimPronoun]'
