from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer

from protocolbuffers.Consts_pb2 import *
from protocolbuffers.S4Common_pb2 import *


class BodyTypesList(Message):
    # __init__
    body_types: 'RepeatedCompositeFieldContainer[int]'  # uint32


class ColorShiftList(Message):
    # __init__
    color_shift: 'RepeatedCompositeFieldContainer[int]'  # uint64


class ObjectIdsList(Message):
    # __init__
    object_id: 'RepeatedCompositeFieldContainer[int]'  # uint64


class LayerIdsList(Message):
    # __init__
    layer_id: 'RepeatedCompositeFieldContainer[int]'  # uint32


class OutfitData(Message):
    # __init__
    outfit_id: 'int'  # uint64
    category: 'int'  # uint32
    parts: 'IdList'
    created: 'int'  # uint64
    body_types_list: 'BodyTypesList'
    match_hair_style: 'bool'
    outfit_flags: 'int'  # uint64
    outfit_flags_high: 'int'  # uint64
    part_shifts: 'ColorShiftList'
    title: 'str'
    object_ids: 'ObjectIdsList'
    layer_ids: 'LayerIdsList'
    outfitflags_array: 'RepeatedCompositeFieldContainer[int]'  # uint64


class OutfitList(Message):
    # __init__
    outfits: 'RepeatedCompositeFieldContainer[OutfitData]'


class PartData(Message):
    # __init__
    id: 'int'  # uint64
    body_type: 'int'  # uint32
    color_shift: 'int'  # uint64
    object_id: 'int'  # uint64
    layer_id: 'int'  # uint32


class PartDataList(Message):
    # __init__
    parts: 'RepeatedCompositeFieldContainer[PartData]'


class GeneticData(Message):
    # __init__
    sculpts_and_mods_attr: 'bytes'
    physique: 'str'
    voice_pitch: 'float'  # float32
    voice_actor: 'int'  # uint32
    parts_list: 'PartDataList'
    growth_parts_list: 'PartDataList'


class PeltLayerData(Message):
    # __init__
    layer_id: 'int'  # uint64
    color: 'int'  # uint32


class PeltLayerDataList(Message):
    # __init__
    layers: 'RepeatedCompositeFieldContainer[PeltLayerData]'


class SimPartCustomTattooData(Message):
    # __init__
    body_type: 'int'  # uint32
    texture_id: 'int'  # uint64


class SimPartCreatorData(Message):
    # __init__
    body_type: 'int'  # uint32
    creator_uuid: 'bytes'
    creator_id: 'int'  # uint64
    creator_name: 'str'
    creator_platform: 'ExchangeItemPlatform'
    creator_platform_id: 'int'  # uint64
    creator_platform_name: 'str'
