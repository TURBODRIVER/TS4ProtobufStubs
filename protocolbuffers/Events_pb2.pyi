from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer
from enum import IntEnum

from protocolbuffers.Consts_pb2 import *
from protocolbuffers.Localization_pb2 import *


class EventVersion(IntEnum):
    UNKNOWN: 'EventVersion' = 0
    R3_EVENT: 'EventVersion' = 100
    DEC_EVENT: 'EventVersion' = 200
    R4_EVENT: 'EventVersion' = 300
    R5_EVENT: 'EventVersion' = 400
    EVTSept25: 'EventVersion' = 500


UNKNOWN = EventVersion.UNKNOWN
R3_EVENT = EventVersion.R3_EVENT
DEC_EVENT = EventVersion.DEC_EVENT
R4_EVENT = EventVersion.R4_EVENT
R5_EVENT = EventVersion.R5_EVENT
EVTSept25 = EventVersion.EVTSept25


class EventDefinition(Message):
    # __init__
    event_id: 'str'
    start_date: 'LocalizedDateAndTimeData'
    end_date: 'LocalizedDateAndTimeData'
    event_type: 'str'
    name: 'str'
    description: 'str'
    reward_periods: 'RepeatedCompositeFieldContainer[RewardPeriod]'
    progress_rewards: 'RepeatedCompositeFieldContainer[EventProgressReward]'
    grace_period_end_date: 'LocalizedDateAndTimeData'
    last_revision_time: 'LocalizedDateAndTimeData'


class RewardPeriod(Message):
    # __init__
    reward_period_id: 'int'  # uint32
    start_date: 'LocalizedDateAndTimeData'
    end_date: 'LocalizedDateAndTimeData'
    name: 'str'
    quests: 'RepeatedCompositeFieldContainer[Quest]'
    catch_up_periods: 'RepeatedCompositeFieldContainer[CatchUpPeriod]'
    max_xp: 'int'  # int64


class Reward(Message):
    # __init__
    reward_id: 'int'  # int64
    reward_type: 'RewardType'
    amount: 'int'  # int64


class EventProgressReward(Message):
    # __init__
    progress_id: 'int'  # uint32
    type: 'ProgressType'
    target_xp: 'int'  # int64
    rewards: 'RepeatedCompositeFieldContainer[Reward]'


class ProgressReward(Message):
    # __init__
    progress_id: 'int'  # uint32
    reward_unlocked: 'bool'
    reward_claimed: 'bool'


class EventProgressResponse(Message):
    class EventProgress():
        # __init__
        event_id: 'str'
        event_xp: 'int'  # int64
        progress: 'RepeatedCompositeFieldContainer[RewardPeriodProgress]'
        progress_rewards: 'RepeatedCompositeFieldContainer[ProgressReward]'

    # __init__
    event_progress: 'RepeatedCompositeFieldContainer[EventProgressResponse.EventProgress]'
    event_id: 'str'
    event_xp: 'int'  # int64
    progress: 'RepeatedCompositeFieldContainer[RewardPeriodProgress]'
    progress_rewards: 'RepeatedCompositeFieldContainer[ProgressReward]'


class Quest(Message):
    # __init__
    quest_id: 'int'  # uint32
    tuning_instance_id: 'int'  # uint32
    quest_name: 'str'
    xp: 'int'  # int64
    objectives: 'RepeatedCompositeFieldContainer[QuestObjective]'
    is_canceled: 'bool'


class QuestObjective(Message):
    # __init__
    objective_id: 'int'  # uint32
    xp: 'int'  # int64
    name: 'str'
    is_canceled: 'bool'


class CatchUpPeriod(Message):
    # __init__
    catch_up_id: 'int'  # uint32
    start_date: 'LocalizedDateAndTimeData'
    end_date: 'LocalizedDateAndTimeData'
    xp_multiplier: 'float'  # float32
    is_enabled: 'bool'


class ClaimedRewardUpdate(Message):
    # __init__
    event_id: 'str'
    claimed_progress_id: 'RepeatedCompositeFieldContainer[int]'  # uint32


class ServerResponse(Message):
    # __init__
    response_code: 'EventOpResponse'
    description: 'str'


class QuestObjectiveProgress(Message):
    # __init__
    objective_id: 'int'  # uint32
    xp: 'int'  # int64
    catch_up_id: 'int'  # uint32
    completion_time: 'LocalizedDateAndTimeData'
    completed: 'bool'


class QuestProgress(Message):
    # __init__
    quest_id: 'int'  # uint32
    quest_objective_progress: 'RepeatedCompositeFieldContainer[QuestObjectiveProgress]'
    xp: 'int'  # int64
    catch_up_id: 'int'  # uint32
    completion_time: 'LocalizedDateAndTimeData'
    completed: 'bool'
    canceled: 'bool'


class EventProgressUpdate(Message):
    # __init__
    event_id: 'str'
    progress: 'RepeatedCompositeFieldContainer[RewardPeriodProgress]'
    event_xp: 'int'  # int64


class RewardPeriodProgress(Message):
    # __init__
    reward_period_id: 'int'  # uint32
    quest_progress: 'RepeatedCompositeFieldContainer[QuestProgress]'


class PlayerInventoryResponse(Message):
    # __init__
    rewards: 'RepeatedCompositeFieldContainer[Reward]'


class EventsControlMessage(Message):
    # __init__
    opCode: 'EventsOpTypes'
    transactionId: 'int'  # uint64
    response: 'ServerResponse'
    event_definition: 'RepeatedCompositeFieldContainer[EventDefinition]'
    event_progress_update: 'EventProgressUpdate'
    claimed_reward_update: 'ClaimedRewardUpdate'
    event_progress_response: 'EventProgressResponse'
    player_inventory_response: 'PlayerInventoryResponse'
    max_event_version: 'EventVersion'
