from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer


class RoommateLeaveReasonInfo(Message):
    # __init__
    reason: 'int'  # uint64
    total_time: 'int'  # uint64
    been_warned: 'bool'


class RoommateInfo(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    bed_id: 'int'  # uint64
    decoration_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    leave_reason_infos: 'RepeatedCompositeFieldContainer[RoommateLeaveReasonInfo]'


class RoommateBlacklistSimInfo(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    time_left: 'int'  # uint64


class RoommateAdInfo(Message):
    # __init__
    household_id: 'int'  # fixed uint64
    pending_interview_alarms: 'RepeatedCompositeFieldContainer[int]'  # uint64
    interviewee_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class RoommateData(Message):
    # __init__
    zone_id: 'int'  # fixed uint64
    household_id: 'int'  # fixed uint64
    roommate_infos: 'RepeatedCompositeFieldContainer[RoommateInfo]'
    blacklist_infos: 'RepeatedCompositeFieldContainer[RoommateBlacklistSimInfo]'
    pending_destroy_decoration_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    locked_out_id: 'int'  # fixed uint64
    available_beds: 'int'  # int32


class PersistableRoommateService(Message):
    # __init__
    roommate_datas: 'RepeatedCompositeFieldContainer[RoommateData]'
    ad_info: 'RoommateAdInfo'
