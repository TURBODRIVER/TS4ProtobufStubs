from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer
from enum import IntEnum

from protocolbuffers.ResourceKey_pb2 import *
from protocolbuffers.Localization_pb2 import *
from protocolbuffers.UI_pb2 import *
from protocolbuffers.Consts_pb2 import *
from protocolbuffers.Exchange_pb2 import *
from protocolbuffers.Social_pb2 import *
from protocolbuffers.S4Common_pb2 import *
from protocolbuffers.Clubs_pb2 import *
from protocolbuffers.Lot_pb2 import *
from protocolbuffers.Commands_pb2 import *
from protocolbuffers.Commodities_pb2 import *


class UiDialogChoiceMessage(Message):
    class UiDialogChoiceUiRequest(IntEnum):
        NO_REQUEST: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 0
        SHOW_LESSONS: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 1
        SHOW_ACHIEVEMENTS: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 2
        SHOW_GALLERY_ITEM: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 3
        SHOW_FAMILY_INVENTORY: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 4
        SHOW_SKILL_PANEL: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 5
        SHOW_SUMMARY_PANEL: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 6
        SHOW_ASPIRATION_PANEL: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 7
        SHOW_ASPIRATION_UI: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 8
        SHOW_EVENT_UI: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 9
        SHOW_CAREER_PANEL: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 10
        SHOW_RELATIONSHIP_PANEL: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 11
        SHOW_SIM_INVENTORY: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 12
        SHOW_REWARD_STORE: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 13
        SHOW_MOTIVE_PANEL: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 14
        SHOW_STATS: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 15
        SHOW_COLLECTIBLES: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 16
        SHOW_CAREER_UI: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 17
        TRANSITION_TO_NEIGHBORHOOD_SAVE: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 18
        TRANSITION_TO_MAIN_MENU_NO_SAVE: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 19
        SHOW_SHARE_PLAYER_PROFILE: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 20
        SHOW_ASPIRATION_SELECTOR: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 21
        SHOW_SHARE_MY_LIBRARY: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 22
        SHOW_NOTEBOOK: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 23
        SEND_COMMAND: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 24
        CAREER_GO_TO_WORK: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 25
        CAREER_WORK_FROM_HOME: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 26
        CAREER_TAKE_PTO: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 27
        CAREER_CALL_IN_SICK: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 28
        SHOW_OCCULT_POWERS_PANEL: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 29
        SHOW_FAME_PERKS_PANEL: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 30
        SHOW_FACTION_REP_PANEL: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 31
        SEND_UI_MESSAGE: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 32
        PIVOTAL_MOMENT_ASK_LATER: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 33
        SHOW_GHOST_POWERS_PERKS_PANEL: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 34
        SHOW_SMALL_BUSINESS_PERKS_PANEL: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 35
        SHOW_SMALL_BUSINESS_PANEL: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 36
        SHOW_BUILD_BUY_WITH_FILTER: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 37
        SHOW_SMALL_BUSINESS_CONFIGURATOR: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest' = 38

    NO_REQUEST = UiDialogChoiceUiRequest.NO_REQUEST
    SHOW_LESSONS = UiDialogChoiceUiRequest.SHOW_LESSONS
    SHOW_ACHIEVEMENTS = UiDialogChoiceUiRequest.SHOW_ACHIEVEMENTS
    SHOW_GALLERY_ITEM = UiDialogChoiceUiRequest.SHOW_GALLERY_ITEM
    SHOW_FAMILY_INVENTORY = UiDialogChoiceUiRequest.SHOW_FAMILY_INVENTORY
    SHOW_SKILL_PANEL = UiDialogChoiceUiRequest.SHOW_SKILL_PANEL
    SHOW_SUMMARY_PANEL = UiDialogChoiceUiRequest.SHOW_SUMMARY_PANEL
    SHOW_ASPIRATION_PANEL = UiDialogChoiceUiRequest.SHOW_ASPIRATION_PANEL
    SHOW_ASPIRATION_UI = UiDialogChoiceUiRequest.SHOW_ASPIRATION_UI
    SHOW_EVENT_UI = UiDialogChoiceUiRequest.SHOW_EVENT_UI
    SHOW_CAREER_PANEL = UiDialogChoiceUiRequest.SHOW_CAREER_PANEL
    SHOW_RELATIONSHIP_PANEL = UiDialogChoiceUiRequest.SHOW_RELATIONSHIP_PANEL
    SHOW_SIM_INVENTORY = UiDialogChoiceUiRequest.SHOW_SIM_INVENTORY
    SHOW_REWARD_STORE = UiDialogChoiceUiRequest.SHOW_REWARD_STORE
    SHOW_MOTIVE_PANEL = UiDialogChoiceUiRequest.SHOW_MOTIVE_PANEL
    SHOW_STATS = UiDialogChoiceUiRequest.SHOW_STATS
    SHOW_COLLECTIBLES = UiDialogChoiceUiRequest.SHOW_COLLECTIBLES
    SHOW_CAREER_UI = UiDialogChoiceUiRequest.SHOW_CAREER_UI
    TRANSITION_TO_NEIGHBORHOOD_SAVE = UiDialogChoiceUiRequest.TRANSITION_TO_NEIGHBORHOOD_SAVE
    TRANSITION_TO_MAIN_MENU_NO_SAVE = UiDialogChoiceUiRequest.TRANSITION_TO_MAIN_MENU_NO_SAVE
    SHOW_SHARE_PLAYER_PROFILE = UiDialogChoiceUiRequest.SHOW_SHARE_PLAYER_PROFILE
    SHOW_ASPIRATION_SELECTOR = UiDialogChoiceUiRequest.SHOW_ASPIRATION_SELECTOR
    SHOW_SHARE_MY_LIBRARY = UiDialogChoiceUiRequest.SHOW_SHARE_MY_LIBRARY
    SHOW_NOTEBOOK = UiDialogChoiceUiRequest.SHOW_NOTEBOOK
    SEND_COMMAND = UiDialogChoiceUiRequest.SEND_COMMAND
    CAREER_GO_TO_WORK = UiDialogChoiceUiRequest.CAREER_GO_TO_WORK
    CAREER_WORK_FROM_HOME = UiDialogChoiceUiRequest.CAREER_WORK_FROM_HOME
    CAREER_TAKE_PTO = UiDialogChoiceUiRequest.CAREER_TAKE_PTO
    CAREER_CALL_IN_SICK = UiDialogChoiceUiRequest.CAREER_CALL_IN_SICK
    SHOW_OCCULT_POWERS_PANEL = UiDialogChoiceUiRequest.SHOW_OCCULT_POWERS_PANEL
    SHOW_FAME_PERKS_PANEL = UiDialogChoiceUiRequest.SHOW_FAME_PERKS_PANEL
    SHOW_FACTION_REP_PANEL = UiDialogChoiceUiRequest.SHOW_FACTION_REP_PANEL
    SEND_UI_MESSAGE = UiDialogChoiceUiRequest.SEND_UI_MESSAGE
    PIVOTAL_MOMENT_ASK_LATER = UiDialogChoiceUiRequest.PIVOTAL_MOMENT_ASK_LATER
    SHOW_GHOST_POWERS_PERKS_PANEL = UiDialogChoiceUiRequest.SHOW_GHOST_POWERS_PERKS_PANEL
    SHOW_SMALL_BUSINESS_PERKS_PANEL = UiDialogChoiceUiRequest.SHOW_SMALL_BUSINESS_PERKS_PANEL
    SHOW_SMALL_BUSINESS_PANEL = UiDialogChoiceUiRequest.SHOW_SMALL_BUSINESS_PANEL
    SHOW_BUILD_BUY_WITH_FILTER = UiDialogChoiceUiRequest.SHOW_BUILD_BUY_WITH_FILTER
    SHOW_SMALL_BUSINESS_CONFIGURATOR = UiDialogChoiceUiRequest.SHOW_SMALL_BUSINESS_CONFIGURATOR

    # __init__
    choice_id: 'int'  # uint32
    text: 'LocalizedString'
    ui_request: 'UiDialogChoiceMessage.UiDialogChoiceUiRequest'
    exchange_args: 'UiExchangeArgs'
    tutorial_args: 'UiTutorialArgs'
    command_with_args: 'UiCommandArgs'
    subtext: 'LocalizedString'
    disabled_text: 'LocalizedString'
    audio_event_name: 'str'
    ui_message_args: 'UiSendMessageArgs'
    tooltip_text: 'LocalizedString'
    button_icon: 'IconInfo'
    show_build_buy_args: 'UiShowBuildBuyArgs'


class UiShowBuildBuyArgs(Message):
    # __init__
    category_tag: 'int'  # uint32
    pack_id: 'int'  # uint32


class UiExchangeArgs(Message):
    # __init__
    item_id: 'int'  # uint64
    item_type: 'ExchangeItemTypes'
    is_favorite: 'bool'
    creator_id: 'int'  # uint64
    creator_name: 'str'
    item_data: 'TrayMetadata'
    feed_id: 'bytes'
    feed_type: 'SocialFeedItemType'
    quantity: 'int'  # uint32
    timestamp: 'int'  # uint64
    is_maxis_curated: 'bool'


class UiTutorialArgs(Message):
    # __init__
    tutorial_id: 'int'  # uint64


class UiCommandArgs(Message):
    # __init__
    command_name: 'str'
    command_remote_args: 'RemoteArgs'


class UiSendMessageArgs(Message):
    class Action(IntEnum):
        SEND_UI_MESSAGE: 'UiSendMessageArgs.Action' = 0
        SEND_GAME_MESSAGE: 'UiSendMessageArgs.Action' = 1
        CALL_UI_SERVICE: 'UiSendMessageArgs.Action' = 2
        CALL_GAME_SERVICE: 'UiSendMessageArgs.Action' = 3

    SEND_UI_MESSAGE = Action.SEND_UI_MESSAGE
    SEND_GAME_MESSAGE = Action.SEND_GAME_MESSAGE
    CALL_UI_SERVICE = Action.CALL_UI_SERVICE
    CALL_GAME_SERVICE = Action.CALL_GAME_SERVICE

    class Parameter():
        # __init__
        name: 'str'
        value: 'UiValue'

    # __init__
    action: 'UiSendMessageArgs.Action'
    name: 'str'
    parameters: 'RepeatedCompositeFieldContainer[UiSendMessageArgs.Parameter]'
    name: 'str'
    value: 'UiValue'


class UiDialogTextInputMessage(Message):
    # __init__
    text_input_name: 'str'
    default_text: 'LocalizedString'
    initial_value: 'LocalizedString'
    min_length: 'int'  # int32
    max_length: 'int'  # int32
    restricted_characters: 'LocalizedString'
    input_too_short_tooltip: 'LocalizedString'
    title: 'LocalizedString'
    max_value: 'int'  # int32
    input_invalid_max_tooltip: 'LocalizedString'
    min_value: 'int'  # int32
    input_invalid_min_tooltip: 'LocalizedString'
    check_profanity: 'bool'
    height: 'int'  # int32


class UiDialogMessage(Message):
    class Type(IntEnum):
        DEFAULT: 'UiDialogMessage.Type' = 1
        OBJECT_PICKER: 'UiDialogMessage.Type' = 2
        NOTIFICATION: 'UiDialogMessage.Type' = 3
        OK_CANCEL_ICONS: 'UiDialogMessage.Type' = 4
        INFO_SETTING: 'UiDialogMessage.Type' = 5
        ICONS_LABELS: 'UiDialogMessage.Type' = 6
        MULTI_PICKER: 'UiDialogMessage.Type' = 7
        INFO_IN_COLUMNS: 'UiDialogMessage.Type' = 8
        CUSTOMIZE_OBJECT_MULTI_PICKER: 'UiDialogMessage.Type' = 9
        REVEAL_SEQUENCE: 'UiDialogMessage.Type' = 10
        CRAFTING_JEWELRY: 'UiDialogMessage.Type' = 11
        DEATH_OPTIONS: 'UiDialogMessage.Type' = 12
        FAMILY_RECIPE: 'UiDialogMessage.Type' = 13

    DEFAULT = Type.DEFAULT
    OBJECT_PICKER = Type.OBJECT_PICKER
    NOTIFICATION = Type.NOTIFICATION
    OK_CANCEL_ICONS = Type.OK_CANCEL_ICONS
    INFO_SETTING = Type.INFO_SETTING
    ICONS_LABELS = Type.ICONS_LABELS
    MULTI_PICKER = Type.MULTI_PICKER
    INFO_IN_COLUMNS = Type.INFO_IN_COLUMNS
    CUSTOMIZE_OBJECT_MULTI_PICKER = Type.CUSTOMIZE_OBJECT_MULTI_PICKER
    REVEAL_SEQUENCE = Type.REVEAL_SEQUENCE
    CRAFTING_JEWELRY = Type.CRAFTING_JEWELRY
    DEATH_OPTIONS = Type.DEATH_OPTIONS
    FAMILY_RECIPE = Type.FAMILY_RECIPE

    class DialogStyle(IntEnum):
        DEFAULT_STYLE: 'UiDialogMessage.DialogStyle' = 0
        CHANCE_CARDS: 'UiDialogMessage.DialogStyle' = 1
        CELEBRATION: 'UiDialogMessage.DialogStyle' = 2
        VET_CHECK_IN: 'UiDialogMessage.DialogStyle' = 3
        LARGE_ICON: 'UiDialogMessage.DialogStyle' = 4
        TRAIT_REASSIGNMENT: 'UiDialogMessage.DialogStyle' = 5
        LIFESTYLE_BRAND: 'UiDialogMessage.DialogStyle' = 6
        LARGE_ICON_TEXT_HORIZONTAL: 'UiDialogMessage.DialogStyle' = 7
        LIFESTYLE_TRAITS: 'UiDialogMessage.DialogStyle' = 8
        LARGE_ICON_WIDE: 'UiDialogMessage.DialogStyle' = 9
        NPC_DISPLAY: 'UiDialogMessage.DialogStyle' = 10
        GUIDANCE_WARNING: 'UiDialogMessage.DialogStyle' = 11
        ICON_SWAP: 'UiDialogMessage.DialogStyle' = 12
        DYNAMIC_SIGN: 'UiDialogMessage.DialogStyle' = 13
        JEWELRY_CRAFTING: 'UiDialogMessage.DialogStyle' = 14
        GEMSTONE_CUTTING: 'UiDialogMessage.DialogStyle' = 15

    DEFAULT_STYLE = DialogStyle.DEFAULT_STYLE
    CHANCE_CARDS = DialogStyle.CHANCE_CARDS
    CELEBRATION = DialogStyle.CELEBRATION
    VET_CHECK_IN = DialogStyle.VET_CHECK_IN
    LARGE_ICON = DialogStyle.LARGE_ICON
    TRAIT_REASSIGNMENT = DialogStyle.TRAIT_REASSIGNMENT
    LIFESTYLE_BRAND = DialogStyle.LIFESTYLE_BRAND
    LARGE_ICON_TEXT_HORIZONTAL = DialogStyle.LARGE_ICON_TEXT_HORIZONTAL
    LIFESTYLE_TRAITS = DialogStyle.LIFESTYLE_TRAITS
    LARGE_ICON_WIDE = DialogStyle.LARGE_ICON_WIDE
    NPC_DISPLAY = DialogStyle.NPC_DISPLAY
    GUIDANCE_WARNING = DialogStyle.GUIDANCE_WARNING
    ICON_SWAP = DialogStyle.ICON_SWAP
    DYNAMIC_SIGN = DialogStyle.DYNAMIC_SIGN
    JEWELRY_CRAFTING = DialogStyle.JEWELRY_CRAFTING
    GEMSTONE_CUTTING = DialogStyle.GEMSTONE_CUTTING

    class DialogBGStyle(IntEnum):
        BG_DEFAULT_STYLE: 'UiDialogMessage.DialogBGStyle' = 0
        BG_CHANCE_CARDS: 'UiDialogMessage.DialogBGStyle' = 1
        BG_CELEBRATION: 'UiDialogMessage.DialogBGStyle' = 2
        BG_LIFESTYLE_BRAND: 'UiDialogMessage.DialogBGStyle' = 3
        BG_STYLE_CELEBRATION_LARGE: 'UiDialogMessage.DialogBGStyle' = 4
        BG_UNIVERSITY: 'UiDialogMessage.DialogBGStyle' = 5
        BG_DROIDS: 'UiDialogMessage.DialogBGStyle' = 6
        BG_VENDORS: 'UiDialogMessage.DialogBGStyle' = 7
        BG_CHANCE_CARDS_HAUNTED: 'UiDialogMessage.DialogBGStyle' = 8
        BG_MUSIC_FESTIVAL: 'UiDialogMessage.DialogBGStyle' = 9
        BG_DYNAMIC_IMAGE: 'UiDialogMessage.DialogBGStyle' = 10
        BG_MANI_PEDI: 'UiDialogMessage.DialogBGStyle' = 11
        BG_CAKE_TOPPER: 'UiDialogMessage.DialogBGStyle' = 12
        BG_TRENDI: 'UiDialogMessage.DialogBGStyle' = 13
        BG_GUIDANCE: 'UiDialogMessage.DialogBGStyle' = 14
        BG_FOOD_RECIPE_PICKER_ONLY: 'UiDialogMessage.DialogBGStyle' = 15
        BG_DEATH: 'UiDialogMessage.DialogBGStyle' = 16
        BG_TAROT: 'UiDialogMessage.DialogBGStyle' = 17

    BG_DEFAULT_STYLE = DialogBGStyle.BG_DEFAULT_STYLE
    BG_CHANCE_CARDS = DialogBGStyle.BG_CHANCE_CARDS
    BG_CELEBRATION = DialogBGStyle.BG_CELEBRATION
    BG_LIFESTYLE_BRAND = DialogBGStyle.BG_LIFESTYLE_BRAND
    BG_STYLE_CELEBRATION_LARGE = DialogBGStyle.BG_STYLE_CELEBRATION_LARGE
    BG_UNIVERSITY = DialogBGStyle.BG_UNIVERSITY
    BG_DROIDS = DialogBGStyle.BG_DROIDS
    BG_VENDORS = DialogBGStyle.BG_VENDORS
    BG_CHANCE_CARDS_HAUNTED = DialogBGStyle.BG_CHANCE_CARDS_HAUNTED
    BG_MUSIC_FESTIVAL = DialogBGStyle.BG_MUSIC_FESTIVAL
    BG_DYNAMIC_IMAGE = DialogBGStyle.BG_DYNAMIC_IMAGE
    BG_MANI_PEDI = DialogBGStyle.BG_MANI_PEDI
    BG_CAKE_TOPPER = DialogBGStyle.BG_CAKE_TOPPER
    BG_TRENDI = DialogBGStyle.BG_TRENDI
    BG_GUIDANCE = DialogBGStyle.BG_GUIDANCE
    BG_FOOD_RECIPE_PICKER_ONLY = DialogBGStyle.BG_FOOD_RECIPE_PICKER_ONLY
    BG_DEATH = DialogBGStyle.BG_DEATH
    BG_TAROT = DialogBGStyle.BG_TAROT

    # __init__
    dialog_id: 'int'  # uint64
    choices: 'RepeatedCompositeFieldContainer[UiDialogChoiceMessage]'
    text: 'LocalizedString'
    timeout_duration: 'float'  # float32
    owner_id: 'int'  # uint64
    target_id: 'int'  # uint64
    picker_data: 'UiDialogPicker'
    dialog_type: 'UiDialogMessage.Type'
    text_input: 'RepeatedCompositeFieldContainer[UiDialogTextInputMessage]'
    title: 'LocalizedString'
    dialog_options: 'int'  # uint32
    icon: 'ResourceKey'
    icon_info: 'IconInfo'
    secondary_icon_info: 'IconInfo'
    timestamp: 'int'  # uint64
    lot_title: 'LocalizedString'
    venue_icon: 'IconInfo'
    icon_infos: 'RepeatedCompositeFieldContainer[IconInfo]'
    dialog_style: 'int'  # uint32
    override_sim_icon_id: 'int'  # uint64
    multi_picker_data: 'UiDialogMultiPicker'
    dialog_bg_style: 'int'  # uint32
    is_special_dialog: 'bool'
    info_in_columns_data: 'UiDialogInfoInColumns'
    additional_texts: 'RepeatedCompositeFieldContainer[LocalizedString]'
    anonymous_target_sim: 'bool'
    background_audio_event: 'str'
    background_image: 'ResourceKey'
    footer_type: 'int'  # uint32
    subtitle: 'LocalizedString'
    mask_alert_icon: 'IconInfo'
    mask_alert_sim_name: 'LocalizedString'
    mask_header_icon: 'IconInfo'
    validation_command: 'str'


class UiDialogResponseMessage(Message):
    # __init__
    dialog_id: 'int'  # uint64
    choice_id: 'int'  # uint32


class UiDialogCloseRequest(Message):
    # __init__
    dialog_id: 'int'  # uint64


class UiDialogInfoInColumns(Message):
    # __init__
    column_headers: 'RepeatedCompositeFieldContainer[LocalizedString]'
    rows: 'RepeatedCompositeFieldContainer[UiDialogRowData]'


class UiDialogRowData(Message):
    # __init__
    column_info: 'RepeatedCompositeFieldContainer[IconInfo]'


class PickerColumn(Message):
    class ColumnType(IntEnum):
        TEXT: 'PickerColumn.ColumnType' = 1
        ICON: 'PickerColumn.ColumnType' = 2
        ICON_AND_TEXT: 'PickerColumn.ColumnType' = 3

    TEXT = ColumnType.TEXT
    ICON = ColumnType.ICON
    ICON_AND_TEXT = ColumnType.ICON_AND_TEXT

    # __init__
    type: 'PickerColumn.ColumnType'
    column_data_name: 'str'
    column_icon_name: 'str'
    label: 'LocalizedString'
    icon: 'ResourceKey'
    tooltip: 'LocalizedString'
    width: 'float'  # float32
    sortable: 'bool'


class PickerBaseRowData(Message):
    # __init__
    option_id: 'int'  # uint32
    is_enable: 'bool'
    name: 'LocalizedString'
    icon: 'ResourceKey'
    description: 'LocalizedString'
    icon_info: 'IconInfo'
    tooltip: 'LocalizedString'
    is_selected: 'bool'
    tag_list: 'RepeatedCompositeFieldContainer[int]'  # uint32
    second_tag_list: 'RepeatedCompositeFieldContainer[int]'  # uint32
    description_only_prepped: 'LocalizedString'
    description_both_fresh_prepped: 'LocalizedString'
    tooltip_only_prepped: 'LocalizedString'
    tooltip_both_fresh_prepped: 'LocalizedString'
    is_enable_fresh: 'bool'
    is_enable_prepped: 'bool'
    is_enable_both_fresh_prepped: 'bool'


class RecipeIngredientData(Message):
    # __init__
    ingredient_name: 'LocalizedString'
    in_inventory: 'bool'


class RecipeBucksCostData(Message):
    # __init__
    bucks_type: 'int'  # uint32
    amount: 'int'  # uint32


class RecipeGroupOverrideData(Message):
    # __init__
    skill_level: 'int'  # uint32
    name: 'LocalizedString'
    tooltip: 'LocalizedString'


class RecipePickerRowData(Message):
    # __init__
    base_data: 'PickerBaseRowData'
    price: 'int'  # uint32
    skill_level: 'int'  # uint32
    linked_option_ids: 'RepeatedCompositeFieldContainer[int]'  # uint32
    event_icon: 'ResourceKey'
    visible_as_subrow: 'bool'
    ingredients: 'RepeatedCompositeFieldContainer[RecipeIngredientData]'
    price_with_ingredients: 'int'  # uint32
    mtx_id: 'int'  # fixed uint64
    serving_display_name: 'LocalizedString'
    discounted_price: 'int'  # uint32
    is_discounted: 'bool'
    show_full_subrows: 'bool'
    bucks_costs: 'RepeatedCompositeFieldContainer[RecipeBucksCostData]'
    subrow_sort_id: 'int'  # int32
    locked_in_cas_icon_info: 'IconInfo'
    group_override: 'RecipeGroupOverrideData'
    ingredients_list: 'LocalizedString'
    enable_speed_up_background: 'bool'
    only_prepped_ingredients: 'RepeatedCompositeFieldContainer[RecipeIngredientData]'
    both_fresh_prepped_ingredients: 'RepeatedCompositeFieldContainer[RecipeIngredientData]'
    ingredients_list_only_prepped: 'LocalizedString'
    ingredients_list_both_fresh_prepped: 'LocalizedString'
    cooking_time_reduced: 'bool'
    price_with_only_prepped_ingredients: 'int'  # uint32
    price_with_both_fresh_prepped_ingredients: 'int'  # uint32
    food_restriction_ingredients: 'RepeatedCompositeFieldContainer[str]'
    recipe_id: 'int'  # uint64
    buff_id: 'int'  # uint64


class SimPickerRowData(Message):
    # __init__
    base_data: 'PickerBaseRowData'
    sim_id: 'int'  # uint64
    select_default: 'bool'
    failed_criteria: 'RepeatedCompositeFieldContainer[int]'  # uint32
    skills: 'RepeatedCompositeFieldContainer[SimPickerSkillRowData]'
    mood_id: 'int'  # fixed uint64
    sim_location: 'str'
    household_id: 'int'  # uint64


class SimPickerSkillRowData(Message):
    # __init__
    skill_id: 'int'  # fixed uint64
    current_points: 'int'  # uint32
    tooltip: 'LocalizedString'


class ObjectPickerRowData(Message):
    # __init__
    base_data: 'PickerBaseRowData'
    object_id: 'int'  # uint64
    def_id: 'int'  # uint64
    count: 'int'  # uint32
    rarity_text: 'LocalizedString'
    use_catalog_product_thumbnails: 'bool'
    second_rarity_text: 'LocalizedString'
    flair_icon: 'IconInfo'
    object_picker_style: 'int'  # uint32
    cost: 'int'  # uint32
    discounted_cost: 'int'  # uint32
    use_cas_catalog_product_thumbnails: 'bool'
    cas_catalog_gender: 'int'  # uint32
    slot_types: 'RepeatedCompositeFieldContainer[ResourceKey]'
    owner_sim_id: 'int'  # uint64
    is_new: 'bool'
    target_sim_id: 'int'  # uint64


class OutfitPickerRowData(Message):
    # __init__
    base_data: 'PickerBaseRowData'
    outfit_sim_id: 'int'  # fixed uint64
    outfit_category: 'int'  # uint32
    outfit_index: 'int'  # uint32


class PurchasePickerRowData(Message):
    # __init__
    base_data: 'PickerBaseRowData'
    def_id: 'int'  # uint64
    num_owned: 'int'  # uint32
    tag_list: 'RepeatedCompositeFieldContainer[int]'  # uint32
    num_available: 'int'  # int32
    object_id: 'int'  # fixed uint64
    custom_price: 'int'  # int32
    is_discounted: 'bool'
    prediscounted_price: 'int'  # int32
    fashion_trend: 'LocalizedString'


class LotPickerRowData(Message):
    # __init__
    base_data: 'PickerBaseRowData'
    lot_info_item: 'LotInfoItem'


class OddJobPickerRowData(Message):
    # __init__
    base_data: 'PickerBaseRowData'
    customer_id: 'int'  # uint64
    customer_description: 'LocalizedString'
    tip_title: 'LocalizedString'
    tip_icon: 'IconInfo'
    customer_thumbnail_override: 'IconInfo'
    customer_background: 'IconInfo'
    customer_name: 'LocalizedString'


class OddJobPickerData(Message):
    # __init__
    row_data: 'RepeatedCompositeFieldContainer[OddJobPickerRowData]'
    star_ranking: 'int'  # uint32
    picker_background: 'ResourceKey'
    hide_star_rating: 'bool'


class RecipePickerData(Message):
    # __init__
    column_list: 'RepeatedCompositeFieldContainer[PickerColumn]'
    row_data: 'RepeatedCompositeFieldContainer[RecipePickerRowData]'
    skill_id: 'int'  # uint64
    column_sort_list: 'RepeatedCompositeFieldContainer[int]'  # uint32
    display_ingredient_check: 'bool'
    display_funds: 'bool'
    display_prepped_ingredient_check: 'bool'


class SimPickerData(Message):
    # __init__
    row_data: 'RepeatedCompositeFieldContainer[SimPickerRowData]'
    should_show_names: 'bool'
    club_building_info: 'ClubBuildingInfo'
    rel_bit_collection_ids: 'RepeatedCompositeFieldContainer[int]'  # uint32
    column_count: 'int'  # uint32
    cell_type: 'int'  # uint32
    display_filter: 'bool'
    override_owner_relationships: 'RepeatedCompositeFieldContainer[RelationshipUpdate]'


class ObjectPickerData(Message):
    # __init__
    row_data: 'RepeatedCompositeFieldContainer[ObjectPickerRowData]'
    num_columns: 'int'  # uint32


class OutfitPickerData(Message):
    class ObjectPickerThumbnailType(IntEnum):
        SIM_INFO: 'OutfitPickerData.ObjectPickerThumbnailType' = 1
        MANNEQUIN: 'OutfitPickerData.ObjectPickerThumbnailType' = 2

    SIM_INFO = ObjectPickerThumbnailType.SIM_INFO
    MANNEQUIN = ObjectPickerThumbnailType.MANNEQUIN

    # __init__
    row_data: 'RepeatedCompositeFieldContainer[OutfitPickerRowData]'
    thumbnail_type: 'OutfitPickerData.ObjectPickerThumbnailType'
    outfit_category_filters: 'RepeatedCompositeFieldContainer[int]'  # uint32


class PurchasePickerData(Message):
    # __init__
    row_data: 'RepeatedCompositeFieldContainer[PurchasePickerRowData]'
    object_id: 'int'  # fixed uint64
    show_description: 'bool'
    categories: 'RepeatedCompositeFieldContainer[PurchasePickerCategory]'
    inventory_object_id: 'int'  # fixed uint64
    show_cost: 'bool'
    max_selectable_in_row: 'int'  # uint32
    show_description_tooltip: 'bool'
    use_dialog_pick_response: 'bool'
    right_custom_text: 'LocalizedString'
    sub_total_text: 'LocalizedString'
    sub_total_cost: 'int'  # uint32
    delivery_method: 'int'  # uint32
    max_selectable_rows: 'int'  # uint32


class PurchasePickerCategory(Message):
    # __init__
    tag_type: 'int'  # uint32
    icon_info: 'IconInfo'
    description: 'LocalizedString'
    disabled_tooltip: 'LocalizedString'


class LotPickerData(Message):
    # __init__
    row_data: 'RepeatedCompositeFieldContainer[LotPickerRowData]'


class PickerFilterData(Message):
    # __init__
    tag_type: 'int'  # uint32
    icon_info: 'IconInfo'
    description: 'LocalizedString'


class DropdownPickerData(Message):
    # __init__
    default_item: 'UiDialogDropdownItem'
    items: 'RepeatedCompositeFieldContainer[UiDialogDropdownItem]'
    invalid_tooltip: 'LocalizedString'
    selected_item_id: 'int'  # uint32
    options: 'int'  # uint32


class UiDialogDropdownItem(Message):
    # __init__
    text: 'LocalizedString'
    icon_info: 'IconInfo'
    id: 'int'  # uint32


class UiDialogPicker(Message):
    class ObjectPickerType(IntEnum):
        RECIPE: 'UiDialogPicker.ObjectPickerType' = 1
        INTERACTION: 'UiDialogPicker.ObjectPickerType' = 2
        SIM: 'UiDialogPicker.ObjectPickerType' = 3
        OBJECT: 'UiDialogPicker.ObjectPickerType' = 4
        PIE_MENU: 'UiDialogPicker.ObjectPickerType' = 5
        CAREER: 'UiDialogPicker.ObjectPickerType' = 6
        OUTFIT: 'UiDialogPicker.ObjectPickerType' = 7
        PURCHASE: 'UiDialogPicker.ObjectPickerType' = 8
        LOT: 'UiDialogPicker.ObjectPickerType' = 9
        SIM_CLUB: 'UiDialogPicker.ObjectPickerType' = 10
        ITEM: 'UiDialogPicker.ObjectPickerType' = 11
        OBJECT_LARGE: 'UiDialogPicker.ObjectPickerType' = 12
        DROPDOWN: 'UiDialogPicker.ObjectPickerType' = 13
        OBJECT_SQUARE: 'UiDialogPicker.ObjectPickerType' = 14
        ODD_JOBS: 'UiDialogPicker.ObjectPickerType' = 15
        MISSIONS: 'UiDialogPicker.ObjectPickerType' = 16
        LARGE_TEXT_FLAIR: 'UiDialogPicker.ObjectPickerType' = 17
        PHOTO: 'UiDialogPicker.ObjectPickerType' = 18
        SELL: 'UiDialogPicker.ObjectPickerType' = 19
        QUESTS: 'UiDialogPicker.ObjectPickerType' = 20
        OBJECT_TEXT: 'UiDialogPicker.ObjectPickerType' = 21
        OBJECT_TEXT_ADD: 'UiDialogPicker.ObjectPickerType' = 22
        FASHION_PURCHASE: 'UiDialogPicker.ObjectPickerType' = 23
        RELATIONSHIP: 'UiDialogPicker.ObjectPickerType' = 24
        OBJECT_EXPANDED_INFO: 'UiDialogPicker.ObjectPickerType' = 25
        OBJECT_CAS_ICON: 'UiDialogPicker.ObjectPickerType' = 26

    RECIPE = ObjectPickerType.RECIPE
    INTERACTION = ObjectPickerType.INTERACTION
    SIM = ObjectPickerType.SIM
    OBJECT = ObjectPickerType.OBJECT
    PIE_MENU = ObjectPickerType.PIE_MENU
    CAREER = ObjectPickerType.CAREER
    OUTFIT = ObjectPickerType.OUTFIT
    PURCHASE = ObjectPickerType.PURCHASE
    LOT = ObjectPickerType.LOT
    SIM_CLUB = ObjectPickerType.SIM_CLUB
    ITEM = ObjectPickerType.ITEM
    OBJECT_LARGE = ObjectPickerType.OBJECT_LARGE
    DROPDOWN = ObjectPickerType.DROPDOWN
    OBJECT_SQUARE = ObjectPickerType.OBJECT_SQUARE
    ODD_JOBS = ObjectPickerType.ODD_JOBS
    MISSIONS = ObjectPickerType.MISSIONS
    LARGE_TEXT_FLAIR = ObjectPickerType.LARGE_TEXT_FLAIR
    PHOTO = ObjectPickerType.PHOTO
    SELL = ObjectPickerType.SELL
    QUESTS = ObjectPickerType.QUESTS
    OBJECT_TEXT = ObjectPickerType.OBJECT_TEXT
    OBJECT_TEXT_ADD = ObjectPickerType.OBJECT_TEXT_ADD
    FASHION_PURCHASE = ObjectPickerType.FASHION_PURCHASE
    RELATIONSHIP = ObjectPickerType.RELATIONSHIP
    OBJECT_EXPANDED_INFO = ObjectPickerType.OBJECT_EXPANDED_INFO
    OBJECT_CAS_ICON = ObjectPickerType.OBJECT_CAS_ICON

    class DescriptionDisplay(IntEnum):
        DEFAULT: 'UiDialogPicker.DescriptionDisplay' = 1
        NO_DESCRIPTION: 'UiDialogPicker.DescriptionDisplay' = 2
        FULL_DESCRIPTION: 'UiDialogPicker.DescriptionDisplay' = 3

    DEFAULT = DescriptionDisplay.DEFAULT
    NO_DESCRIPTION = DescriptionDisplay.NO_DESCRIPTION
    FULL_DESCRIPTION = DescriptionDisplay.FULL_DESCRIPTION

    # __init__
    type: 'UiDialogPicker.ObjectPickerType'
    title: 'LocalizedString'
    owner_sim_id: 'int'  # uint64
    target_sim_id: 'int'  # uint64
    recipe_picker_data: 'RecipePickerData'
    sim_picker_data: 'SimPickerData'
    object_picker_data: 'ObjectPickerData'
    outfit_picker_data: 'OutfitPickerData'
    max_selectable: 'int'  # uint32
    shop_picker_data: 'PurchasePickerData'
    lot_picker_data: 'LotPickerData'
    is_sortable: 'bool'
    hide_row_description: 'bool'
    use_dropdown_filter: 'bool'
    row_picker_data: 'RepeatedCompositeFieldContainer[PickerBaseRowData]'
    min_selectable: 'int'  # uint32
    filter_data: 'RepeatedCompositeFieldContainer[PickerFilterDataList]'
    dropdown_picker_data: 'DropdownPickerData'
    description_display: 'UiDialogPicker.DescriptionDisplay'
    odd_job_picker_data: 'OddJobPickerData'
    control_id_type: 'int'  # uint32
    current_selected: 'int'  # uint32
    counter_label_text: 'LocalizedString'
    help_tooltip: 'LocalizedString'
    bubble_up_selected: 'bool'
    subtitle: 'LocalizedString'
    force_done_button: 'bool'
    disable_non_selectable_items: 'bool'
    slot_types_max_selectable: 'RepeatedCompositeFieldContainer[SlotTypesMaxSelectable]'
    max_selectable_subtitle: 'LocalizedString'
    tooltip_text_cancel: 'LocalizedString'
    tooltip_text_ok: 'LocalizedString'


class SlotTypesMaxSelectable(Message):
    # __init__
    slot_type_key: 'ResourceKey'
    max_selectable: 'int'  # uint32


class PickerFilterDataList(Message):
    # __init__
    filter_data: 'RepeatedCompositeFieldContainer[PickerFilterData]'
    use_dropdown_filter: 'int'  # uint32
    add_all_category: 'bool'
    sort_filter_categories: 'bool'
    remove_empty_filter_categories: 'bool'
    use_sim_inventory_filter_categories: 'bool'


class UiDialogMultiPicker(Message):
    class MultiPickerStyle(IntEnum):
        DEFAULT: 'UiDialogMultiPicker.MultiPickerStyle' = 0
        PHOTOPAIR_ORGANIZE_DELETE: 'UiDialogMultiPicker.MultiPickerStyle' = 1
        PHOTOPAIR_SELECT: 'UiDialogMultiPicker.MultiPickerStyle' = 2

    DEFAULT = MultiPickerStyle.DEFAULT
    PHOTOPAIR_ORGANIZE_DELETE = MultiPickerStyle.PHOTOPAIR_ORGANIZE_DELETE
    PHOTOPAIR_SELECT = MultiPickerStyle.PHOTOPAIR_SELECT

    # __init__
    multi_picker_items: 'RepeatedCompositeFieldContainer[UiDialogMultiPickerItem]'
    multi_picker_style: 'UiDialogMultiPicker.MultiPickerStyle'
    multi_picker_selection_equality: 'bool'
    multi_selection_inequality_tooltip: 'LocalizedString'
    multipicker_filter_type: 'int'  # uint32
    multi_picker_items_height: 'float'  # float32
    combined_limits_datas: 'RepeatedCompositeFieldContainer[UIDialogMultiPickerCombinedLimitsData]'


class UIDialogMultiPickerCombinedLimitsData(Message):
    # __init__
    picker_ids: 'RepeatedCompositeFieldContainer[int]'  # uint32
    max_selectable: 'int'  # uint32
    min_selectable: 'int'  # uint32
    max_selectable_tooltip: 'LocalizedString'
    min_selectable_tooltip: 'LocalizedString'


class UiDialogMultiPickerItem(Message):
    # __init__
    picker_data: 'UiDialogPicker'
    picker_id: 'int'  # uint32
    disabled_tooltip: 'LocalizedString'
    max_selected_tooltip: 'LocalizedString'
    show_header: 'bool'


class UiPhoneRing(Message):
    class PhoneRingType(IntEnum):
        NONE: 'UiPhoneRing.PhoneRingType' = 0
        BUZZ: 'UiPhoneRing.PhoneRingType' = 1
        RING: 'UiPhoneRing.PhoneRingType' = 2
        ALARM: 'UiPhoneRing.PhoneRingType' = 3
        PIVOTAL_MOMENT: 'UiPhoneRing.PhoneRingType' = 4

    NONE = PhoneRingType.NONE
    BUZZ = PhoneRingType.BUZZ
    RING = PhoneRingType.RING
    ALARM = PhoneRingType.ALARM
    PIVOTAL_MOMENT = PhoneRingType.PIVOTAL_MOMENT

    # __init__
    phone_ring_type: 'UiPhoneRing.PhoneRingType'
    dialog: 'UiDialogMessage'
    caller_id: 'int'  # uint64


class UiCalendarMessage(Message):
    # __init__
    event_type: 'int'  # uint32
    calendar_icon: 'IconInfo'
    start_time: 'int'  # uint64
    lot_id: 'int'  # uint64
    description: 'LocalizedString'
    sim_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    zone_id: 'int'  # uint64
    tradition_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    show_go_to_button: 'bool'
    drama_node_guid: 'int'  # uint64


class UiDialogNotification(Message):
    class NotificationExpandBehavior(IntEnum):
        USER_SETTING: 'UiDialogNotification.NotificationExpandBehavior' = 0
        FORCE_EXPAND: 'UiDialogNotification.NotificationExpandBehavior' = 1

    USER_SETTING = NotificationExpandBehavior.USER_SETTING
    FORCE_EXPAND = NotificationExpandBehavior.FORCE_EXPAND

    class NotificationCriticality(IntEnum):
        DEFAULT: 'UiDialogNotification.NotificationCriticality' = 0
        URGENT: 'UiDialogNotification.NotificationCriticality' = 1

    DEFAULT = NotificationCriticality.DEFAULT
    URGENT = NotificationCriticality.URGENT

    class NotificationLevel(IntEnum):
        PLAYER: 'UiDialogNotification.NotificationLevel' = 0
        SIM: 'UiDialogNotification.NotificationLevel' = 1
        GALLERY: 'UiDialogNotification.NotificationLevel' = 2

    PLAYER = NotificationLevel.PLAYER
    SIM = NotificationLevel.SIM
    GALLERY = NotificationLevel.GALLERY

    class NotificationVisualType(IntEnum):
        INFORMATION: 'UiDialogNotification.NotificationVisualType' = 0
        SPEECH: 'UiDialogNotification.NotificationVisualType' = 1
        SPECIAL_MOMENT: 'UiDialogNotification.NotificationVisualType' = 2

    INFORMATION = NotificationVisualType.INFORMATION
    SPEECH = NotificationVisualType.SPEECH
    SPECIAL_MOMENT = NotificationVisualType.SPECIAL_MOMENT

    class NotificationAutoDeleteReason(IntEnum):
        NO_REASON: 'UiDialogNotification.NotificationAutoDeleteReason' = 0
        LEAVE_LIVE_MODE: 'UiDialogNotification.NotificationAutoDeleteReason' = 1

    NO_REASON = NotificationAutoDeleteReason.NO_REASON
    LEAVE_LIVE_MODE = NotificationAutoDeleteReason.LEAVE_LIVE_MODE

    dialog: 'UiDialogNotification'

    # __init__
    expand_behavior: 'UiDialogNotification.NotificationExpandBehavior'
    criticality: 'UiDialogNotification.NotificationCriticality'
    information_level: 'UiDialogNotification.NotificationLevel'
    visual_type: 'UiDialogNotification.NotificationVisualType'
    primary_icon_response: 'UiDialogChoiceMessage'
    secondary_icon_response: 'UiDialogChoiceMessage'
    save_uid: 'int'  # uint64
    does_persist: 'bool'
    career_args: 'UiCareerNotificationArgs'
    auto_delete_reason: 'UiDialogNotification.NotificationAutoDeleteReason'


class UiCareerNotificationArgs(Message):
    # __init__
    career_uid: 'int'  # uint64
    career_level: 'int'  # uint32
    career_track: 'int'  # uint64
    user_career_level: 'int'  # uint32
    sim_id: 'int'  # uint64
    paid_time_off_available: 'int'  # uint32
    work_schedule: 'Schedule'
    paid_time_off_disabled: 'bool'
    schedule_shift_type: 'int'  # uint32
    pay: 'int'  # uint32


class SimPersonalityAssignmentDialog(Message):
    # __init__
    sim_id: 'int'  # uint64
    dialog: 'UiDialogMessage'
    secondary_title: 'LocalizedString'
    age_description: 'LocalizedString'
    naming_title_text: 'LocalizedString'
    aspirations_and_trait_assignment_text: 'LocalizedString'
    available_trait_slots: 'int'  # uint64
    current_personality_trait_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    available_personality_trait_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    available_aspiration_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    is_female: 'bool'
    current_aspiration_id: 'int'  # uint64
    current_aspiration_trait_id: 'int'  # uint64
    replace_trait_id: 'int'  # uint64
    reward_trait_id: 'int'  # uint64
    current_skill_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    previous_skill_levels: 'RepeatedCompositeFieldContainer[int]'  # uint32
    previous_skill_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    unlocked_trait_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    age_up_reward_trait_text: 'LocalizedString'


class RetailSummaryDialog(Message):
    # __init__
    name: 'LocalizedString'
    subtitle: 'LocalizedString'
    icon: 'IconInfo'
    hours_open: 'int'  # uint32
    line_items: 'RepeatedCompositeFieldContainer[RetailSummaryLineItem]'
    total_amount: 'int'  # int32


class RetailSummaryLineItem(Message):
    # __init__
    name: 'LocalizedString'
    item_type: 'LocalizedString'
    value: 'int'  # int32


class RetailManageEmployeesDialog(Message):
    # __init__
    hiring_sim_id: 'int'  # fixed uint64
    employees: 'RepeatedCompositeFieldContainer[RetailEmployeeRowData]'
    available_sims: 'RepeatedCompositeFieldContainer[RetailEmployeeRowData]'
    open_slots: 'int'  # uint32
    locked_slots: 'int'  # uint32


class RetailEmployeeRowData(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    satisfaction_string: 'LocalizedString'
    pay: 'int'  # uint32
    skill_data: 'RepeatedCompositeFieldContainer[RetailEmployeeSkillData]'
    current_career_level: 'int'  # uint32
    max_career_level: 'int'  # uint32


class RetailEmployeeSkillData(Message):
    # __init__
    skill_id: 'int'  # fixed uint64
    curr_points: 'int'  # uint32


class GameplayPerkList(Message):
    # __init__
    bucks_type: 'int'  # uint32
    perk_list: 'RepeatedCompositeFieldContainer[GameplayPerk]'


class GameplayPerk(Message):
    class PerkType(IntEnum):
        DEFAULT: 'GameplayPerk.PerkType' = 0
        OBJECT: 'GameplayPerk.PerkType' = 1
        CASPART: 'GameplayPerk.PerkType' = 2

    DEFAULT = PerkType.DEFAULT
    OBJECT = PerkType.OBJECT
    CASPART = PerkType.CASPART

    # __init__
    id: 'int'  # fixed uint64
    type: 'GameplayPerk.PerkType'
    display_name: 'LocalizedString'
    description: 'LocalizedString'
    disabled_tooltip: 'LocalizedString'
    icon: 'IconInfo'
    cost: 'int'  # uint32
    affordable: 'bool'
    purchased: 'bool'
    category: 'int'  # uint64
    lock_on_purchase: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    locked: 'bool'
    next_perk_id: 'int'  # fixed uint64
    conflicting_perks: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    required_perks: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    recently_locked: 'bool'
    unlock_timestamp: 'int'  # uint64
    locked_from_tests: 'bool'
    ui_display_flags: 'int'  # uint32


class BalanceTransferDialog(Message):
    # __init__
    transfer_amount: 'int'  # uint32
    lot_data: 'RepeatedCompositeFieldContainer[BalanceTransferLotData]'


class BalanceTransferLotData(Message):
    # __init__
    lot_name: 'LocalizedString'
    zone_id: 'int'  # uint64
    balance: 'int'  # int32


class MultiPickerResponse(Message):
    # __init__
    picker_responses: 'RepeatedCompositeFieldContainer[MultiPickerResponseItem]'
    text_input: 'str'


class MultiPickerResponseItem(Message):
    # __init__
    choices: 'RepeatedCompositeFieldContainer[int]'  # uint64
    picker_id: 'int'  # uint32
    control_ids: 'RepeatedCompositeFieldContainer[int]'  # uint32


class PickerValidationResponse(Message):
    # __init__
    is_valid: 'bool'
