from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer
from enum import IntEnum

from protocolbuffers.ResourceKey_pb2 import *
from protocolbuffers.Localization_pb2 import *
from protocolbuffers.UI_pb2 import *


class Interactable(Message):
    class InteractableFlags(IntEnum):
        INTERACTABLE: 'Interactable.InteractableFlags' = 1
        FORSALE: 'Interactable.InteractableFlags' = 2

    INTERACTABLE = InteractableFlags.INTERACTABLE
    FORSALE = InteractableFlags.FORSALE

    # __init__
    is_interactable: 'bool'
    object_id: 'int'  # fixed uint64
    interactable_flags: 'int'  # uint64


class PieMenuItem(Message):
    # __init__
    id: 'int'  # uint32
    loc_string: 'LocalizedString'
    related_skills: 'RepeatedCompositeFieldContainer[int]'  # uint64
    target_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    icon: 'ResourceKey'
    disabled_text: 'LocalizedString'
    score_icon: 'ResourceKey'
    category_key: 'int'  # uint64
    is_super: 'bool'
    score: 'float'  # float32
    icons: 'RepeatedCompositeFieldContainer[ResourceKey]'
    mood: 'int'  # fixed uint64
    mood_intensity: 'int'  # uint32
    pie_menu_priority: 'int'  # uint32
    success_tooltip: 'LocalizedString'
    icon_infos: 'RepeatedCompositeFieldContainer[IconInfo]'
    display_notification: 'bool'
    affordance_id: 'int'  # uint64
    phone_notification_control_override: 'bool'


class PieMenuCreate(Message):
    # __init__
    sim: 'int'  # uint64
    items: 'RepeatedCompositeFieldContainer[PieMenuItem]'
    client_reference_id: 'int'  # uint32
    server_reference_id: 'int'  # uint32
    category_tokens: 'RepeatedCompositeFieldContainer[LocalizedStringToken]'
    disabled_tooltip: 'LocalizedString'
    supress_social_front_page: 'bool'
    selected_affordance_id: 'int'  # uint64


class TravelMenuCreate(Message):
    # __init__
    sim_id: 'int'  # uint64
    selected_lot_id: 'int'  # uint64
    selected_world_id: 'int'  # uint32
    selected_lot_name: 'str'
    friend_account: 'str'


class TravelMenuInfo(Message):
    # __init__
    sim_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64


class TravelMenuResponse(Message):
    # __init__
    reserved: 'bool'


class TravelInitiate(Message):
    # __init__
    zoneId: 'int'  # uint64


class MoveInMoveOutInfo(Message):
    # __init__
    moving_family_id: 'int'  # uint64
    is_in_game_evict: 'bool'
    source_zone_id: 'int'  # uint64


class SellRetailLot(Message):
    # __init__
    retail_zone_id: 'int'  # uint64


class TravelSimsToZone(Message):
    # __init__
    zone_id: 'int'  # fixed uint64
    sim_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    active_sim_id: 'int'  # fixed uint64


class CASAvailableZonesInfo(Message):
    # __init__
    zones: 'RepeatedCompositeFieldContainer[WorldZonesInfo]'


class WorldZonesInfo(Message):
    # __init__
    name: 'str'
    defaultName: 'LocalizedString'
    zones: 'RepeatedCompositeFieldContainer[ZoneInfo]'
    worldId: 'int'  # uint32


class ZoneInfo(Message):
    # __init__
    id: 'int'  # uint64
    name: 'str'
    defaultName: 'LocalizedString'
    world_id: 'int'  # uint32
    lot_description_id: 'int'  # fixed uint64


class InteractionProgressUpdate(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    name: 'LocalizedString'
    percent: 'float'  # float32
    rate_change: 'float'  # float32
    interaction_id: 'int'  # uint64


class SimTransferRequest(Message):
    # __init__
    source_household_id: 'int'  # fixed uint64
    target_household_id: 'int'  # fixed uint64
    active_sim_id: 'int'  # fixed uint64


class PhoneNotificationUpdate(Message):
    # __init__
    interaction_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    sim_id: 'int'  # uint64
