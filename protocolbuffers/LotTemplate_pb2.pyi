from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer

from protocolbuffers.Math_pb2 import *
from protocolbuffers.ResourceKey_pb2 import *


class LotObject(Message):
    # __init__
    id: 'int'  # uint64
    quat_pos: 'Transform'
    object_def_guid: 'int'  # uint32
    level: 'int'  # int32
    parent_id: 'int'  # uint64
    slot_hash: 'int'  # uint32
    slot_index: 'int'  # uint32
    object_state_idx: 'int'  # uint32
    parent_type: 'int'  # uint32
    parent_location: 'int'  # uint64
    light_color: 'Vector3'
    scale: 'float'  # float32
    light_dimmer_value: 'float'  # float32
    object_def_guid64: 'int'  # uint64
    geo_state_id: 'int'  # uint32
    model_override_key: 'ResourceKey'
    material_state_id: 'int'  # uint32
    buildbuy_use_flags: 'int'  # uint32
    texture_id: 'int'  # fixed uint64
    attributes: 'bytes'
    material_variant: 'int'  # uint32
    texture_effect: 'int'  # uint32
    multicolor: 'RepeatedCompositeFieldContainer[Vector3]'


class LotObjectList(Message):
    # __init__
    lot_id: 'int'  # uint32
    lot_objects: 'RepeatedCompositeFieldContainer[LotObject]'


class LotTemplate(Message):
    # __init__
    lot_object_list: 'LotObjectList'
    architecture: 'bytes'
