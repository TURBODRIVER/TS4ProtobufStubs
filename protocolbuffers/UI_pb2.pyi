from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer
from enum import IntEnum

from protocolbuffers.Consts_pb2 import *
from protocolbuffers.Sparse_pb2 import *
from protocolbuffers.ResourceKey_pb2 import *
from protocolbuffers.Localization_pb2 import *
from protocolbuffers.Math_pb2 import *


class BookCategoryDisplayType(IntEnum):
    DEFAULT: 'BookCategoryDisplayType' = 0
    WITCH_PRACTICAL_SPELL: 'BookCategoryDisplayType' = 1
    WITCH_MISCHIEF_SPELL: 'BookCategoryDisplayType' = 2
    WITCH_UNTAMED_SPELL: 'BookCategoryDisplayType' = 3
    WITCH_POTION: 'BookCategoryDisplayType' = 4


DEFAULT = BookCategoryDisplayType.DEFAULT
WITCH_PRACTICAL_SPELL = BookCategoryDisplayType.WITCH_PRACTICAL_SPELL
WITCH_MISCHIEF_SPELL = BookCategoryDisplayType.WITCH_MISCHIEF_SPELL
WITCH_UNTAMED_SPELL = BookCategoryDisplayType.WITCH_UNTAMED_SPELL
WITCH_POTION = BookCategoryDisplayType.WITCH_POTION


class UiValue(Message):
    # __init__
    raw_int: 'int'  # int32
    raw_float: 'float'  # float32
    raw_string: 'str'
    raw_bool: 'bool'
    resource_key: 'ResourceKey'


class ObjectTimer(Message):
    # __init__
    time: 'int'  # uint64
    text: 'LocalizedString'
    object_name: 'LocalizedString'
    finished_text: 'LocalizedString'
    must_update_timer: 'bool'
    last_updated_time: 'int'  # uint64
    timer_header: 'LocalizedString'


class UiObjectMetadata(Message):
    class HoverTipStyle(IntEnum):
        HOVER_TIP_DISABLED: 'UiObjectMetadata.HoverTipStyle' = 0
        HOVER_TIP_DEFAULT: 'UiObjectMetadata.HoverTipStyle' = 1
        HOVER_TIP_CONSUMABLE_CRAFTABLE: 'UiObjectMetadata.HoverTipStyle' = 2
        HOVER_TIP_GARDENING: 'UiObjectMetadata.HoverTipStyle' = 3
        HOVER_TIP_COLLECTION: 'UiObjectMetadata.HoverTipStyle' = 4
        HOVER_TIP_CUSTOM_OBJECT: 'UiObjectMetadata.HoverTipStyle' = 5
        HOVER_TIP_ICON_TITLE_DESCRIPTION: 'UiObjectMetadata.HoverTipStyle' = 6
        HOVER_TIP_OBJECT_RELATIONSHIP: 'UiObjectMetadata.HoverTipStyle' = 7
        HOVER_TIP_HEIRLOOM_OBJECT: 'UiObjectMetadata.HoverTipStyle' = 8

    HOVER_TIP_DISABLED = HoverTipStyle.HOVER_TIP_DISABLED
    HOVER_TIP_DEFAULT = HoverTipStyle.HOVER_TIP_DEFAULT
    HOVER_TIP_CONSUMABLE_CRAFTABLE = HoverTipStyle.HOVER_TIP_CONSUMABLE_CRAFTABLE
    HOVER_TIP_GARDENING = HoverTipStyle.HOVER_TIP_GARDENING
    HOVER_TIP_COLLECTION = HoverTipStyle.HOVER_TIP_COLLECTION
    HOVER_TIP_CUSTOM_OBJECT = HoverTipStyle.HOVER_TIP_CUSTOM_OBJECT
    HOVER_TIP_ICON_TITLE_DESCRIPTION = HoverTipStyle.HOVER_TIP_ICON_TITLE_DESCRIPTION
    HOVER_TIP_OBJECT_RELATIONSHIP = HoverTipStyle.HOVER_TIP_OBJECT_RELATIONSHIP
    HOVER_TIP_HEIRLOOM_OBJECT = HoverTipStyle.HOVER_TIP_HEIRLOOM_OBJECT

    # __init__
    sparse_data: 'SparseMessageData'
    hover_tip: 'UiObjectMetadata.HoverTipStyle'
    debug_hover_tip: 'UiObjectMetadata.HoverTipStyle'
    custom_name: 'str'
    recipe_name: 'LocalizedString'
    crafter_sim_id: 'int'  # fixed uint64
    buff_effects: 'RepeatedCompositeFieldContainer[LocalizedString]'
    recipe_description: 'LocalizedString'
    quality: 'int'  # uint32
    servings: 'int'  # uint32
    spoiled_time: 'int'  # uint64
    percentage_left: 'LocalizedString'
    style_name: 'LocalizedString'
    simoleon_value: 'int'  # uint32
    main_icon: 'ResourceKey'
    sub_icons: 'RepeatedCompositeFieldContainer[ResourceKey]'
    quality_description: 'LocalizedString'
    quality_color: 'int'  # fixed uint32
    object_info_names: 'RepeatedCompositeFieldContainer[LocalizedString]'
    object_info_descriptions: 'RepeatedCompositeFieldContainer[LocalizedString]'
    inscription: 'str'
    custom_description: 'str'
    header: 'LocalizedString'
    subtext: 'LocalizedString'
    crafted_by_text: 'LocalizedString'
    stolen_from_text: 'LocalizedString'
    rarity_text: 'LocalizedString'
    simoleon_text: 'LocalizedString'
    relic_description: 'LocalizedString'
    evolution_progress: 'float'  # float32
    season_text: 'LocalizedString'
    spoiled_time_text: 'LocalizedString'
    rel_override_id: 'int'  # uint64
    icon_infos: 'RepeatedCompositeFieldContainer[IconInfo]'
    simoleon_custom_text: 'LocalizedString'
    creature_type: 'int'  # uint32
    header_subtext: 'LocalizedString'
    header_status: 'LocalizedString'
    mark_up_value: 'int'  # uint32
    object_timers: 'RepeatedCompositeFieldContainer[ObjectTimer]'
    footer_text: 'LocalizedString'
    heirloom_sim_id: 'int'  # fixed uint64
    heirloom_title: 'LocalizedString'
    heirloom_owner: 'LocalizedString'
    engraved_message: 'LocalizedString'
    mark_up_value_tooltip: 'int'  # int32
    enchantment_time: 'int'  # uint64
    active_seasons_text: 'LocalizedString'


class HovertipCreated(Message):
    # __init__
    is_from_ui: 'bool'
    is_success: 'bool'


class BoundObjectUpdate(Message):
    # __init__
    object_id: 'int'  # uint64
    bone_name: 'str'
    world_offset_x: 'float'  # float32
    world_offset_y: 'float'  # float32
    world_offset_z: 'float'  # float32


class IconInfo(Message):
    class CanvasStateType(IntEnum):
        PAINTING_CROSSSTITCH: 'IconInfo.CanvasStateType' = 0
        PUZZLE: 'IconInfo.CanvasStateType' = 1

    PAINTING_CROSSSTITCH = CanvasStateType.PAINTING_CROSSSTITCH
    PUZZLE = CanvasStateType.PUZZLE

    # __init__
    name: 'LocalizedString'
    icon: 'ResourceKey'
    desc: 'LocalizedString'
    icon_object: 'ManagerObjectId'
    icon_object_def: 'DefinitionGeoPair'
    texture_id: 'int'  # fixed uint64
    object_instance_id: 'int'  # fixed uint64
    texture_effect: 'int'  # fixed uint64
    control_id: 'int'  # uint32
    tooltip: 'LocalizedString'
    canvas_state_type: 'IconInfo.CanvasStateType'
    location_desc: 'LocalizedString'
    multicolor: 'RepeatedCompositeFieldContainer[Vector3]'
    main_objective: 'LocalizedString'
    parent_id: 'int'  # fixed uint64


class InventoryUpdate(Message):
    # __init__
    sim_id: 'int'  # uint64
    size: 'int'  # uint32


class InventoryItemSortData(Message):
    # __init__
    value: 'float'  # float32
    type: 'int'  # uint32


class DynamicInventoryItemData(Message):
    # __init__
    value: 'int'  # uint32
    locked: 'bool'
    in_use: 'bool'
    crafting_quality: 'int'  # int32
    count: 'int'  # uint32
    new_object_id: 'int'  # uint64
    is_new: 'bool'
    sort_order: 'int'  # uint32
    icon_info: 'IconInfo'
    custom_name: 'str'
    recipe_name: 'LocalizedString'
    sort_data: 'RepeatedCompositeFieldContainer[InventoryItemSortData]'
    is_favorite: 'bool'
    dynamic_tags: 'RepeatedCompositeFieldContainer[int]'  # uint32
    visual_state: 'str'
    visual_icon_state: 'str'
    is_sell_disabled_from_component: 'bool'


class InventoryItemData(Message):
    # __init__
    definition_id: 'int'  # uint64
    dynamic_data: 'DynamicInventoryItemData'


class SimInventoryItemUpdate(Message):
    class UpdateType(IntEnum):
        TYPE_ADD: 'SimInventoryItemUpdate.UpdateType' = 0
        TYPE_UPDATE: 'SimInventoryItemUpdate.UpdateType' = 1
        TYPE_REMOVE: 'SimInventoryItemUpdate.UpdateType' = 2

    TYPE_ADD = UpdateType.TYPE_ADD
    TYPE_UPDATE = UpdateType.TYPE_UPDATE
    TYPE_REMOVE = UpdateType.TYPE_REMOVE

    # __init__
    type: 'SimInventoryItemUpdate.UpdateType'
    sim_id: 'int'  # uint64
    object_id: 'int'  # uint64
    add_data: 'InventoryItemData'
    update_data: 'DynamicInventoryItemData'
    object_inventory_type: 'int'  # uint64
    stack_id: 'int'  # uint64


class InventoryItemUpdate(Message):
    class UpdateType(IntEnum):
        TYPE_ADD: 'InventoryItemUpdate.UpdateType' = 0
        TYPE_UPDATE: 'InventoryItemUpdate.UpdateType' = 1
        TYPE_REMOVE: 'InventoryItemUpdate.UpdateType' = 2
        TYPE_SET_STACK_OPTION: 'InventoryItemUpdate.UpdateType' = 3

    TYPE_ADD = UpdateType.TYPE_ADD
    TYPE_UPDATE = UpdateType.TYPE_UPDATE
    TYPE_REMOVE = UpdateType.TYPE_REMOVE
    TYPE_SET_STACK_OPTION = UpdateType.TYPE_SET_STACK_OPTION

    class InventoryType(IntEnum):
        TYPE_OBJECT: 'InventoryItemUpdate.InventoryType' = 0
        TYPE_SHARED: 'InventoryItemUpdate.InventoryType' = 1

    TYPE_OBJECT = InventoryType.TYPE_OBJECT
    TYPE_SHARED = InventoryType.TYPE_SHARED

    # __init__
    type: 'InventoryItemUpdate.UpdateType'
    inventory_id: 'int'  # uint64
    object_id: 'int'  # uint64
    add_data: 'InventoryItemData'
    update_data: 'DynamicInventoryItemData'
    inventory_type: 'InventoryItemUpdate.InventoryType'
    stack_id: 'int'  # uint64


class OpenInventory(Message):
    # __init__
    object_id: 'int'  # uint64
    inventory_type: 'InventoryItemUpdate.InventoryType'
    inventory_id: 'int'  # uint64
    sim_only: 'bool'


class OpenInventoryWithPreselectedFilters(Message):
    # __init__
    object_id: 'int'  # uint64
    inventory_type: 'InventoryItemUpdate.InventoryType'
    inventory_id: 'int'  # uint64
    filter_tag: 'int'  # uint32


class CollectibleItemUpdate(Message):
    class UpdateType(IntEnum):
        TYPE_ADD: 'CollectibleItemUpdate.UpdateType' = 0
        TYPE_REMOVE: 'CollectibleItemUpdate.UpdateType' = 1
        TYPE_DISCOVERY: 'CollectibleItemUpdate.UpdateType' = 2

    TYPE_ADD = UpdateType.TYPE_ADD
    TYPE_REMOVE = UpdateType.TYPE_REMOVE
    TYPE_DISCOVERY = UpdateType.TYPE_DISCOVERY

    # __init__
    type: 'CollectibleItemUpdate.UpdateType'
    collection_id: 'int'  # uint64
    household_id: 'int'  # uint64
    object_id: 'int'  # uint64
    object_def_id: 'int'  # uint64
    sim_id: 'int'  # uint64
    quality: 'int'  # uint32
    icon_info: 'IconInfo'
    order_discovered: 'int'  # uint32


class IncrementCommunityCollectableCount(Message):
    # __init__
    count: 'int'  # uint32


class ShowObjectInventory(Message):
    # __init__
    name: 'LocalizedString'
    items: 'RepeatedCompositeFieldContainer[InventoryItemData]'


class InventoryCountUpdate(Message):
    class InventoryCount():
        # __init__
        inventory_type: 'int'  # uint32
        count: 'int'  # uint32

    # __init__
    inventory_counts: 'RepeatedCompositeFieldContainer[InventoryCountUpdate.InventoryCount]'
    inventory_type: 'int'  # uint32
    count: 'int'  # uint32


class GameSaveCheatLock(Message):
    # __init__
    slot_id: 'int'  # uint32


class GameSaveComplete(Message):
    # __init__
    return_status: 'int'  # uint32
    save_cooldown: 'float'  # float32
    failure_reason: 'LocalizedString'
    slot_id: 'int'  # uint32


class GameSaveLockUnlock(Message):
    # __init__
    is_locked: 'bool'
    lock_reason: 'LocalizedString'


class UiScreenSlam(Message):
    class Types(IntEnum):
        LEGACY: 'UiScreenSlam.Types' = 0
        CUSTOM: 'UiScreenSlam.Types' = 1

    LEGACY = Types.LEGACY
    CUSTOM = Types.CUSTOM

    class Size(IntEnum):
        SMALL: 'UiScreenSlam.Size' = 0
        MEDIUM: 'UiScreenSlam.Size' = 1
        LARGE: 'UiScreenSlam.Size' = 2
        EXTRA_LARGE: 'UiScreenSlam.Size' = 3

    SMALL = Size.SMALL
    MEDIUM = Size.MEDIUM
    LARGE = Size.LARGE
    EXTRA_LARGE = Size.EXTRA_LARGE

    # __init__
    type: 'int'  # uint32
    name: 'LocalizedString'
    icon: 'ResourceKey'
    size: 'int'  # uint32
    title: 'LocalizedString'
    sim_id: 'int'  # uint64
    ui_key: 'str'
    audio_sting: 'ResourceKey'


class LotDisplayInfo(Message):
    # __init__
    lot_name: 'str'
    household_name: 'str'
    icon_infos: 'RepeatedCompositeFieldContainer[IconInfo]'
    lot_challenges: 'RepeatedCompositeFieldContainer[LocalizedString]'


class HouseholdDisplayInfo(Message):
    # __init__
    household_id: 'int'  # fixed uint64
    lot_id: 'int'  # fixed uint64
    at_home_sim_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class SimRelativeLotLocation(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    on_active_lot: 'bool'
    home_zone_active: 'bool'
    is_on_vacation: 'bool'


class LightColorAndIntensity(Message):
    # __init__
    red: 'int'  # uint32
    green: 'int'  # uint32
    blue: 'int'  # uint32
    intensity: 'float'  # float32
    target_id: 'int'  # fixed uint64
    response_id: 'int'  # uint32
    checkbox_state: 'bool'
    palette: 'int'  # uint32
    style: 'int'  # uint32
    grid_label: 'LocalizedString'
    slider_label: 'LocalizedString'


class SatisfyTutorialTip(Message):
    # __init__
    tutorial_tip_id: 'int'  # fixed uint64


class ActiveTutorialTipGroup(Message):
    class ActionType(IntEnum):
        ACTIVATE: 'ActiveTutorialTipGroup.ActionType' = 0
        DEACTIVATE: 'ActiveTutorialTipGroup.ActionType' = 1

    ACTIVATE = ActionType.ACTIVATE
    DEACTIVATE = ActionType.DEACTIVATE

    class ContextType(IntEnum):
        NONE: 'ActiveTutorialTipGroup.ContextType' = 0
        GENERAL: 'ActiveTutorialTipGroup.ContextType' = 1
        GUIDANCE_TIP: 'ActiveTutorialTipGroup.ContextType' = 2

    NONE = ContextType.NONE
    GENERAL = ContextType.GENERAL
    GUIDANCE_TIP = ContextType.GUIDANCE_TIP

    # __init__
    group_id: 'int'  # fixed uint64
    action_type: 'ActiveTutorialTipGroup.ActionType'
    context_type: 'ActiveTutorialTipGroup.ContextType'
    context_id: 'int'  # fixed uint64
    result: 'bool'


class GuidanceTipResult(Message):
    class ResponseType(IntEnum):
        SUCCESS: 'GuidanceTipResult.ResponseType' = 0
        CANCEL: 'GuidanceTipResult.ResponseType' = 1

    SUCCESS = ResponseType.SUCCESS
    CANCEL = ResponseType.CANCEL

    # __init__
    item_id: 'int'  # fixed uint64
    response: 'GuidanceTipResult.ResponseType'


class IsGuidanceTipComplete(Message):
    # __init__
    guidance_tip_id: 'int'  # fixed uint64


class ShowMapView(Message):
    class MapViewMode(IntEnum):
        TRAVEL: 'ShowMapView.MapViewMode' = 0
        VACATION: 'ShowMapView.MapViewMode' = 1
        PURCHASE: 'ShowMapView.MapViewMode' = 2
        CHANGE_VENUE: 'ShowMapView.MapViewMode' = 3

    TRAVEL = MapViewMode.TRAVEL
    VACATION = MapViewMode.VACATION
    PURCHASE = MapViewMode.PURCHASE
    CHANGE_VENUE = MapViewMode.CHANGE_VENUE

    # __init__
    actor_sim_id: 'int'  # fixed uint64
    lot_ids_for_travel: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    dialog_id: 'int'  # uint32
    traveling_sim_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    is_vacation: 'bool'
    mode: 'ShowMapView.MapViewMode'
    purchase_venue_type: 'int'  # fixed uint64
    venue_types_allowed: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    target_sim_id: 'int'  # fixed uint64


class ShowPlexView(Message):
    # __init__
    actor_sim_id: 'int'  # fixed uint64
    lot_ids_for_travel: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    dialog_id: 'int'  # uint32
    traveling_sim_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class SimTravelAvailability(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    is_active_household: 'bool'
    household_id: 'int'  # fixed uint64
    is_at_work: 'bool'
    zone_id: 'int'  # fixed uint64
    age: 'int'  # uint32
    selected_by_default: 'bool'


class AvailableSimsForTravel(Message):
    # __init__
    actor_sim_id: 'int'  # fixed uint64
    sim_ids_for_travel: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    available_sims: 'RepeatedCompositeFieldContainer[SimTravelAvailability]'


class ExtendVacation(Message):
    # __init__
    travel_group_id: 'int'  # fixed uint64
    zone_id: 'int'  # fixed uint64
    sim_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    days_remaining: 'float'  # float32
    household_description_id: 'int'  # fixed uint64
    lot_name: 'str'
    lot_daily_cost: 'int'  # uint32
    is_getaway: 'bool'
    dialog_type: 'int'  # uint32


class SimInfoLocationStatus(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    age: 'int'  # uint32
    is_at_home: 'bool'
    zone_id: 'int'  # fixed uint64


class HouseholdLocationStatus(Message):
    # __init__
    household_id: 'int'  # fixed uint64
    household_name: 'str'
    home_zone_id: 'int'  # fixed uint64
    sim_info_status: 'RepeatedCompositeFieldContainer[SimInfoLocationStatus]'
    is_played: 'bool'


class TravelViewHouseholdsInfo(Message):
    # __init__
    household_locations: 'RepeatedCompositeFieldContainer[HouseholdLocationStatus]'


class NotebookEntryListMessage(Message):
    # __init__
    item_message: 'LocalizedString'
    item_count: 'int'  # uint32
    item_total: 'int'  # uint32
    item_icon: 'IconInfo'
    item_tooltip: 'LocalizedString'
    new_item: 'bool'


class NotebookEntryMessage(Message):
    # __init__
    entry_message: 'LocalizedString'
    entry_icon: 'IconInfo'
    entry_tooltip: 'LocalizedString'
    entry_list: 'RepeatedCompositeFieldContainer[NotebookEntryListMessage]'
    new_entry: 'bool'
    entry_list_description: 'LocalizedString'
    entry_metadata_hovertip: 'UiObjectMetadata'
    entry_id: 'int'  # uint32
    is_sortable: 'bool'
    is_new_item_sortable: 'bool'
    entry_message_description: 'LocalizedString'


class NotebookSubCategoryMessage(Message):
    class NotebookEntryStyle(IntEnum):
        NOTEBOOK_EXPANDABLE: 'NotebookSubCategoryMessage.NotebookEntryStyle' = 0
        NOTEBOOK_NUMBERED: 'NotebookSubCategoryMessage.NotebookEntryStyle' = 1
        NOTEBOOK_ICON_DESCRIPTION: 'NotebookSubCategoryMessage.NotebookEntryStyle' = 2
        NOTEBOOK_EXPANDABLE_SINGLE: 'NotebookSubCategoryMessage.NotebookEntryStyle' = 3

    NOTEBOOK_EXPANDABLE = NotebookEntryStyle.NOTEBOOK_EXPANDABLE
    NOTEBOOK_NUMBERED = NotebookEntryStyle.NOTEBOOK_NUMBERED
    NOTEBOOK_ICON_DESCRIPTION = NotebookEntryStyle.NOTEBOOK_ICON_DESCRIPTION
    NOTEBOOK_EXPANDABLE_SINGLE = NotebookEntryStyle.NOTEBOOK_EXPANDABLE_SINGLE

    # __init__
    subcategory_name: 'LocalizedString'
    subcategory_icon: 'IconInfo'
    subcategory_tooltip: 'LocalizedString'
    entry_type: 'NotebookSubCategoryMessage.NotebookEntryStyle'
    max_num_entries: 'int'  # uint32
    entries: 'RepeatedCompositeFieldContainer[NotebookEntryMessage]'
    subcategory_id: 'int'  # uint32
    is_sortable: 'bool'
    is_new_entry_sortable: 'bool'


class NotebookCategoryMessage(Message):
    # __init__
    category_name: 'LocalizedString'
    category_icon: 'IconInfo'
    subcategories: 'RepeatedCompositeFieldContainer[NotebookSubCategoryMessage]'
    category_description: 'LocalizedString'
    enum_name: 'str'
    category_large_icon: 'IconInfo'


class NotebookView(Message):
    # __init__
    categories: 'RepeatedCompositeFieldContainer[NotebookCategoryMessage]'
    selected_category_index: 'int'  # uint32
    selected_subcategory_index: 'int'  # uint32
    notes: 'str'
    open_page: 'bool'


class InterrogationProgressUpdate(Message):
    class UpdateType(IntEnum):
        TYPE_START: 'InterrogationProgressUpdate.UpdateType' = 0
        TYPE_UPDATE: 'InterrogationProgressUpdate.UpdateType' = 1
        TYPE_STOP: 'InterrogationProgressUpdate.UpdateType' = 2

    TYPE_START = UpdateType.TYPE_START
    TYPE_UPDATE = UpdateType.TYPE_UPDATE
    TYPE_STOP = UpdateType.TYPE_STOP

    # __init__
    type: 'InterrogationProgressUpdate.UpdateType'
    target_id: 'int'  # uint64
    value: 'float'  # float32
    decay_rate: 'float'  # float32


class ObjectRelationshipUpdate(Message):
    class UpdateType(IntEnum):
        TYPE_START: 'ObjectRelationshipUpdate.UpdateType' = 0
        TYPE_UPDATE: 'ObjectRelationshipUpdate.UpdateType' = 1
        TYPE_STOP: 'ObjectRelationshipUpdate.UpdateType' = 2

    TYPE_START = UpdateType.TYPE_START
    TYPE_UPDATE = UpdateType.TYPE_UPDATE
    TYPE_STOP = UpdateType.TYPE_STOP

    # __init__
    type: 'ObjectRelationshipUpdate.UpdateType'
    target_id: 'int'  # uint64
    value: 'float'  # float32


class BreakThroughMessage(Message):
    # __init__
    sim_id: 'int'  # uint64
    progress: 'int'  # uint32
    display_time: 'float'  # float32


class PurchaseIntentUpdate(Message):
    # __init__
    sim_id: 'int'  # uint64
    curr_value: 'int'  # uint32
    target_value: 'int'  # uint32
    show_continuously: 'bool'


class RetailMarkupMultiplierEntry(Message):
    # __init__
    name: 'LocalizedString'
    multiplier: 'float'  # float32
    is_selected: 'bool'


class RetailMarkupMultiplierMessage(Message):
    # __init__
    markup_multipliers: 'RepeatedCompositeFieldContainer[RetailMarkupMultiplierEntry]'


class OwnedRetailLotCountMessage(Message):
    # __init__
    owned_lot_count: 'int'  # uint32


class BuildBuyLockUnlock(Message):
    # __init__
    build_buy_locked: 'bool'
    reason: 'LocalizedString'


class DynamicSignActivityInfo(Message):
    # __init__
    name: 'LocalizedString'
    description: 'LocalizedString'
    icon: 'IconInfo'


class DynamicSignView(Message):
    class DynamicSignType(IntEnum):
        DEFAULT: 'DynamicSignView.DynamicSignType' = 0
        SCENARIO: 'DynamicSignView.DynamicSignType' = 1

    DEFAULT = DynamicSignType.DEFAULT
    SCENARIO = DynamicSignType.SCENARIO

    # __init__
    name: 'LocalizedString'
    venue: 'LocalizedString'
    time: 'LocalizedString'
    image: 'ResourceKey'
    activities: 'RepeatedCompositeFieldContainer[DynamicSignActivityInfo]'
    action_label: 'LocalizedString'
    disabled_tooltip: 'LocalizedString'
    background_image: 'ResourceKey'
    drama_node_guid: 'int'  # uint64
    household_id: 'int'  # uint64
    time_spent: 'float'  # float32
    sign_type: 'DynamicSignView.DynamicSignType'


class SimAlertUpdate(Message):
    class AlertType(IntEnum):
        NONE: 'SimAlertUpdate.AlertType' = 0
        PET_DISTRESS: 'SimAlertUpdate.AlertType' = 1

    NONE = AlertType.NONE
    PET_DISTRESS = AlertType.PET_DISTRESS

    # __init__
    sim_id: 'int'  # fixed uint64
    alert_type: 'SimAlertUpdate.AlertType'


class FestivalActivityData(Message):
    # __init__
    name: 'LocalizedString'
    icon: 'IconInfo'
    description: 'LocalizedString'


class CalendarEntry(Message):
    # __init__
    entry_type: 'int'  # uint32
    entry_id: 'int'  # uint64
    icon_info: 'IconInfo'
    start_time: 'int'  # uint64
    end_time: 'int'  # uint64
    scoring_enabled: 'bool'
    lot_id: 'int'  # uint64
    household_sim_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    tradition_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    holiday_id: 'int'  # uint64
    zone_id: 'int'  # uint64
    deletable: 'bool'
    festival_activities: 'RepeatedCompositeFieldContainer[FestivalActivityData]'
    favorited: 'bool'
    entry_guid: 'int'  # uint64
    show_go_to_event_button: 'bool'
    in_progress: 'bool'
    getaway_name: 'str'
    getaway_duration: 'int'  # uint32
    getaway_recurring_days: 'RepeatedCompositeFieldContainer[int]'  # uint32


class CalendarUpdate(Message):
    class CalendarUpdateType(IntEnum):
        ADD: 'CalendarUpdate.CalendarUpdateType' = 0
        REMOVE: 'CalendarUpdate.CalendarUpdateType' = 1
        UPDATE: 'CalendarUpdate.CalendarUpdateType' = 2

    ADD = CalendarUpdateType.ADD
    REMOVE = CalendarUpdateType.REMOVE
    UPDATE = CalendarUpdateType.UPDATE

    # __init__
    update_type: 'CalendarUpdate.CalendarUpdateType'
    updated_entry: 'CalendarEntry'


class Calendar(Message):
    # __init__
    calendar_entries: 'RepeatedCompositeFieldContainer[CalendarEntry]'


class SeasonUpdate(Message):
    class SeasonType(IntEnum):
        SUMMER: 'SeasonUpdate.SeasonType' = 0
        FALL: 'SeasonUpdate.SeasonType' = 1
        WINTER: 'SeasonUpdate.SeasonType' = 2
        SPRING: 'SeasonUpdate.SeasonType' = 3

    SUMMER = SeasonType.SUMMER
    FALL = SeasonType.FALL
    WINTER = SeasonType.WINTER
    SPRING = SeasonType.SPRING

    # __init__
    season_type: 'SeasonUpdate.SeasonType'
    season_guid: 'int'  # uint64
    season_start_time: 'int'  # uint64


class PrepTaskData(Message):
    # __init__
    task_name: 'LocalizedString'
    task_icon: 'ResourceKey'
    is_completed: 'bool'
    task_tooltip: 'LocalizedString'


class PrepTaskUpdate(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    gig_uid: 'int'  # uint64
    prep_tasks: 'RepeatedCompositeFieldContainer[PrepTaskData]'


class UniversityMajorData(Message):
    class UniversityMajorStatus(IntEnum):
        NOT_ACCEPTED: 'UniversityMajorData.UniversityMajorStatus' = 0
        ACCEPTED: 'UniversityMajorData.UniversityMajorStatus' = 1
        GRADUATED: 'UniversityMajorData.UniversityMajorStatus' = 2

    NOT_ACCEPTED = UniversityMajorStatus.NOT_ACCEPTED
    ACCEPTED = UniversityMajorStatus.ACCEPTED
    GRADUATED = UniversityMajorStatus.GRADUATED

    # __init__
    major_id: 'int'  # uint64
    core_class_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    class_remaining: 'int'  # uint32
    status: 'UniversityMajorData.UniversityMajorStatus'


class UniversityData(Message):
    # __init__
    university_id: 'int'  # uint64
    degrees: 'RepeatedCompositeFieldContainer[UniversityMajorData]'
    elective_class_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64


class UniversityEnrollmentSimData(Message):
    # __init__
    university_id: 'int'  # uint64
    major_id: 'int'  # uint64


class UniversityEnrollmentData(Message):
    # __init__
    universities: 'RepeatedCompositeFieldContainer[UniversityData]'
    housing_zone_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    current_enrollment: 'UniversityEnrollmentSimData'
    household_id: 'int'  # fixed uint64
    scholarships: 'RepeatedCompositeFieldContainer[UniversityScholarship]'
    is_pregnant: 'bool'


class UniversityScholarship(Message):
    # __init__
    scholarship_id: 'int'  # uint64
    value: 'int'  # uint32


class BookView(Message):
    class BookDisplayStyle(IntEnum):
        DEFAULT: 'BookView.BookDisplayStyle' = 0
        WITCH: 'BookView.BookDisplayStyle' = 1

    DEFAULT = BookDisplayStyle.DEFAULT
    WITCH = BookDisplayStyle.WITCH

    # __init__
    pages: 'RepeatedCompositeFieldContainer[BookPageMessage]'
    style: 'BookView.BookDisplayStyle'
    tabs: 'RepeatedCompositeFieldContainer[BookTabMessage]'
    context: 'str'


class BookCategoryMessage(Message):
    # __init__
    first_page_index: 'int'  # uint32
    name: 'LocalizedString'
    icon: 'ResourceKey'
    tooltip_text: 'LocalizedString'
    progress: 'int'  # uint32
    progress_title: 'LocalizedString'
    progress_text: 'LocalizedString'
    new_entries: 'RepeatedCompositeFieldContainer[int]'  # uint64


class BookEntryMessage(Message):
    # __init__
    id: 'int'  # uint64
    name: 'LocalizedString'
    description: 'LocalizedString'
    icon: 'ResourceKey'
    subtext_title: 'LocalizedString'
    subtext: 'LocalizedString'
    tooltip_text: 'LocalizedString'
    category_type: 'BookCategoryDisplayType'
    status_flags: 'int'  # uint32


class BookPageMessage(Message):
    class BookPageType(IntEnum):
        BLANK: 'BookPageMessage.BookPageType' = 0
        FRONT: 'BookPageMessage.BookPageType' = 1
        CATEGORY_LIST: 'BookPageMessage.BookPageType' = 2
        CATEGORY_FRONT: 'BookPageMessage.BookPageType' = 3
        CATEGORY: 'BookPageMessage.BookPageType' = 4

    BLANK = BookPageType.BLANK
    FRONT = BookPageType.FRONT
    CATEGORY_LIST = BookPageType.CATEGORY_LIST
    CATEGORY_FRONT = BookPageType.CATEGORY_FRONT
    CATEGORY = BookPageType.CATEGORY

    # __init__
    type: 'BookPageMessage.BookPageType'
    title: 'LocalizedString'
    description: 'LocalizedString'
    icon: 'ResourceKey'
    category_type: 'BookCategoryDisplayType'
    categories: 'RepeatedCompositeFieldContainer[BookCategoryMessage]'
    entries: 'RepeatedCompositeFieldContainer[BookEntryMessage]'


class BookTabMessage(Message):
    # __init__
    first_page_index: 'int'  # uint32
    icon_info: 'IconInfo'


class SplitHousehold(Message):
    # __init__
    source_household_id: 'int'  # uint64
    target_household_id: 'int'  # uint64
    to_source_sims: 'RepeatedCompositeFieldContainer[int]'  # uint64
    to_target_sims: 'RepeatedCompositeFieldContainer[int]'  # uint64
    source_funds_difference: 'int'  # int64
    target_funds_difference: 'int'  # int64
    destination_zone_id: 'int'  # uint64
    funds: 'int'  # int64
    bSellFurniture: 'bool'


class CivicPolicy(Message):
    # __init__
    policy_id: 'int'  # uint64
    count: 'int'  # uint32
    max_count: 'int'  # uint32


class CommunityBoardShow(Message):
    # __init__
    sim_id: 'int'  # uint64
    influence_points: 'int'  # uint32
    title: 'LocalizedString'
    enacted_policies: 'RepeatedCompositeFieldContainer[CivicPolicy]'
    balloted_policies: 'RepeatedCompositeFieldContainer[CivicPolicy]'
    new_policy_allowed: 'bool'
    disabled_tooltip: 'LocalizedString'
    provider_type: 'int'  # uint32
    policy_disabled_tooltip: 'LocalizedString'
    new_policy_disabled_tooltip: 'LocalizedString'
    target_id: 'int'  # uint64
    schedule_text: 'LocalizedString'


class CommunityBoardResponse(Message):
    # __init__
    sim_id: 'int'  # uint64
    influence_points: 'int'  # uint32
    balloted_policies: 'RepeatedCompositeFieldContainer[CivicPolicy]'
    provider_type: 'int'  # uint32
    target_id: 'int'  # uint64


class CommunityBoardAddPolicy(Message):
    # __init__
    sim_id: 'int'  # uint64
    policy_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    new_policy_allowed: 'bool'
    policies: 'RepeatedCompositeFieldContainer[CivicPolicy]'


class BillUtilityInfo(Message):
    # __init__
    utility: 'int'  # uint64
    cost: 'int'  # int64
    max_value: 'int'  # int64
    current_value: 'int'  # int64
    utility_name: 'LocalizedString'
    rate_of_change: 'float'  # float32
    selling: 'bool'
    utility_symbol: 'int'  # int32


class BillLineItem(Message):
    # __init__
    amount: 'int'  # int32
    label: 'LocalizedString'
    tooltip: 'LocalizedString'


class ShowBillsDialog(Message):
    # __init__
    utility_info: 'RepeatedCompositeFieldContainer[BillUtilityInfo]'
    line_items: 'RepeatedCompositeFieldContainer[BillLineItem]'
    due_bills_line_items: 'RepeatedCompositeFieldContainer[BillLineItem]'


class ShowSocialMediaDialog(Message):
    # __init__
    sim_id: 'int'  # uint64
    followers_count: 'int'  # uint32
    feed_items: 'RepeatedCompositeFieldContainer[SocialMediaFeedItem]'
    messages_items: 'RepeatedCompositeFieldContainer[SocialMediaMessagesItem]'
    is_update: 'bool'
    has_new_posts: 'bool'
    has_new_messages: 'bool'
    can_make_context_post: 'bool'
    can_add_contacts: 'bool'


class SocialMediaFeedItem(Message):
    # __init__
    post_id: 'int'  # uint64
    author_sim_id: 'int'  # fixed uint64
    target_sim_id: 'int'  # fixed uint64
    post_type: 'int'  # uint32
    post_time: 'int'  # uint64
    post_text: 'LocalizedString'
    reactions: 'RepeatedCompositeFieldContainer[SocialMediaReaction]'
    has_author_reacted: 'bool'


class SocialMediaMessagesItem(Message):
    # __init__
    message_id: 'int'  # uint64
    message_post: 'SocialMediaFeedItem'
    reply_post: 'SocialMediaFeedItem'


class SocialMediaReaction(Message):
    # __init__
    narrative_type: 'int'  # uint32
    polarity_type: 'int'  # uint32
    count: 'int'  # uint32
    reacted_sims: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class ShowHorseCompetitionSelector(Message):
    # __init__
    is_update: 'bool'
    selected_sim: 'HorseCompetitionAssigneeData'
    selected_horse: 'HorseCompetitionAssigneeData'
    competition_metadatas: 'RepeatedCompositeFieldContainer[HorseCompetitionMetadata]'


class ShowMatchmakingDialog(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    trait_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    selected_ages: 'RepeatedCompositeFieldContainer[int]'  # uint32
    selected_traits: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    cooldown_mins_left: 'int'  # uint64
    num_contact_actions: 'int'  # int32
    profiles: 'RepeatedCompositeFieldContainer[MatchmakingProfile]'
    is_update: 'bool'
    saved_profiles: 'RepeatedCompositeFieldContainer[MatchmakingProfile]'
    max_save: 'int'  # int32
    attracted_options: 'RepeatedCompositeFieldContainer[int]'  # uint32
    woohoo_options: 'RepeatedCompositeFieldContainer[int]'  # uint32
    is_exploring: 'bool'
    res_key: 'ResourceKey'
    min_download_count: 'int'  # fixed uint64
    upload_time_range_start: 'int'  # fixed uint64
    update_time_range_end: 'int'  # fixed uint64
    bg_res_key: 'ResourceKey'
    gallery_sims_enabled: 'bool'
    max_contact: 'int'  # int32
    gallery_sims_favorites_only_enabled: 'bool'
    is_traits_display_update: 'bool'
    remote_ids_on_cooldown: 'RepeatedCompositeFieldContainer[str]'


class MatchmakingProfile(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    profile_type: 'int'  # uint32
    name: 'str'
    real_sim_id: 'int'  # fixed uint64
    display_traits: 'RepeatedCompositeFieldContainer[TraitAttractionScore]'
    contacted: 'bool'
    profile_bg_res_key: 'ResourceKey'
    exchange_data_creator_name: 'str'
    exchange_data_remote_id: 'str'
    exchange_data_type: 'int'  # uint32
    exchange_data_household_id: 'int'  # fixed uint64
    reported: 'bool'
    region_name: 'str'
    pose_index: 'int'  # int32
    thumbnail_url: 'str'
    rel_is_hidden: 'bool'


class TraitAttractionScore(Message):
    # __init__
    trait_id: 'int'  # fixed uint64
    score: 'int'  # int32


class HorseCompetitionMetadata(Message):
    # __init__
    competition_id: 'int'  # fixed uint64
    eligible_to_compete: 'bool'
    not_eligible_reason: 'LocalizedString'
    has_placed_previously: 'bool'
    highest_placement: 'int'  # int32


class HorseCompetitionAssigneeSkillData(Message):
    # __init__
    skill_id: 'int'  # fixed uint64
    level: 'int'  # uint32


class HorseCompetitionAssigneeData(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    mood_id: 'int'  # fixed uint64
    mood_intensity: 'int'  # uint32
    mood_tooltip: 'LocalizedString'
    skills: 'RepeatedCompositeFieldContainer[HorseCompetitionAssigneeSkillData]'


class ShowHorseCompetitionResults(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    horse_id: 'int'  # fixed uint64
    competition_id: 'int'  # fixed uint64
    placement: 'int'  # int32
    unlocked_new_competition: 'bool'
    unlocked_competition_id: 'int'  # fixed uint64


class InventoryItemSellRequest(Message):
    # __init__
    id: 'int'  # uint64
    count: 'int'  # uint32


class InventorySellRequest(Message):
    # __init__
    sim_id: 'int'  # uint64
    stacks: 'RepeatedCompositeFieldContainer[int]'  # uint64
    items: 'RepeatedCompositeFieldContainer[InventoryItemSellRequest]'
    currency_type: 'int'  # uint32


class ShowSimProfile(Message):
    # __init__
    sim_id: 'int'  # uint64
    actor_sim_id: 'int'  # uint64
    target_sim_id: 'int'  # uint64


class ToggleSimInfoPanel(Message):
    class SimInfoPanelType(IntEnum):
        SIM_INFO_MOTIVE_PANEL: 'ToggleSimInfoPanel.SimInfoPanelType' = 0
        SIM_INFO_SKILL_PANEL: 'ToggleSimInfoPanel.SimInfoPanelType' = 1
        SIM_INFO_RELATIONSHIP_PANEL: 'ToggleSimInfoPanel.SimInfoPanelType' = 2
        SIM_INFO_CAREER_PANEL: 'ToggleSimInfoPanel.SimInfoPanelType' = 3
        SIM_INFO_INVENTORY_PANEL: 'ToggleSimInfoPanel.SimInfoPanelType' = 4
        SIM_INFO_ASPIRATION_PANEL: 'ToggleSimInfoPanel.SimInfoPanelType' = 5
        SIM_INFO_SUMMARY_PANEL: 'ToggleSimInfoPanel.SimInfoPanelType' = 6
        SIM_INFO_CLUB_PANEL: 'ToggleSimInfoPanel.SimInfoPanelType' = 7

    SIM_INFO_MOTIVE_PANEL = SimInfoPanelType.SIM_INFO_MOTIVE_PANEL
    SIM_INFO_SKILL_PANEL = SimInfoPanelType.SIM_INFO_SKILL_PANEL
    SIM_INFO_RELATIONSHIP_PANEL = SimInfoPanelType.SIM_INFO_RELATIONSHIP_PANEL
    SIM_INFO_CAREER_PANEL = SimInfoPanelType.SIM_INFO_CAREER_PANEL
    SIM_INFO_INVENTORY_PANEL = SimInfoPanelType.SIM_INFO_INVENTORY_PANEL
    SIM_INFO_ASPIRATION_PANEL = SimInfoPanelType.SIM_INFO_ASPIRATION_PANEL
    SIM_INFO_SUMMARY_PANEL = SimInfoPanelType.SIM_INFO_SUMMARY_PANEL
    SIM_INFO_CLUB_PANEL = SimInfoPanelType.SIM_INFO_CLUB_PANEL

    # __init__
    panel_type: 'ToggleSimInfoPanel.SimInfoPanelType'
    stay_open: 'bool'


class GhostUltimateStatisticProgress(Message):
    # __init__
    good_ultimate_progress: 'int'  # int32
    evil_ultimate_progress: 'int'  # int32


class SkillsAffectedByMasteryPerk(Message):
    # __init__
    mastery_perk_id: 'int'  # fixed uint64
    skill_names: 'RepeatedCompositeFieldContainer[LocalizedString]'


class ShowSmallBusinessConfigurator(Message):
    # __init__
    has_ticket_machine: 'bool'
    is_edit: 'bool'
    base_entry_fee: 'int'  # int32
    base_hourly_fee: 'int'  # int32
    is_current_zone_allowed_for_small_business: 'bool'
    is_home_zone_allowed_for_small_business: 'bool'


class FamilyRecipeCostModifier(Message):
    # __init__
    cost_modifier_size: 'float'  # float32


class CheatSheetDefinition(Message):
    # __init__
    controls: 'RepeatedCompositeFieldContainer[CheatSheetControl]'


class CheatSheetControl(Message):
    # __init__
    elements: 'RepeatedCompositeFieldContainer[CheatSheetElement]'
    description: 'LocalizedString'
    conditions: 'RepeatedCompositeFieldContainer[int]'  # int32


class CheatSheetElement(Message):
    # __init__
    element_type: 'int'  # int32
    keyframe: 'str'
    control: 'LocalizedString'
