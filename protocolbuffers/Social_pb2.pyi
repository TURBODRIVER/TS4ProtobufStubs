from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer
from enum import IntEnum

from protocolbuffers.Consts_pb2 import *
from protocolbuffers.S4Common_pb2 import *
from protocolbuffers.Localization_pb2 import *
from protocolbuffers.Exchange_pb2 import *


class SocialFeedItemType(IntEnum):
    SFI_ITEM_DOWNLOADED: 'SocialFeedItemType' = 0
    SFI_ITEM_UPLOADED: 'SocialFeedItemType' = 1
    SFI_ITEM_FAVORITED: 'SocialFeedItemType' = 2
    SFI_ITEM_COMMENTED: 'SocialFeedItemType' = 3
    SFI_ITEM_SHOWCASED: 'SocialFeedItemType' = 4
    SFI_PROFILE_COMMENTED: 'SocialFeedItemType' = 5
    SFI_NEW_FOLLOWERS: 'SocialFeedItemType' = 6


SFI_ITEM_DOWNLOADED = SocialFeedItemType.SFI_ITEM_DOWNLOADED
SFI_ITEM_UPLOADED = SocialFeedItemType.SFI_ITEM_UPLOADED
SFI_ITEM_FAVORITED = SocialFeedItemType.SFI_ITEM_FAVORITED
SFI_ITEM_COMMENTED = SocialFeedItemType.SFI_ITEM_COMMENTED
SFI_ITEM_SHOWCASED = SocialFeedItemType.SFI_ITEM_SHOWCASED
SFI_PROFILE_COMMENTED = SocialFeedItemType.SFI_PROFILE_COMMENTED
SFI_NEW_FOLLOWERS = SocialFeedItemType.SFI_NEW_FOLLOWERS


class SocialClusterMessageType(IntEnum):
    SOC_LOGIN: 'SocialClusterMessageType' = 0
    SOC_LOGOFF: 'SocialClusterMessageType' = 1
    SOC_PRESENCEUPDATE: 'SocialClusterMessageType' = 2
    SOC_FEEDUPDATE: 'SocialClusterMessageType' = 3
    SOC_ADD_FEEDSUB: 'SocialClusterMessageType' = 4
    SOC_REMOVE_FEEDSUB: 'SocialClusterMessageType' = 5
    SOC_BROADCAST_PRIVOP: 'SocialClusterMessageType' = 6
    SOC_BROADCAST_QUEUED: 'SocialClusterMessageType' = 8
    SOC_BROADCAST_CACHE_INVALIDATE: 'SocialClusterMessageType' = 9
    SOC_REST_USER_REGISTER: 'SocialClusterMessageType' = 10


SOC_LOGIN = SocialClusterMessageType.SOC_LOGIN
SOC_LOGOFF = SocialClusterMessageType.SOC_LOGOFF
SOC_PRESENCEUPDATE = SocialClusterMessageType.SOC_PRESENCEUPDATE
SOC_FEEDUPDATE = SocialClusterMessageType.SOC_FEEDUPDATE
SOC_ADD_FEEDSUB = SocialClusterMessageType.SOC_ADD_FEEDSUB
SOC_REMOVE_FEEDSUB = SocialClusterMessageType.SOC_REMOVE_FEEDSUB
SOC_BROADCAST_PRIVOP = SocialClusterMessageType.SOC_BROADCAST_PRIVOP
SOC_BROADCAST_QUEUED = SocialClusterMessageType.SOC_BROADCAST_QUEUED
SOC_BROADCAST_CACHE_INVALIDATE = SocialClusterMessageType.SOC_BROADCAST_CACHE_INVALIDATE
SOC_REST_USER_REGISTER = SocialClusterMessageType.SOC_REST_USER_REGISTER


class SocialFriendMsg(Message):
    # __init__
    simId: 'int'  # uint64
    nucleusid: 'int'  # uint64
    note: 'str'
    prefix: 'str'
    persona: 'str'
    cheatForce: 'bool'


class SocialPersonaResponseMsg(Message):
    # __init__
    personas: 'RepeatedCompositeFieldContainer[str]'


class SocialGenericResponse(Message):
    # __init__
    error: 'int'  # uint32
    msg_type: 'SocialOpTypes'
    postId: 'bytes'
    postParentId: 'bytes'


class SocialPlayerInfoList(Message):
    class PlayerInfo():
        # __init__
        AccountName: 'str'
        AccountNotes: 'str'
        presence: 'OnlinePresenceStatus'
        OnlineStatus2: 'str'
        NucleusId: 'int'  # uint64
        PlayerBio: 'str'
        exclude_reported: 'bool'
        IsUserBlocked: 'bool'

    # __init__
    players: 'RepeatedCompositeFieldContainer[SocialPlayerInfoList.PlayerInfo]'
    AccountName: 'str'
    AccountNotes: 'str'
    presence: 'OnlinePresenceStatus'
    OnlineStatus2: 'str'
    NucleusId: 'int'  # uint64
    PlayerBio: 'str'
    exclude_reported: 'bool'
    IsUserBlocked: 'bool'


class SocialSearchMsg(Message):
    # __init__
    prefix: 'str'
    search_results: 'RepeatedCompositeFieldContainer[LocalizedStringToken]'


class OriginErrorMessage(Message):
    # __init__
    errorcode: 'int'  # uint32
    errormessage: 'str'


class SocialInviteResponseMessage(Message):
    # __init__
    invitationid: 'str'
    invitationtype: 'int'  # uint32
    inviternucleusid: 'int'  # uint64
    accepternucleusid: 'int'  # uint64
    actionSuccess: 'bool'


class SocialCassandraTest(Message):
    # __init__
    opcode: 'CassandraTestCode'


class SocialFriendListRequestMessage(Message):
    # __init__
    account_id: 'int'  # uint64
    friend_id: 'int'  # uint64
    address_str: 'str'
    object_str: 'str'
    reply_proxy_id: 'int'  # uint64


class SocialRequestNucleusIdFromPersona(Message):
    # __init__
    requestid: 'int'  # uint64
    personaName: 'str'
    message_id: 'int'  # uint32


class SocialNucleusIdFromPersonaResponse(Message):
    # __init__
    requestid: 'int'  # uint64
    nucleusid: 'int'  # uint64
    message_id: 'int'  # uint32


class SocialExchangeMessage(Message):
    # __init__
    envelope: 'ExchangeSocialEnvelope'


class SocialFollowersMessage(Message):
    # __init__
    sfim_blob: 'RepeatedCompositeFieldContainer[bytes]'


class SocialFeedItemMessage(Message):
    # __init__
    feed_id: 'bytes'
    feed_type: 'SocialFeedItemType'
    metadata: 'TrayMetadata'
    nucleusid: 'int'  # uint64
    persona: 'str'
    quantity: 'int'  # uint64
    follower_nucleusid: 'int'  # uint64
    follower_persona: 'str'
    followers_blob: 'SocialFollowersMessage'
    is_maxis_curated: 'bool'


class SocialFeedItemUnserializedMessage(Message):
    # __init__
    feed_id: 'bytes'
    data: 'bytes'
    count_override: 'int'  # uint64


class SocialWallCommentMessage(Message):
    # __init__
    uuid: 'bytes'
    author_id: 'int'  # uint64
    author_persona: 'str'
    message: 'str'
    created_timestamp: 'int'  # uint64


class SocialGetWallCommentsMessage(Message):
    # __init__
    nucleusid: 'int'  # uint64
    gallery_id: 'bytes'
    starting_uuid: 'bytes'
    num_results: 'int'  # uint32
    messages: 'RepeatedCompositeFieldContainer[SocialWallCommentMessage]'
    hidden: 'bool'
    exclude_reported: 'bool'
    nextToken: 'str'


class SocialPostWallCommentMessage(Message):
    # __init__
    nucleusid: 'int'  # uint64
    gallery_id: 'bytes'
    message: 'SocialWallCommentMessage'


class SocialDeleteWallCommentMessage(Message):
    # __init__
    nucleusid: 'int'  # uint64
    gallery_id: 'bytes'
    uuid: 'bytes'


class SocialRequestFeedWallMessage(Message):
    # __init__
    ending_uuid: 'bytes'
    messages: 'RepeatedCompositeFieldContainer[SocialFeedItemMessage]'
    unserialized_messages: 'RepeatedCompositeFieldContainer[SocialFeedItemUnserializedMessage]'
    num_items: 'int'  # uint32


class SocialRequestFollowersMessage(Message):
    # __init__
    playerid: 'int'  # uint64
    id: 'str'
    prev_last_persona: 'str'
    num_request: 'int'  # uint32


class SocialRequestIgnoreListMessage(Message):
    # __init__
    player_nucleus_id: 'int'  # uint64


class SocialGetPlayerInfoListMessage(Message):
    class PlayerInfo():
        # __init__
        nucleus_id: 'int'  # uint64
        origin_persona: 'str'
        first_party_persona: 'str'

    # __init__
    player_nucleus_id: 'int'  # uint64
    player_info_list: 'RepeatedCompositeFieldContainer[SocialGetPlayerInfoListMessage.PlayerInfo]'
    nucleus_id: 'int'  # uint64
    origin_persona: 'str'
    first_party_persona: 'str'


class SocialCommentPetitionMessage(Message):
    # __init__
    nucleusid: 'int'  # uint64
    commentid: 'bytes'
    commentKey: 'str'


class SocialBioPetitionMessage(Message):
    # __init__
    nucleusid: 'int'  # uint64
    bio_nucleusid: 'int'  # uint64


class SocialFeedRemovalMessage(Message):
    # __init__
    feed_id: 'bytes'


class SocialControlMessage(Message):
    # __init__
    opcode: 'SocialOpTypes'
    subop: 'SocialOpTypes'
    transactionId: 'int'  # uint64
    result: 'int'  # uint32
    getwallcommentsmsg: 'SocialGetWallCommentsMessage'
    postwallcommentmsg: 'SocialPostWallCommentMessage'
    deletewallcommentmsg: 'SocialDeleteWallCommentMessage'
    friendmsg: 'SocialFriendMsg'
    genericresponse: 'SocialGenericResponse'
    playerinfo: 'SocialPlayerInfoList'
    feedsubmsg: 'SocialFeedSubMessage'
    searchresultmsg: 'SocialSearchMsg'
    inviteresponsemsg: 'SocialInviteResponseMessage'
    originerror: 'OriginErrorMessage'
    socialcassandratest: 'SocialCassandraTest'
    socialfriendlistrequestmsg: 'SocialFriendListRequestMessage'
    socialrequestnucleusidfrompersona: 'SocialRequestNucleusIdFromPersona'
    socialnucleusidfrompersonaresponse: 'SocialNucleusIdFromPersonaResponse'
    socialexchangemessage: 'SocialExchangeMessage'
    socialrequestfeedwallmessage: 'SocialRequestFeedWallMessage'
    stat_tickers: 'ExchangeStatTickerMessage'
    comment_petition_msg: 'SocialCommentPetitionMessage'
    feedremovalmsg: 'SocialFeedRemovalMessage'
    bio_petition_msg: 'SocialBioPetitionMessage'
    fb_event_msg: 'SocialFacebookEventMessage'
    requestfollowers_msg: 'SocialRequestFollowersMessage'
    responsefollowers_msg: 'SocialResponseFollowersMessage'
    requestignorelist_msg: 'SocialRequestIgnoreListMessage'
    response_player_info_list_msg: 'SocialGetPlayerInfoListMessage'
    player_identification_list_msg: 'ServerPlayerIdentificationListMessage'
    candidate_msg: 'SocialCandidatesMessage'
    evaluation_results_msg: 'SocialEvaluationResultsMessage'
    cg_update_msg: 'SocialCGUpdateMessage'
    ugc_share_msg: 'UGCShare'


class SocialInvalidateMsg(Message):
    # __init__
    cache_index: 'int'  # uint32
    key: 'bytes'


class SocialControlQueueBroadcastMessage(Message):
    # __init__
    control: 'SocialControlMessage'
    friendIds: 'RepeatedCompositeFieldContainer[int]'  # uint64


class LifeEventMessage(Message):
    # __init__
    type: 'int'  # uint32
    sim_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class SocialFacebookEventMessage(Message):
    # __init__
    objectId: 'str'
    accessToken: 'str'
    guid: 'str'


class SocialCandidateStatisticSubmessage(Message):
    # __init__
    remote_id: 'bytes'
    views_count: 'int'  # uint32
    wins_count: 'int'  # uint32
    platform: 'int'  # uint32
    category: 'int'  # uint32
    was_reported: 'bool'
    expires_epoch_sec: 'int'  # uint64


class SocialCandidatesMessage(Message):
    # __init__
    count: 'int'  # uint32
    platform_restriction: 'int'  # uint32
    category_restriction: 'int'  # uint32
    challenge: 'str'
    digest: 'bytes'
    candidates: 'RepeatedCompositeFieldContainer[SocialCandidateStatisticSubmessage]'
    expire_epoch_secs: 'int'  # uint64


class SocialEvaluationResultsMessage(Message):
    # __init__
    winner_ids: 'RepeatedCompositeFieldContainer[str]'
    loser_ids: 'RepeatedCompositeFieldContainer[str]'
    digest: 'bytes'


class SocialCGDigestMessage(Message):
    # __init__
    challenge: 'str'
    candidates: 'RepeatedCompositeFieldContainer[SocialCandidateStatisticSubmessage]'
