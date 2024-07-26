import typing as t

import typing_extensions as te
from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class ProfileViewBasic(base.ModelBase):
    did: str
    handle: str
    associated: t.Optional['models.AppBskyActorDefs.ProfileAssociated'] = None
    avatar: t.Optional[str] = None
    created_at: t.Optional[str] = None
    display_name: t.Optional[str] = Field(default=None, max_length=640)
    labels: t.Optional[t.List['models.ComAtprotoLabelDefs.Label']] = None
    viewer: t.Optional['models.AppBskyActorDefs.ViewerState'] = None

    py_type: t.Literal['app.bsky.actor.defs#profileViewBasic'] = Field(
        default='app.bsky.actor.defs#profileViewBasic', alias='$type', frozen=True
    )


class ProfileView(base.ModelBase):
    did: str
    handle: str
    associated: t.Optional['models.AppBskyActorDefs.ProfileAssociated'] = None
    avatar: t.Optional[str] = None
    created_at: t.Optional[str] = None
    description: t.Optional[str] = Field(default=None, max_length=2560)
    display_name: t.Optional[str] = Field(default=None, max_length=640)
    indexed_at: t.Optional[str] = None
    labels: t.Optional[t.List['models.ComAtprotoLabelDefs.Label']] = None
    viewer: t.Optional['models.AppBskyActorDefs.ViewerState'] = None

    py_type: t.Literal['app.bsky.actor.defs#profileView'] = Field(
        default='app.bsky.actor.defs#profileView', alias='$type', frozen=True
    )


class ProfileViewDetailed(base.ModelBase):
    did: str
    handle: str
    associated: t.Optional['models.AppBskyActorDefs.ProfileAssociated'] = None
    avatar: t.Optional[str] = None
    banner: t.Optional[str] = None
    created_at: t.Optional[str] = None
    description: t.Optional[str] = Field(default=None, max_length=2560)
    display_name: t.Optional[str] = Field(default=None, max_length=640)
    followers_count: t.Optional[int] = None
    follows_count: t.Optional[int] = None
    indexed_at: t.Optional[str] = None
    joined_via_starter_pack: t.Optional['models.AppBskyGraphDefs.StarterPackViewBasic'] = None
    labels: t.Optional[t.List['models.ComAtprotoLabelDefs.Label']] = None
    posts_count: t.Optional[int] = None
    viewer: t.Optional['models.AppBskyActorDefs.ViewerState'] = None

    py_type: t.Literal['app.bsky.actor.defs#profileViewDetailed'] = Field(
        default='app.bsky.actor.defs#profileViewDetailed', alias='$type', frozen=True
    )


class ProfileAssociated(base.ModelBase):
    chat: t.Optional['models.AppBskyActorDefs.ProfileAssociatedChat'] = None
    feedgens: t.Optional[int] = None
    labeler: t.Optional[bool] = None
    lists: t.Optional[int] = None
    starter_packs: t.Optional[int] = None

    py_type: t.Literal['app.bsky.actor.defs#profileAssociated'] = Field(
        default='app.bsky.actor.defs#profileAssociated', alias='$type', frozen=True
    )


class ProfileAssociatedChat(base.ModelBase):
    allow_incoming: str

    py_type: t.Literal['app.bsky.actor.defs#profileAssociatedChat'] = Field(
        default='app.bsky.actor.defs#profileAssociatedChat', alias='$type', frozen=True
    )


class ViewerState(base.ModelBase):
    blocked_by: t.Optional[bool] = None
    blocking: t.Optional[str] = None
    blocking_by_list: t.Optional['models.AppBskyGraphDefs.ListViewBasic'] = None
    followed_by: t.Optional[str] = None
    following: t.Optional[str] = None
    known_followers: t.Optional['models.AppBskyActorDefs.KnownFollowers'] = None
    muted: t.Optional[bool] = None
    muted_by_list: t.Optional['models.AppBskyGraphDefs.ListViewBasic'] = None

    py_type: t.Literal['app.bsky.actor.defs#viewerState'] = Field(
        default='app.bsky.actor.defs#viewerState', alias='$type', frozen=True
    )


class KnownFollowers(base.ModelBase):
    count: int
    followers: t.List['models.AppBskyActorDefs.ProfileViewBasic'] = Field(min_length=0, max_length=5)

    py_type: t.Literal['app.bsky.actor.defs#knownFollowers'] = Field(
        default='app.bsky.actor.defs#knownFollowers', alias='$type', frozen=True
    )


Preferences = t.List[
    te.Annotated[
        t.Union[
            'models.AppBskyActorDefs.AdultContentPref',
            'models.AppBskyActorDefs.ContentLabelPref',
            'models.AppBskyActorDefs.SavedFeedsPref',
            'models.AppBskyActorDefs.SavedFeedsPrefV2',
            'models.AppBskyActorDefs.PersonalDetailsPref',
            'models.AppBskyActorDefs.FeedViewPref',
            'models.AppBskyActorDefs.ThreadViewPref',
            'models.AppBskyActorDefs.InterestsPref',
            'models.AppBskyActorDefs.MutedWordsPref',
            'models.AppBskyActorDefs.HiddenPostsPref',
            'models.AppBskyActorDefs.BskyAppStatePref',
            'models.AppBskyActorDefs.LabelersPref',
        ],
        Field(discriminator='py_type'),
    ]
]


class AdultContentPref(base.ModelBase):
    enabled: bool = None

    py_type: t.Literal['app.bsky.actor.defs#adultContentPref'] = Field(
        default='app.bsky.actor.defs#adultContentPref', alias='$type', frozen=True
    )


class ContentLabelPref(base.ModelBase):
    label: str
    visibility: str
    labeler_did: t.Optional[str] = None

    py_type: t.Literal['app.bsky.actor.defs#contentLabelPref'] = Field(
        default='app.bsky.actor.defs#contentLabelPref', alias='$type', frozen=True
    )


class SavedFeed(base.ModelBase):
    id: str
    pinned: bool
    type: str
    value: str

    py_type: t.Literal['app.bsky.actor.defs#savedFeed'] = Field(
        default='app.bsky.actor.defs#savedFeed', alias='$type', frozen=True
    )


class SavedFeedsPrefV2(base.ModelBase):
    items: t.List['models.AppBskyActorDefs.SavedFeed']

    py_type: t.Literal['app.bsky.actor.defs#savedFeedsPrefV2'] = Field(
        default='app.bsky.actor.defs#savedFeedsPrefV2', alias='$type', frozen=True
    )


class SavedFeedsPref(base.ModelBase):
    pinned: t.List[str]
    saved: t.List[str]
    timeline_index: t.Optional[int] = None

    py_type: t.Literal['app.bsky.actor.defs#savedFeedsPref'] = Field(
        default='app.bsky.actor.defs#savedFeedsPref', alias='$type', frozen=True
    )


class PersonalDetailsPref(base.ModelBase):
    birth_date: t.Optional[str] = None

    py_type: t.Literal['app.bsky.actor.defs#personalDetailsPref'] = Field(
        default='app.bsky.actor.defs#personalDetailsPref', alias='$type', frozen=True
    )


class FeedViewPref(base.ModelBase):
    feed: str
    hide_quote_posts: t.Optional[bool] = None
    hide_replies: t.Optional[bool] = None
    hide_replies_by_like_count: t.Optional[int] = None
    hide_replies_by_unfollowed: t.Optional[bool] = None
    hide_reposts: t.Optional[bool] = None

    py_type: t.Literal['app.bsky.actor.defs#feedViewPref'] = Field(
        default='app.bsky.actor.defs#feedViewPref', alias='$type', frozen=True
    )


class ThreadViewPref(base.ModelBase):
    prioritize_followed_users: t.Optional[bool] = None
    sort: t.Optional[str] = None

    py_type: t.Literal['app.bsky.actor.defs#threadViewPref'] = Field(
        default='app.bsky.actor.defs#threadViewPref', alias='$type', frozen=True
    )


class InterestsPref(base.ModelBase):
    tags: t.List[str] = Field(max_length=100)

    py_type: t.Literal['app.bsky.actor.defs#interestsPref'] = Field(
        default='app.bsky.actor.defs#interestsPref', alias='$type', frozen=True
    )


MutedWordTarget = t.Union[t.Literal['content'], t.Literal['tag']]  #: Muted word target


class MutedWord(base.ModelBase):
    targets: t.List['models.AppBskyActorDefs.MutedWordTarget']
    value: str = Field(max_length=10000)

    py_type: t.Literal['app.bsky.actor.defs#mutedWord'] = Field(
        default='app.bsky.actor.defs#mutedWord', alias='$type', frozen=True
    )


class MutedWordsPref(base.ModelBase):
    items: t.List['models.AppBskyActorDefs.MutedWord']

    py_type: t.Literal['app.bsky.actor.defs#mutedWordsPref'] = Field(
        default='app.bsky.actor.defs#mutedWordsPref', alias='$type', frozen=True
    )


class HiddenPostsPref(base.ModelBase):
    items: t.List[str]

    py_type: t.Literal['app.bsky.actor.defs#hiddenPostsPref'] = Field(
        default='app.bsky.actor.defs#hiddenPostsPref', alias='$type', frozen=True
    )


class LabelersPref(base.ModelBase):
    labelers: t.List['models.AppBskyActorDefs.LabelerPrefItem']

    py_type: t.Literal['app.bsky.actor.defs#labelersPref'] = Field(
        default='app.bsky.actor.defs#labelersPref', alias='$type', frozen=True
    )


class LabelerPrefItem(base.ModelBase):
    did: str

    py_type: t.Literal['app.bsky.actor.defs#labelerPrefItem'] = Field(
        default='app.bsky.actor.defs#labelerPrefItem', alias='$type', frozen=True
    )


class BskyAppStatePref(base.ModelBase):
    active_progress_guide: t.Optional['models.AppBskyActorDefs.BskyAppProgressGuide'] = None
    queued_nudges: t.Optional[t.List[str]] = Field(default=None, max_length=1000)

    py_type: t.Literal['app.bsky.actor.defs#bskyAppStatePref'] = Field(
        default='app.bsky.actor.defs#bskyAppStatePref', alias='$type', frozen=True
    )


class BskyAppProgressGuide(base.ModelBase):
    guide: str = Field(max_length=100)

    py_type: t.Literal['app.bsky.actor.defs#bskyAppProgressGuide'] = Field(
        default='app.bsky.actor.defs#bskyAppProgressGuide', alias='$type', frozen=True
    )
