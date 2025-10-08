from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer
from enum import IntEnum

from protocolbuffers.Venue_pb2 import *


class RecipeItem(Message):
    class ItemType(IntEnum):
        NORMAL: 'RecipeItem.ItemType' = 0
        SPECIAL: 'RecipeItem.ItemType' = 1

    NORMAL = ItemType.NORMAL
    SPECIAL = ItemType.SPECIAL

    # __init__
    recipe_id: 'int'  # uint64
    item_type: 'RecipeItem.ItemType'
    price_override: 'int'  # int32


class Course(Message):
    # __init__
    items: 'RepeatedCompositeFieldContainer[RecipeItem]'
    course_tag: 'int'  # uint32


class Menu(Message):
    # __init__
    courses: 'RepeatedCompositeFieldContainer[Course]'


class SimOrders(Message):
    # __init__
    sim_orders: 'RepeatedCompositeFieldContainer[SimOrder]'
    meal_cost: 'int'  # uint32
    is_recommendation: 'bool'


class SimOrder(Message):
    # __init__
    sim_id: 'int'  # uint64
    recipe_id: 'int'  # uint64
    locked: 'bool'
    course_tag: 'int'  # uint32


class ShowMenu(Message):
    # __init__
    menu: 'Menu'
    sim_orders: 'RepeatedCompositeFieldContainer[SimOrder]'
    sim_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    chef_order: 'bool'
    running_bill_total: 'int'  # uint32
    recommend_order: 'bool'


class Order(Message):
    # __init__
    sim_orders: 'RepeatedCompositeFieldContainer[SimOrder]'


class RestaurantConfiguration(Message):
    class RestaurantOutfitType(IntEnum):
        MALE_CHEF: 'RestaurantConfiguration.RestaurantOutfitType' = 0
        FEMALE_CHEF: 'RestaurantConfiguration.RestaurantOutfitType' = 1
        MALE_WAITER: 'RestaurantConfiguration.RestaurantOutfitType' = 2
        FEMALE_WAITER: 'RestaurantConfiguration.RestaurantOutfitType' = 3
        MALE_HOST: 'RestaurantConfiguration.RestaurantOutfitType' = 4
        FEMALE_HOST: 'RestaurantConfiguration.RestaurantOutfitType' = 5

    MALE_CHEF = RestaurantOutfitType.MALE_CHEF
    FEMALE_CHEF = RestaurantOutfitType.FEMALE_CHEF
    MALE_WAITER = RestaurantOutfitType.MALE_WAITER
    FEMALE_WAITER = RestaurantOutfitType.FEMALE_WAITER
    MALE_HOST = RestaurantOutfitType.MALE_HOST
    FEMALE_HOST = RestaurantOutfitType.FEMALE_HOST

    # __init__
    attire_id: 'int'  # uint32
    preset_id: 'int'  # uint64
    custom_menu: 'Menu'
    outfits: 'RepeatedCompositeFieldContainer[CareerOutfit]'
