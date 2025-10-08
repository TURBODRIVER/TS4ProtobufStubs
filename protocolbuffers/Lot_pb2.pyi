from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer

from protocolbuffers.ResourceKey_pb2 import *
from protocolbuffers.Localization_pb2 import *


class LotInfoItem(Message):
    # __init__
    zone_id: 'int'  # fixed uint64
    name: 'str'
    world_id: 'int'  # uint32
    lot_template_id: 'int'  # uint32
    lot_description_id: 'int'  # fixed uint64
    venue_type_name: 'LocalizedString'
    household_name: 'str'
    venue_type: 'ResourceKey'
    region_description_id: 'int'  # uint32
    region_name: 'str'
    region_icon: 'ResourceKey'
    house_description_id: 'int'  # fixed uint64
    custom_schedule_name: 'str'
    custom_schedule_activity_names: 'RepeatedCompositeFieldContainer[LocalizedString]'
    cost_for_getaway: 'int'  # uint32
    related_household: 'bool'
    is_premade_custom_schedule: 'bool'
    custom_schedule_name_key: 'LocalizedString'


class LotPlexExteriorUpdate(Message):
    # __init__
    zone_id: 'int'  # fixed uint64
    plex_exterior_house_desc_id: 'int'  # uint32
