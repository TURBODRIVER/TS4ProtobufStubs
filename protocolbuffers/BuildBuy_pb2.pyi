from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer

from protocolbuffers.Math_pb2 import *
from protocolbuffers.Venue_pb2 import *


class LotId(Message):
    # __init__
    id: 'int'  # uint32
    household: 'int'  # uint64


class LotOwnershipList(Message):
    # __init__
    account_id: 'int'  # uint64
    lot_id: 'RepeatedCompositeFieldContainer[int]'  # uint32


class LotDescription(Message):
    # __init__
    id: 'int'  # uint32
    position: 'Vector3'
    rotation: 'float'  # float32
    tilesize_x: 'int'  # int32
    tilesize_z: 'int'  # int32
    owner_family_id: 'int'  # uint64
    min_level: 'int'  # int32
    max_level: 'int'  # int32
    playableLot: 'bool'
    lot_price: 'int'  # int32
    blueprint_id: 'int'  # uint64
    active_plex: 'int'  # uint32
    building_type: 'int'  # uint32


class BBOpFailed(Message):
    # __init__
    error_code: 'int'  # uint32
    op_id: 'int'  # uint32


class BBUndoRedoState(Message):
    # __init__
    canUndo: 'bool'
    canRedo: 'bool'


class ApplyBlueprintData(Message):
    # __init__
    blueprint_data: 'bytes'
    furnished: 'bool'
    sell_old_furniture: 'bool'
    zone_id: 'int'  # uint64
    blueprint_id: 'int'  # uint64
    delta_funds: 'int'  # int64
    size_x: 'int'  # int32
    size_z: 'int'  # int32
    bedroom_count: 'int'  # int32
    bathroom_count: 'int'  # int32
    front_side: 'int'  # int32
    region_id: 'int'  # uint64
    allow_custom_textures: 'bool'
    creator_uuid: 'bytes'
    creator_id: 'int'  # uint64
    creator_name: 'str'
    modifier_id: 'int'  # uint64
    modifier_name: 'str'
    zone_name: 'str'
    lot_traits: 'RepeatedCompositeFieldContainer[int]'  # uint64
    university_housing_configuration: 'UniversityHousingConfiguration'
    keep_venue_type: 'bool'
    clear_dynamic_areas: 'bool'


class PlexRatingMessage(Message):
    # __init__
    plex_id: 'int'  # uint32
    size_rating: 'int'  # int32
    amenity_rating: 'int'  # int32
    environment_rating: 'int'  # int32
    real_bed_count: 'int'  # uint32
    real_toilet_count: 'int'  # uint32


class PlexRatingUpdate(Message):
    # __init__
    ratings: 'RepeatedCompositeFieldContainer[PlexRatingMessage]'


class LotValueMessage(Message):
    # __init__
    plex_id: 'int'  # uint32
    unfurnished_value: 'int'  # int32
    furnished_value: 'int'  # int32
    architecture_value: 'int'  # int32


class LotValueUpdate(Message):
    # __init__
    zone_id: 'int'  # uint64
    lot_values: 'RepeatedCompositeFieldContainer[LotValueMessage]'
    plex_rating_update: 'PlexRatingUpdate'
    update_cache: 'bool'


class SetRentPriceData(Message):
    # __init__
    zone_id: 'int'  # uint64
    house_description_id: 'int'  # uint64
    rent_price: 'int'  # uint32


class InitialRentPriceUpdate(Message):
    # __init__
    rent_prices: 'RepeatedCompositeFieldContainer[SetRentPriceData]'
