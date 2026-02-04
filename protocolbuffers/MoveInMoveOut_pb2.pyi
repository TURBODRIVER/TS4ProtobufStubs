from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer


class MoveInData(Message):
    # __init__
    furnished: 'bool'
    empty_lot: 'bool'
    household_id: 'int'  # uint64
    delta_funds: 'int'  # int64
    zone_name: 'str'
    purchase_without_moving: 'bool'
    new_venue_type: 'int'  # fixed uint64


class MoveOutData(Message):
    # __init__
    sell_furniture: 'bool'
    delta_funds: 'int'  # int64
    sell_without_moving: 'bool'


class MoveInMoveOutData(Message):
    # __init__
    zone_src: 'int'  # uint64
    zone_dst: 'int'  # uint64
    move_in_data: 'MoveInData'
    move_out_data_src: 'MoveOutData'
    move_out_data_dst: 'MoveOutData'
    households_to_update: 'RepeatedCompositeFieldContainer[int]'  # uint64
    travel_groups_to_update: 'RepeatedCompositeFieldContainer[int]'  # uint64
    retail_lots_to_update: 'RepeatedCompositeFieldContainer[int]'  # uint64
    notify_gameplay: 'bool'
    is_evict: 'bool'
