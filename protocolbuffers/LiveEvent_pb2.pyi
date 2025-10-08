from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer
from enum import IntEnum

from protocolbuffers.ResourceKey_pb2 import *
from protocolbuffers.Localization_pb2 import *
from protocolbuffers.Events_pb2 import *


class LiveEventProgress(Message):
    class LiveEventType(IntEnum):
        UNKNOWN: 'LiveEventProgress.LiveEventType' = 0
        LOGIN: 'LiveEventProgress.LiveEventType' = 1
        QUEST: 'LiveEventProgress.LiveEventType' = 2

    UNKNOWN = LiveEventType.UNKNOWN
    LOGIN = LiveEventType.LOGIN
    QUEST = LiveEventType.QUEST

    class LiveEventBase():
        # __init__
        id: 'int'  # uint64
        type: 'LiveEventProgress.LiveEventType'
        startDate: 'LocalizedDateAndTimeData'
        endDate: 'LocalizedDateAndTimeData'
        isEnabled: 'bool'

    class LiveEventReward():
        # __init__
        instance: 'ResourceKey'

    class LiveEventLogin():
        # __init__
        eventData: 'LiveEventProgress.LiveEventBase'
        sessionCount: 'int'  # uint32
        lastSessionDate: 'LocalizedDateAndTimeData'
        claimedRewards: 'RepeatedCompositeFieldContainer[LiveEventProgress.LiveEventReward]'
        unclaimedRewards: 'RepeatedCompositeFieldContainer[LiveEventProgress.LiveEventReward]'

    class LiveEventQuest():
        # __init__
        eventData: 'LiveEventProgress.LiveEventBase'
        dataFromServer: 'EventDefinition'
        progressVerifed: 'EventProgressResponse.EventProgress'
        progressOffline: 'EventProgressUpdate'
        claimedRewards: 'RepeatedCompositeFieldContainer[LiveEventProgress.LiveEventReward]'
        unclaimedRewards: 'RepeatedCompositeFieldContainer[LiveEventProgress.LiveEventReward]'

    # __init__
    loginEvents: 'RepeatedCompositeFieldContainer[LiveEventProgress.LiveEventLogin]'
    questEvents: 'RepeatedCompositeFieldContainer[LiveEventProgress.LiveEventQuest]'
    id: 'int'  # uint64
    type: 'LiveEventProgress.LiveEventType'
    startDate: 'LocalizedDateAndTimeData'
    endDate: 'LocalizedDateAndTimeData'
    isEnabled: 'bool'
    instance: 'ResourceKey'
    eventData: 'LiveEventProgress.LiveEventBase'
    sessionCount: 'int'  # uint32
    lastSessionDate: 'LocalizedDateAndTimeData'
    claimedRewards: 'RepeatedCompositeFieldContainer[LiveEventProgress.LiveEventReward]'
    unclaimedRewards: 'RepeatedCompositeFieldContainer[LiveEventProgress.LiveEventReward]'
    eventData: 'LiveEventProgress.LiveEventBase'
    dataFromServer: 'EventDefinition'
    progressVerifed: 'EventProgressResponse.EventProgress'
    progressOffline: 'EventProgressUpdate'
    claimedRewards: 'RepeatedCompositeFieldContainer[LiveEventProgress.LiveEventReward]'
    unclaimedRewards: 'RepeatedCompositeFieldContainer[LiveEventProgress.LiveEventReward]'
