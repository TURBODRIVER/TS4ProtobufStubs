from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer
from enum import IntEnum

from protocolbuffers.S4Common_pb2 import *
from protocolbuffers.Localization_pb2 import *


class SocialNotificationType(IntEnum):
    CHAT: 'SocialNotificationType' = 0
    BUDDYLIST: 'SocialNotificationType' = 1
    BUDDYLIST_INVITE: 'SocialNotificationType' = 2
    WALL: 'SocialNotificationType' = 3
    GAMEPLAY: 'SocialNotificationType' = 4
    MTX: 'SocialNotificationType' = 5
    IMMEDIATE: 'SocialNotificationType' = 6
    GAMEPLAY_ASPIRATION: 'SocialNotificationType' = 7
    SYSTEM: 'SocialNotificationType' = 8
    EXCHANGE: 'SocialNotificationType' = 9


CHAT = SocialNotificationType.CHAT
BUDDYLIST = SocialNotificationType.BUDDYLIST
BUDDYLIST_INVITE = SocialNotificationType.BUDDYLIST_INVITE
WALL = SocialNotificationType.WALL
GAMEPLAY = SocialNotificationType.GAMEPLAY
MTX = SocialNotificationType.MTX
IMMEDIATE = SocialNotificationType.IMMEDIATE
GAMEPLAY_ASPIRATION = SocialNotificationType.GAMEPLAY_ASPIRATION
SYSTEM = SocialNotificationType.SYSTEM
EXCHANGE = SocialNotificationType.EXCHANGE


class ZoneConnectedLotVersionData(Message):
    # __init__
    lotID: 'int'  # uint32
    version: 'int'  # uint64


class ConnectedNeighborhoodLot(Message):
    # __init__
    lotId: 'int'  # uint32
    zoneInstanceId: 'int'  # uint64


class ZoneConnectedData(Message):
    # __init__
    instance_info: 'GameInstanceInfoPB'
    active_lot_id: 'int'  # uint32
    lot_versions: 'RepeatedCompositeFieldContainer[ZoneConnectedLotVersionData]'
    neighborhood_lots: 'RepeatedCompositeFieldContainer[ConnectedNeighborhoodLot]'


class GSI_Open(Message):
    # __init__
    ip: 'str'
    port: 'int'  # uint32
    zone_id: 'int'  # uint64
    additional_params: 'str'


class AchievementTrackerUpdate(Message):
    # __init__
    account_id: 'int'  # uint64
    achievements_completed: 'RepeatedCompositeFieldContainer[int]'  # uint64
    objectives_completed: 'RepeatedCompositeFieldContainer[int]'  # uint64
    init_message: 'bool'
    cheats_used: 'bool'


class AcctGoalsStatusUpdate(Message):
    # __init__
    account_id: 'int'  # uint64
    goals_updated: 'RepeatedCompositeFieldContainer[int]'  # uint64
    goal_values: 'RepeatedCompositeFieldContainer[int]'  # int64
    goal_objectives: 'RepeatedCompositeFieldContainer[int]'  # int64
    goals_that_are_money: 'RepeatedCompositeFieldContainer[bool]'
    goals_that_show_progress: 'RepeatedCompositeFieldContainer[bool]'
    goals_with_update_tooltip_in_special_cases: 'RepeatedCompositeFieldContainer[bool]'


class GameTimeCommand(Message):
    # __init__
    clock_speed: 'int'  # uint32
    game_speed: 'float'  # float32
    server_time: 'int'  # uint64
    sync_game_time: 'int'  # uint64
    monotonic_time: 'int'  # uint64
    super_speed: 'bool'
    serial_number: 'int'  # uint64


class SocialNotification(Message):
    # __init__
    type: 'SocialNotificationType'
    localized_string: 'LocalizedString'
    account_id: 'int'  # uint64
    sim_id: 'int'  # uint64
    event_uid: 'int'  # uint32
