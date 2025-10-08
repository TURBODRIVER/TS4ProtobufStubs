from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer
from enum import IntEnum

from protocolbuffers.Consts_pb2 import *
from protocolbuffers.SimObjectAttributes_pb2 import *
from protocolbuffers.ResourceKey_pb2 import *
from protocolbuffers.Venue_pb2 import *
from protocolbuffers.S4Common_pb2 import *


class UnitTraitData(Message):
    # __init__
    unitId: 'int'  # uint32
    traits: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class TrayBlueprintMetadata(Message):
    # __init__
    venue_type: 'int'  # uint64
    size_x: 'int'  # uint32
    size_z: 'int'  # uint32
    price_level: 'int'  # uint32
    price_value: 'int'  # uint32
    num_bedrooms: 'int'  # uint32
    num_bathrooms: 'int'  # uint32
    architecture_value: 'int'  # uint32
    num_thumbnails: 'int'  # uint32
    front_side: 'int'  # uint32
    venue_type_stringkey: 'int'  # uint32
    ground_floor_index: 'int'  # uint32
    optional_rule_satisfied_stringkeys: 'RepeatedCompositeFieldContainer[int]'  # uint32
    lot_traits: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    building_type: 'int'  # uint32
    lot_template_id: 'int'  # uint64
    university_housing_configuration: 'UniversityHousingConfiguration'
    tile_count: 'int'  # uint32
    unit_count: 'int'  # uint32
    unitTraits: 'RepeatedCompositeFieldContainer[UnitTraitData]'
    dynamic_areas: 'RepeatedCompositeFieldContainer[int]'  # uint32


class TrayRoomBlueprintMetadata(Message):
    # __init__
    room_type: 'int'  # uint32
    size_x: 'int'  # uint32
    size_z: 'int'  # uint32
    price_value: 'int'  # uint32
    height: 'int'  # uint32
    price_level: 'int'  # uint32
    room_type_stringkey: 'int'  # uint32


class WebTraitTracker(Message):
    # __init__
    name_hash: 'int'  # uint32
    name_string: 'str'
    description_hash: 'int'  # uint32
    description_string: 'str'
    icon_key: 'ResourceKey'
    trait_type: 'int'  # int64
    description_origin_hash: 'int'  # uint32
    description_origin_string: 'str'
    cas_selected_icon_key: 'ResourceKey'


class WebAspirationInfo(Message):
    # __init__
    display_hash: 'int'  # uint32
    display_string: 'str'
    description_hash: 'int'  # uint32
    description_string: 'str'
    icon: 'ResourceKey'
    icon_high_res: 'ResourceKey'
    primary_trait: 'WebTraitTracker'


class TraySimMetadata(Message):
    # __init__
    trait_tracker: 'PersistableTraitTracker'
    genealogy_tracker: 'PersistableGenealogyTracker'
    first_name: 'str'
    last_name: 'str'
    id: 'int'  # uint64
    gender: 'int'  # uint32
    aspirationId: 'int'  # uint64
    sim_relationships: 'RepeatedCompositeFieldContainer[FamilyRelation]'
    age: 'int'  # uint32
    web_trait_tracker: 'RepeatedCompositeFieldContainer[WebTraitTracker]'
    web_aspiration_info: 'WebAspirationInfo'
    species: 'int'  # uint32
    is_custom_gender: 'bool'
    occult_types: 'int'  # uint32
    breed_name: 'str'
    breed_name_key: 'int'  # uint32
    fame: 'TrayRankedStatMetadata'
    like_trait_tracker: 'PersistableTraitTracker'
    web_like_trait_tracker: 'RepeatedCompositeFieldContainer[WebTraitTracker]'
    dislike_trait_tracker: 'PersistableTraitTracker'
    web_dislike_trait_tracker: 'RepeatedCompositeFieldContainer[WebTraitTracker]'
    sim_tropes: 'RepeatedCompositeFieldContainer[RelationshipTrope]'
    custom_pronoun: 'SimPronounList'
    death_trait: 'int'  # uint64


class TrayRankedStatMetadata(Message):
    # __init__
    id: 'int'  # uint64
    value: 'float'  # float32


class TrayHouseholdMetadata(Message):
    # __init__
    family_size: 'int'  # uint32
    sim_data: 'RepeatedCompositeFieldContainer[TraySimMetadata]'
    pending_babies: 'int'  # uint32


class TrayMetadata(Message):
    class TrayMetadataVersion(IntEnum):
        v000: 'TrayMetadata.TrayMetadataVersion' = 0
        currentVersion: 'TrayMetadata.TrayMetadataVersion' = 11800

    v000 = TrayMetadataVersion.v000
    currentVersion = TrayMetadataVersion.currentVersion

    class ExtraThumbnailInfo():
        # __init__
        thumbnail_info: 'RepeatedCompositeFieldContainer[int]'  # uint32

    class SpecificData():
        # __init__
        bp_metadata: 'TrayBlueprintMetadata'
        hh_metadata: 'TrayHouseholdMetadata'
        ro_metadata: 'TrayRoomBlueprintMetadata'
        part_metadata: 'TrayPartMetadata'
        is_hidden: 'bool'
        is_downloadtemp: 'bool'
        is_modded_content: 'bool'
        xti: 'TrayMetadata.ExtraThumbnailInfo'
        description_hashtags: 'str'
        language_id: 'int'  # uint64
        sku_id: 'int'  # uint64
        is_maxis_content: 'bool'
        payloadsize: 'int'  # uint32
        was_reported: 'bool'
        was_reviewed_and_cleared: 'bool'
        is_image_modded_content: 'bool'
        sd_creator_platform: 'ExchangeItemPlatform'
        sd_modifier_platform: 'ExchangeItemPlatform'
        sd_creator_platform_persona_id: 'int'  # uint64
        sd_modifier_platform_persona_id: 'int'  # uint64
        is_cg_item: 'bool'
        is_cg_interested: 'bool'
        cg_name: 'str'
        sku2_id: 'int'  # uint64
        cds_patch_base_changelists: 'RepeatedCompositeFieldContainer[int]'  # uint32
        cds_content_patch_mounted: 'bool'
        sku_bits: 'RepeatedCompositeFieldContainer[int]'  # uint32
        version_OBSOLETE: 'TrayMetadata.TrayMetadataVersion'
        version: 'int'  # uint32

    # __init__
    id: 'int'  # uint64
    type: 'ExchangeItemTypes'
    remote_id: 'bytes'
    name: 'str'
    description: 'str'
    creator_id: 'int'  # uint64
    creator_name: 'str'
    favorites: 'int'  # uint64
    downloads: 'int'  # uint64
    metadata: 'TrayMetadata.SpecificData'
    item_timestamp: 'int'  # uint64
    mtx_ids: 'RepeatedCompositeFieldContainer[int]'  # uint64
    creator_uuid: 'bytes'
    modifier_id: 'int'  # uint64
    modifier_name: 'str'
    meta_info: 'RepeatedCompositeFieldContainer[int]'  # uint32
    verify_code: 'int'  # int32
    custom_image_count: 'int'  # uint32
    mannequin_count: 'int'  # uint32
    indexed_counter: 'int'  # uint64
    creator_platform: 'ExchangeItemPlatform'
    modifier_platform: 'ExchangeItemPlatform'
    creator_platform_id: 'int'  # uint64
    creator_platform_name: 'str'
    modifier_platform_id: 'int'  # uint64
    modifier_platform_name: 'str'
    image_uri_type: 'BaseUri.BaseUriType'
    shared_timestamp: 'int'  # uint64
    liked: 'bool'
    thumbnail_info: 'RepeatedCompositeFieldContainer[int]'  # uint32
    bp_metadata: 'TrayBlueprintMetadata'
    hh_metadata: 'TrayHouseholdMetadata'
    ro_metadata: 'TrayRoomBlueprintMetadata'
    part_metadata: 'TrayPartMetadata'
    is_hidden: 'bool'
    is_downloadtemp: 'bool'
    is_modded_content: 'bool'
    xti: 'TrayMetadata.ExtraThumbnailInfo'
    description_hashtags: 'str'
    language_id: 'int'  # uint64
    sku_id: 'int'  # uint64
    is_maxis_content: 'bool'
    payloadsize: 'int'  # uint32
    was_reported: 'bool'
    was_reviewed_and_cleared: 'bool'
    is_image_modded_content: 'bool'
    sd_creator_platform: 'ExchangeItemPlatform'
    sd_modifier_platform: 'ExchangeItemPlatform'
    sd_creator_platform_persona_id: 'int'  # uint64
    sd_modifier_platform_persona_id: 'int'  # uint64
    is_cg_item: 'bool'
    is_cg_interested: 'bool'
    cg_name: 'str'
    sku2_id: 'int'  # uint64
    cds_patch_base_changelists: 'RepeatedCompositeFieldContainer[int]'  # uint32
    cds_content_patch_mounted: 'bool'
    sku_bits: 'RepeatedCompositeFieldContainer[int]'  # uint32
    version_OBSOLETE: 'TrayMetadata.TrayMetadataVersion'
    version: 'int'  # uint32


class ExchangeItemPrerequisites(Message):
    # __init__
    item: 'RepeatedCompositeFieldContainer[int]'  # uint64


class TrayPartMetadata(Message):
    # __init__
    body_type: 'int'  # uint32
    num_thumbnails: 'int'  # uint32
    part_Id: 'RepeatedCompositeFieldContainer[int]'  # uint64


class ExchangeEnvelope(Message):
    class ThumbnailMessage():
        # __init__
        thumbnail_info: 'RepeatedCompositeFieldContainer[int]'  # uint32
        thumbnail_data: 'RepeatedCompositeFieldContainer[bytes]'

    # __init__
    uuid: 'bytes'
    owner: 'str'
    product_ids: 'ExchangeItemPrerequisites'
    small_thumbnail: 'bytes'
    large_thumbnail: 'bytes'
    payload: 'bytes'
    metadata: 'TrayMetadata'
    thumbnail_message: 'ExchangeEnvelope.ThumbnailMessage'
    thumbnail_info: 'RepeatedCompositeFieldContainer[int]'  # uint32
    thumbnail_data: 'RepeatedCompositeFieldContainer[bytes]'


class ExchangeSocialEnvelope(Message):
    # __init__
    nucleusid: 'int'  # uint64
    owner: 'str'
    metadata: 'TrayMetadata'
    quantity: 'int'  # uint64
    feedid: 'bytes'


class ExchangeListResults(Message):
    # __init__
    results: 'RepeatedCompositeFieldContainer[ExchangeEnvelope]'
    nextToken: 'str'


class ExchangeWebserverUri(Message):
    # __init__
    baseuri: 'str'
    foldermodulos: 'int'  # uint32
    baseuris: 'RepeatedCompositeFieldContainer[BaseUri]'


class BaseUri(Message):
    class BaseUriType(IntEnum):
        UNKNOWN: 'BaseUri.BaseUriType' = 0
        LEGACY_CDN: 'BaseUri.BaseUriType' = 1
        GOOGLE_CLOUD_STORAGE: 'BaseUri.BaseUriType' = 2

    UNKNOWN = BaseUriType.UNKNOWN
    LEGACY_CDN = BaseUriType.LEGACY_CDN
    GOOGLE_CLOUD_STORAGE = BaseUriType.GOOGLE_CLOUD_STORAGE

    # __init__
    type: 'BaseUri.BaseUriType'
    baseuri: 'str'


class ExchangeSearchRequest(Message):
    # __init__
    match_term: 'str'
    type: 'ExchangeItemTypes'
    last_uuid: 'bytes'
    max_results: 'int'  # uint32


class ExchangeFetchByStatRequest(Message):
    class ExchangeFetchFromValue():
        # __init__
        counter_value: 'int'  # uint32
        uuid: 'bytes'

    # __init__
    value_fetch: 'ExchangeFetchByStatRequest.ExchangeFetchFromValue'
    type: 'ExchangeItemTypes'
    max_results: 'int'  # uint32
    counter_value: 'int'  # uint32
    uuid: 'bytes'


class ExchangeFetchKeywordRequest(Message):
    # __init__
    keyword: 'str'
    type: 'ExchangeItemTypes'
    uuid: 'bytes'
    max_results: 'int'  # uint32


class ExchangeFetchRecentRequest(Message):
    # __init__
    uuid: 'bytes'
    type: 'ExchangeItemTypes'
    max_results: 'int'  # uint32


class ExchangeGetUpdatedStats(Message):
    # __init__
    uuids: 'RepeatedCompositeFieldContainer[bytes]'


class ExchangeGetPrefixMatch(Message):
    # __init__
    prefix: 'str'
    matches: 'RepeatedCompositeFieldContainer[str]'


class ExchangeCombinedSearch(Message):
    # __init__
    filter: 'ExchangeGalleryFilter'
    persona: 'str'
    keyword: 'str'
    type: 'ExchangeItemTypes'
    venue: 'int'  # uint64
    uuid: 'bytes'
    counter_value: 'int'  # uint32
    max_results: 'int'  # uint32
    content_type: 'ExchangeContentType'
    hashtag: 'str'
    sim_size: 'ExchangeGallerySecondaryFilter'
    lot_size: 'ExchangeGallerySecondaryFilter'
    room_size: 'ExchangeGallerySecondaryFilter'
    room_height: 'ExchangeGalleryWallHeight'
    price_range: 'ExchangeGalleryPriceRange'
    room_type: 'int'  # uint64
    sku: 'int'  # uint64
    language: 'int'  # uint64
    modded: 'int'  # uint64
    locked: 'int'  # uint64
    nucleusid: 'int'  # uint64
    exclude_reported: 'bool'
    platform_filter: 'ExchangeItemPlatformFilter'
    sku2: 'int'  # uint64
    persona_type: 'ExchangePersonaSearchType'
    nextToken: 'str'
    favorites_nucleusid: 'int'  # uint64
    download_count_range_min: 'int'  # uint64
    upload_time_range_start: 'int'  # uint64
    upload_time_range_end: 'int'  # uint64
    exclusive_packs: 'RepeatedCompositeFieldContainer[int]'  # uint32
    body_type: 'int'  # uint32
    compatible_item_version: 'int'  # uint32
    keyword_type: 'KeywordSearchType'
    sku_bits: 'RepeatedCompositeFieldContainer[int]'  # uint32


class ExchangeTestParameters(Message):
    # __init__
    max_entries: 'int'  # uint64
    broadcast: 'bool'
    low_range: 'int'  # uint64
    high_range: 'int'  # uint64


class ExchangeSocialMessage(Message):
    # __init__
    friends: 'RepeatedCompositeFieldContainer[int]'  # uint64
    subscriptions: 'RepeatedCompositeFieldContainer[int]'  # uint64
    added: 'bool'


class ExchangeWWCEMessage(Message):
    # __init__
    requestid: 'int'  # uint64
    reporter_nucleusid: 'int'  # uint64
    reported_nucleusid: 'int'  # uint64
    offense_field: 'int'  # uint32
    offense_description: 'str'
    content_uuid: 'str'
    content_type: 'int'  # uint32
    comment_id: 'bytes'
    reporter_persona: 'str'
    reported_persona: 'str'
    content_metadata: 'TrayMetadata'
    locale: 'str'
    bio_persona_id: 'int'  # uint64
    reporter_platform: 'str'
    petition_category: 'PetitionCategory'
    petition_content_type: 'PetitionContentType'


class ExchangeWWCEHideMessage(Message):
    # __init__
    hide: 'bool'
    content_uuid: 'str'
    content_type: 'int'  # uint32


class ExchangeWWCEKickMessage(Message):
    # __init__
    persona: 'str'


class ExchangeWWCEResponse(Message):
    # __init__
    petition_guid: 'str'
    op_result: 'WWCEOpResult'
    content_guid: 'str'
    content_type: 'int'  # uint32
    petition_code: 'int'  # uint32


class UGCShare(Message):
    class CTDDescription():
        # __init__
        value: 'CTDValue'
        category: 'CTDCategory'

    # __init__
    id: 'int'  # uint64
    ctd_details: 'RepeatedCompositeFieldContainer[UGCShare.CTDDescription]'
    pf_check: 'bool'
    value: 'CTDValue'
    category: 'CTDCategory'


class ExchangeFetchPlayerInfoMessage(Message):
    # __init__
    playerid: 'int'  # uint64
    playername: 'str'
    platformplayerid: 'int'  # uint64
    platformplayername: 'str'


class SocialId(Message):
    # __init__
    persona: 'str'
    s4guid: 'int'  # uint64
    guid_descriptor: 'str'
    nucleusId: 'int'  # uint64


class SocialResponseFollowersMessage(Message):
    class PlayerFollower():
        # __init__
        follower_id: 'int'  # uint64
        id: 'bytes'
        follower_persona: 'str'
        num_followers: 'int'  # uint32
        first_party_persona: 'str'

    # __init__
    nucleusid: 'int'  # uint64
    followerslist: 'RepeatedCompositeFieldContainer[SocialResponseFollowersMessage.PlayerFollower]'
    index: 'int'  # uint32
    total_follower_count: 'int'  # uint32
    follower_id: 'int'  # uint64
    id: 'bytes'
    follower_persona: 'str'
    num_followers: 'int'  # uint32
    first_party_persona: 'str'


class SocialFeedSubMessage(Message):
    class SubscriptionFlags():
        # __init__
        hidden: 'bool'
        filterTypes: 'RepeatedCompositeFieldContainer[int]'  # uint32

    class SubscriptionObject():
        # __init__
        name: 'str'
        id: 'SocialId'
        flags: 'SocialFeedSubMessage.SubscriptionFlags'
        first_party_persona: 'str'

    # __init__
    owner_id: 'SocialId'
    subscriptions: 'RepeatedCompositeFieldContainer[SocialFeedSubMessage.SubscriptionObject]'
    hidden: 'bool'
    filterTypes: 'RepeatedCompositeFieldContainer[int]'  # uint32
    name: 'str'
    id: 'SocialId'
    flags: 'SocialFeedSubMessage.SubscriptionFlags'
    first_party_persona: 'str'


class SocialCGVotePeriodMessage(Message):
    # __init__
    challenge_name: 'str'
    start_epoch_utc_sec: 'int'  # uint64
    end_epoch_utc_sec: 'int'  # uint64


class SocialCandidateReportMessage(Message):
    # __init__
    uuid_as_string: 'str'
    challenge: 'str'
    was_reported: 'bool'


class SocialCandidatesBroadcast(Message):
    # __init__
    challenge_name: 'str'
    last_requested_epoch_sec: 'int'  # uint64
    candidate_last_views: 'int'  # uint32
    remove_candidate_uuid: 'bytes'
    remove_candidate_category: 'int'  # uint32


class SocialCGUpdateMessage(Message):
    # __init__
    challenge_period: 'RepeatedCompositeFieldContainer[SocialCGVotePeriodMessage]'
    report_msg: 'SocialCandidateReportMessage'
    candidate_broadcast_msg: 'SocialCandidatesBroadcast'


class ServerPlayerIdentificationMessage(Message):
    # __init__
    playerid: 'int'  # uint64
    persona: 'str'
    platform_persona_id: 'int'  # uint64
    platform_persona: 'str'
    first_party_playerid: 'int'  # uint64


class ServerCallbackInfoMessage(Message):
    # __init__
    callback_op: 'int'  # uint64
    client_reply_proxy_id: 'int'  # uint64
    transaction_id: 'int'  # uint64
    platform_type: 'ExchangeItemPlatform'


class ServerPlayerIdentificationListMessage(Message):
    # __init__
    key_type: 'ePlayerIdentificationType'
    want_type: 'int'  # uint32
    player_info_list: 'RepeatedCompositeFieldContainer[ServerPlayerIdentificationMessage]'
    server_callback_info: 'ServerCallbackInfoMessage'
    social_responsefollowers_msg: 'SocialResponseFollowersMessage'
    social_feed_submessage: 'SocialFeedSubMessage'


class ExchangeFetchPlayerStatistics(Message):
    # __init__
    playerid: 'int'  # uint64
    downloads: 'int'  # uint32
    shared: 'int'  # uint32
    followers: 'int'  # uint32
    communityevent1: 'int'  # uint32


class ExchangeFetchSubcriptionStats(Message):
    # __init__
    fetchplayerstats: 'RepeatedCompositeFieldContainer[ExchangeFetchPlayerStatistics]'


class ExchangeHashtagTrendsMessage(Message):
    # __init__
    results: 'RepeatedCompositeFieldContainer[str]'


class ExchangeModerateMessage(Message):
    # __init__
    tag: 'str'
    value: 'int'  # uint32


class ExchangeStatTicker(Message):
    # __init__
    type: 'int'  # uint32
    value: 'int'  # uint32


class ExchangeStatTickerMessage(Message):
    # __init__
    data: 'RepeatedCompositeFieldContainer[ExchangeStatTicker]'


class ExchangeGetSharedItemsByIdMessage(Message):
    # __init__
    remote_ids: 'RepeatedCompositeFieldContainer[bytes]'


class ExchangeItemWithStatus(Message):
    # __init__
    remote_id: 'bytes'
    status_code: 'int'  # uint32
    timestamp_id: 'bytes'


class ExchangeItemListWebMessage(Message):
    # __init__
    items: 'RepeatedCompositeFieldContainer[ExchangeItemWithStatus]'
    max_items: 'int'  # uint32
    last_item: 'bytes'


class ExchangeRecommendationEngineResult(Message):
    # __init__
    recommendation_engine_segment_id: 'int'  # uint64
    recommendation_engine_url: 'str'


class ExchangeControlMessage(Message):
    # __init__
    opcode: 'ExchangeOpTypes'
    result: 'ExchangeOpResult'
    envelope: 'ExchangeEnvelope'
    getlistmsg: 'ExchangeListResults'
    webserveruri: 'ExchangeWebserverUri'
    searchrequestmsg: 'ExchangeSearchRequest'
    fetchbystatmsg: 'ExchangeFetchByStatRequest'
    getupdatedstatsmsg: 'ExchangeGetUpdatedStats'
    getprefixmatch: 'ExchangeGetPrefixMatch'
    fetchkeywordmsg: 'ExchangeFetchKeywordRequest'
    fetchrecentmsg: 'ExchangeFetchRecentRequest'
    combinedsearchmsg: 'ExchangeCombinedSearch'
    exchangetest: 'ExchangeTestParameters'
    exchangesocial: 'ExchangeSocialMessage'
    wwcemsg: 'ExchangeWWCEMessage'
    wwceresponse: 'ExchangeWWCEResponse'
    wwcehidemsg: 'ExchangeWWCEHideMessage'
    fetchplayerinfomsg: 'ExchangeFetchPlayerInfoMessage'
    fetchplayerstats: 'ExchangeFetchPlayerStatistics'
    subscribers_stats: 'ExchangeFetchSubcriptionStats'
    hashtagtrends: 'ExchangeHashtagTrendsMessage'
    moderatemsg: 'ExchangeModerateMessage'
    stat_tickers: 'ExchangeStatTickerMessage'
    items_request: 'ExchangeGetSharedItemsByIdMessage'
    item_weblist: 'ExchangeItemListWebMessage'
    wwcekickmsg: 'ExchangeWWCEKickMessage'
    recommendation_engine_result: 'ExchangeRecommendationEngineResult'
    player_identification_list_msg: 'ServerPlayerIdentificationListMessage'
    ugc_share_msg: 'UGCShare'
    transactionId: 'int'  # uint64
