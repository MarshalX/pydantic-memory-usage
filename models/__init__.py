from models.app.bsky.actor import defs as AppBskyActorDefs
from models.app.bsky.actor import get_preferences as AppBskyActorGetPreferences
from models.app.bsky.actor import get_profile as AppBskyActorGetProfile
from models.app.bsky.actor import get_profiles as AppBskyActorGetProfiles
from models.app.bsky.actor import get_suggestions as AppBskyActorGetSuggestions
from models.app.bsky.actor import profile as AppBskyActorProfile
from models.app.bsky.actor import put_preferences as AppBskyActorPutPreferences
from models.app.bsky.actor import search_actors as AppBskyActorSearchActors
from models.app.bsky.actor import search_actors_typeahead as AppBskyActorSearchActorsTypeahead
from models.app.bsky.embed import external as AppBskyEmbedExternal
from models.app.bsky.embed import images as AppBskyEmbedImages
from models.app.bsky.embed import record as AppBskyEmbedRecord
from models.app.bsky.embed import record_with_media as AppBskyEmbedRecordWithMedia
from models.app.bsky.feed import defs as AppBskyFeedDefs
from models.app.bsky.feed import describe_feed_generator as AppBskyFeedDescribeFeedGenerator
from models.app.bsky.feed import generator as AppBskyFeedGenerator
from models.app.bsky.feed import get_actor_feeds as AppBskyFeedGetActorFeeds
from models.app.bsky.feed import get_actor_likes as AppBskyFeedGetActorLikes
from models.app.bsky.feed import get_author_feed as AppBskyFeedGetAuthorFeed
from models.app.bsky.feed import get_feed as AppBskyFeedGetFeed
from models.app.bsky.feed import get_feed_generator as AppBskyFeedGetFeedGenerator
from models.app.bsky.feed import get_feed_generators as AppBskyFeedGetFeedGenerators
from models.app.bsky.feed import get_feed_skeleton as AppBskyFeedGetFeedSkeleton
from models.app.bsky.feed import get_likes as AppBskyFeedGetLikes
from models.app.bsky.feed import get_list_feed as AppBskyFeedGetListFeed
from models.app.bsky.feed import get_post_thread as AppBskyFeedGetPostThread
from models.app.bsky.feed import get_posts as AppBskyFeedGetPosts
from models.app.bsky.feed import get_reposted_by as AppBskyFeedGetRepostedBy
from models.app.bsky.feed import get_suggested_feeds as AppBskyFeedGetSuggestedFeeds
from models.app.bsky.feed import get_timeline as AppBskyFeedGetTimeline
from models.app.bsky.feed import like as AppBskyFeedLike
from models.app.bsky.feed import post as AppBskyFeedPost
from models.app.bsky.feed import repost as AppBskyFeedRepost
from models.app.bsky.feed import search_posts as AppBskyFeedSearchPosts
from models.app.bsky.feed import send_interactions as AppBskyFeedSendInteractions
from models.app.bsky.feed import threadgate as AppBskyFeedThreadgate
from models.app.bsky.graph import block as AppBskyGraphBlock
from models.app.bsky.graph import defs as AppBskyGraphDefs
from models.app.bsky.graph import follow as AppBskyGraphFollow
from models.app.bsky.graph import get_actor_starter_packs as AppBskyGraphGetActorStarterPacks
from models.app.bsky.graph import get_blocks as AppBskyGraphGetBlocks
from models.app.bsky.graph import get_followers as AppBskyGraphGetFollowers
from models.app.bsky.graph import get_follows as AppBskyGraphGetFollows
from models.app.bsky.graph import get_known_followers as AppBskyGraphGetKnownFollowers
from models.app.bsky.graph import get_list as AppBskyGraphGetList
from models.app.bsky.graph import get_list_blocks as AppBskyGraphGetListBlocks
from models.app.bsky.graph import get_list_mutes as AppBskyGraphGetListMutes
from models.app.bsky.graph import get_lists as AppBskyGraphGetLists
from models.app.bsky.graph import get_mutes as AppBskyGraphGetMutes
from models.app.bsky.graph import get_relationships as AppBskyGraphGetRelationships
from models.app.bsky.graph import get_starter_pack as AppBskyGraphGetStarterPack
from models.app.bsky.graph import get_starter_packs as AppBskyGraphGetStarterPacks
from models.app.bsky.graph import (
    get_suggested_follows_by_actor as AppBskyGraphGetSuggestedFollowsByActor,
)
from models.app.bsky.graph import list as AppBskyGraphList
from models.app.bsky.graph import listblock as AppBskyGraphListblock
from models.app.bsky.graph import listitem as AppBskyGraphListitem
from models.app.bsky.graph import mute_actor as AppBskyGraphMuteActor
from models.app.bsky.graph import mute_actor_list as AppBskyGraphMuteActorList
from models.app.bsky.graph import mute_thread as AppBskyGraphMuteThread
from models.app.bsky.graph import starterpack as AppBskyGraphStarterpack
from models.app.bsky.graph import unmute_actor as AppBskyGraphUnmuteActor
from models.app.bsky.graph import unmute_actor_list as AppBskyGraphUnmuteActorList
from models.app.bsky.graph import unmute_thread as AppBskyGraphUnmuteThread
from models.app.bsky.labeler import defs as AppBskyLabelerDefs
from models.app.bsky.labeler import get_services as AppBskyLabelerGetServices
from models.app.bsky.labeler import service as AppBskyLabelerService
from models.app.bsky.notification import get_unread_count as AppBskyNotificationGetUnreadCount
from models.app.bsky.notification import list_notifications as AppBskyNotificationListNotifications
from models.app.bsky.notification import put_preferences as AppBskyNotificationPutPreferences
from models.app.bsky.notification import register_push as AppBskyNotificationRegisterPush
from models.app.bsky.notification import update_seen as AppBskyNotificationUpdateSeen
from models.app.bsky.richtext import facet as AppBskyRichtextFacet
from models.app.bsky.unspecced import defs as AppBskyUnspeccedDefs
from models.app.bsky.unspecced import (
    get_popular_feed_generators as AppBskyUnspeccedGetPopularFeedGenerators,
)
from models.app.bsky.unspecced import get_suggestions_skeleton as AppBskyUnspeccedGetSuggestionsSkeleton
from models.app.bsky.unspecced import get_tagged_suggestions as AppBskyUnspeccedGetTaggedSuggestions
from models.app.bsky.unspecced import search_actors_skeleton as AppBskyUnspeccedSearchActorsSkeleton
from models.app.bsky.unspecced import search_posts_skeleton as AppBskyUnspeccedSearchPostsSkeleton
from models.chat.bsky.actor import declaration as ChatBskyActorDeclaration
from models.chat.bsky.actor import defs as ChatBskyActorDefs
from models.chat.bsky.actor import delete_account as ChatBskyActorDeleteAccount
from models.chat.bsky.actor import export_account_data as ChatBskyActorExportAccountData
from models.chat.bsky.convo import defs as ChatBskyConvoDefs
from models.chat.bsky.convo import delete_message_for_self as ChatBskyConvoDeleteMessageForSelf
from models.chat.bsky.convo import get_convo as ChatBskyConvoGetConvo
from models.chat.bsky.convo import get_convo_for_members as ChatBskyConvoGetConvoForMembers
from models.chat.bsky.convo import get_log as ChatBskyConvoGetLog
from models.chat.bsky.convo import get_messages as ChatBskyConvoGetMessages
from models.chat.bsky.convo import leave_convo as ChatBskyConvoLeaveConvo
from models.chat.bsky.convo import list_convos as ChatBskyConvoListConvos
from models.chat.bsky.convo import mute_convo as ChatBskyConvoMuteConvo
from models.chat.bsky.convo import send_message as ChatBskyConvoSendMessage
from models.chat.bsky.convo import send_message_batch as ChatBskyConvoSendMessageBatch
from models.chat.bsky.convo import unmute_convo as ChatBskyConvoUnmuteConvo
from models.chat.bsky.convo import update_read as ChatBskyConvoUpdateRead
from models.chat.bsky.moderation import get_actor_metadata as ChatBskyModerationGetActorMetadata
from models.chat.bsky.moderation import get_message_context as ChatBskyModerationGetMessageContext
from models.chat.bsky.moderation import update_actor_access as ChatBskyModerationUpdateActorAccess
from models.com.atproto.admin import defs as ComAtprotoAdminDefs
from models.com.atproto.admin import delete_account as ComAtprotoAdminDeleteAccount
from models.com.atproto.admin import disable_account_invites as ComAtprotoAdminDisableAccountInvites
from models.com.atproto.admin import disable_invite_codes as ComAtprotoAdminDisableInviteCodes
from models.com.atproto.admin import enable_account_invites as ComAtprotoAdminEnableAccountInvites
from models.com.atproto.admin import get_account_info as ComAtprotoAdminGetAccountInfo
from models.com.atproto.admin import get_account_infos as ComAtprotoAdminGetAccountInfos
from models.com.atproto.admin import get_invite_codes as ComAtprotoAdminGetInviteCodes
from models.com.atproto.admin import get_subject_status as ComAtprotoAdminGetSubjectStatus
from models.com.atproto.admin import search_accounts as ComAtprotoAdminSearchAccounts
from models.com.atproto.admin import send_email as ComAtprotoAdminSendEmail
from models.com.atproto.admin import update_account_email as ComAtprotoAdminUpdateAccountEmail
from models.com.atproto.admin import update_account_handle as ComAtprotoAdminUpdateAccountHandle
from models.com.atproto.admin import update_account_password as ComAtprotoAdminUpdateAccountPassword
from models.com.atproto.admin import update_subject_status as ComAtprotoAdminUpdateSubjectStatus
from models.com.atproto.identity import (
    get_recommended_did_credentials as ComAtprotoIdentityGetRecommendedDidCredentials,
)
from models.com.atproto.identity import (
    request_plc_operation_signature as ComAtprotoIdentityRequestPlcOperationSignature,
)
from models.com.atproto.identity import resolve_handle as ComAtprotoIdentityResolveHandle
from models.com.atproto.identity import sign_plc_operation as ComAtprotoIdentitySignPlcOperation
from models.com.atproto.identity import submit_plc_operation as ComAtprotoIdentitySubmitPlcOperation
from models.com.atproto.identity import update_handle as ComAtprotoIdentityUpdateHandle
from models.com.atproto.label import defs as ComAtprotoLabelDefs
from models.com.atproto.label import query_labels as ComAtprotoLabelQueryLabels
from models.com.atproto.label import subscribe_labels as ComAtprotoLabelSubscribeLabels
from models.com.atproto.moderation import create_report as ComAtprotoModerationCreateReport
from models.com.atproto.moderation import defs as ComAtprotoModerationDefs
from models.com.atproto.repo import apply_writes as ComAtprotoRepoApplyWrites
from models.com.atproto.repo import create_record as ComAtprotoRepoCreateRecord
from models.com.atproto.repo import delete_record as ComAtprotoRepoDeleteRecord
from models.com.atproto.repo import describe_repo as ComAtprotoRepoDescribeRepo
from models.com.atproto.repo import get_record as ComAtprotoRepoGetRecord
from models.com.atproto.repo import import_repo as ComAtprotoRepoImportRepo
from models.com.atproto.repo import list_missing_blobs as ComAtprotoRepoListMissingBlobs
from models.com.atproto.repo import list_records as ComAtprotoRepoListRecords
from models.com.atproto.repo import put_record as ComAtprotoRepoPutRecord
from models.com.atproto.repo import strong_ref as ComAtprotoRepoStrongRef
from models.com.atproto.repo import upload_blob as ComAtprotoRepoUploadBlob
from models.com.atproto.server import activate_account as ComAtprotoServerActivateAccount
from models.com.atproto.server import check_account_status as ComAtprotoServerCheckAccountStatus
from models.com.atproto.server import confirm_email as ComAtprotoServerConfirmEmail
from models.com.atproto.server import create_account as ComAtprotoServerCreateAccount
from models.com.atproto.server import create_app_password as ComAtprotoServerCreateAppPassword
from models.com.atproto.server import create_invite_code as ComAtprotoServerCreateInviteCode
from models.com.atproto.server import create_invite_codes as ComAtprotoServerCreateInviteCodes
from models.com.atproto.server import create_session as ComAtprotoServerCreateSession
from models.com.atproto.server import deactivate_account as ComAtprotoServerDeactivateAccount
from models.com.atproto.server import defs as ComAtprotoServerDefs
from models.com.atproto.server import delete_account as ComAtprotoServerDeleteAccount
from models.com.atproto.server import delete_session as ComAtprotoServerDeleteSession
from models.com.atproto.server import describe_server as ComAtprotoServerDescribeServer
from models.com.atproto.server import get_account_invite_codes as ComAtprotoServerGetAccountInviteCodes
from models.com.atproto.server import get_service_auth as ComAtprotoServerGetServiceAuth
from models.com.atproto.server import get_session as ComAtprotoServerGetSession
from models.com.atproto.server import list_app_passwords as ComAtprotoServerListAppPasswords
from models.com.atproto.server import refresh_session as ComAtprotoServerRefreshSession
from models.com.atproto.server import request_account_delete as ComAtprotoServerRequestAccountDelete
from models.com.atproto.server import (
    request_email_confirmation as ComAtprotoServerRequestEmailConfirmation,
)
from models.com.atproto.server import request_email_update as ComAtprotoServerRequestEmailUpdate
from models.com.atproto.server import request_password_reset as ComAtprotoServerRequestPasswordReset
from models.com.atproto.server import reserve_signing_key as ComAtprotoServerReserveSigningKey
from models.com.atproto.server import reset_password as ComAtprotoServerResetPassword
from models.com.atproto.server import revoke_app_password as ComAtprotoServerRevokeAppPassword
from models.com.atproto.server import update_email as ComAtprotoServerUpdateEmail
from models.com.atproto.sync import get_blob as ComAtprotoSyncGetBlob
from models.com.atproto.sync import get_blocks as ComAtprotoSyncGetBlocks
from models.com.atproto.sync import get_checkout as ComAtprotoSyncGetCheckout
from models.com.atproto.sync import get_head as ComAtprotoSyncGetHead
from models.com.atproto.sync import get_latest_commit as ComAtprotoSyncGetLatestCommit
from models.com.atproto.sync import get_record as ComAtprotoSyncGetRecord
from models.com.atproto.sync import get_repo as ComAtprotoSyncGetRepo
from models.com.atproto.sync import get_repo_status as ComAtprotoSyncGetRepoStatus
from models.com.atproto.sync import list_blobs as ComAtprotoSyncListBlobs
from models.com.atproto.sync import list_repos as ComAtprotoSyncListRepos
from models.com.atproto.sync import notify_of_update as ComAtprotoSyncNotifyOfUpdate
from models.com.atproto.sync import request_crawl as ComAtprotoSyncRequestCrawl
from models.com.atproto.sync import subscribe_repos as ComAtprotoSyncSubscribeRepos
from models.com.atproto.temp import check_signup_queue as ComAtprotoTempCheckSignupQueue
from models.com.atproto.temp import fetch_labels as ComAtprotoTempFetchLabels
from models.com.atproto.temp import request_phone_verification as ComAtprotoTempRequestPhoneVerification
from models.models_loader import load_models

load_models()
