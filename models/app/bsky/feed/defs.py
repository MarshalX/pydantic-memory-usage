import typing as t

import typing_extensions as te
from pydantic import Field

if t.TYPE_CHECKING:
    import models
    from models.unknown_type import UnknownType
from models import base


class PostView(base.ModelBase):
    author: 'models.AppBskyActorDefs.ProfileViewBasic'
    cid: str
    indexed_at: str
    record: 'UnknownType'
    uri: str
    embed: t.Optional[
        te.Annotated[
            t.Union[
                'models.AppBskyEmbedImages.View',
                'models.AppBskyEmbedExternal.View',
                'models.AppBskyEmbedRecord.View',
                'models.AppBskyEmbedRecordWithMedia.View',
            ],
            Field(default=None, discriminator='py_type'),
        ]
    ] = None
    labels: t.Optional[t.List['models.ComAtprotoLabelDefs.Label']] = None
    like_count: t.Optional[int] = None
    reply_count: t.Optional[int] = None
    repost_count: t.Optional[int] = None
    threadgate: t.Optional['models.AppBskyFeedDefs.ThreadgateView'] = None
    viewer: t.Optional['models.AppBskyFeedDefs.ViewerState'] = None

    py_type: t.Literal['app.bsky.feed.defs#postView'] = Field(
        default='app.bsky.feed.defs#postView', alias='$type', frozen=True
    )


class ViewerState(base.ModelBase):
    like: t.Optional[str] = None
    reply_disabled: t.Optional[bool] = None
    repost: t.Optional[str] = None
    thread_muted: t.Optional[bool] = None

    py_type: t.Literal['app.bsky.feed.defs#viewerState'] = Field(
        default='app.bsky.feed.defs#viewerState', alias='$type', frozen=True
    )


class FeedViewPost(base.ModelBase):
    post: 'models.AppBskyFeedDefs.PostView'
    feed_context: t.Optional[str] = Field(default=None, max_length=2000)
    reason: t.Optional[
        te.Annotated[t.Union['models.AppBskyFeedDefs.ReasonRepost'], Field(default=None, discriminator='py_type')]
    ] = None
    reply: t.Optional['models.AppBskyFeedDefs.ReplyRef'] = None

    py_type: t.Literal['app.bsky.feed.defs#feedViewPost'] = Field(
        default='app.bsky.feed.defs#feedViewPost', alias='$type', frozen=True
    )


class ReplyRef(base.ModelBase):
    parent: te.Annotated[
        t.Union[
            'models.AppBskyFeedDefs.PostView',
            'models.AppBskyFeedDefs.NotFoundPost',
            'models.AppBskyFeedDefs.BlockedPost',
        ],
        Field(discriminator='py_type'),
    ]
    root: te.Annotated[
        t.Union[
            'models.AppBskyFeedDefs.PostView',
            'models.AppBskyFeedDefs.NotFoundPost',
            'models.AppBskyFeedDefs.BlockedPost',
        ],
        Field(discriminator='py_type'),
    ]
    grandparent_author: t.Optional['models.AppBskyActorDefs.ProfileViewBasic'] = None

    py_type: t.Literal['app.bsky.feed.defs#replyRef'] = Field(
        default='app.bsky.feed.defs#replyRef', alias='$type', frozen=True
    )


class ReasonRepost(base.ModelBase):
    by: 'models.AppBskyActorDefs.ProfileViewBasic'
    indexed_at: str

    py_type: t.Literal['app.bsky.feed.defs#reasonRepost'] = Field(
        default='app.bsky.feed.defs#reasonRepost', alias='$type', frozen=True
    )


class ThreadViewPost(base.ModelBase):
    post: 'models.AppBskyFeedDefs.PostView'
    parent: t.Optional[
        te.Annotated[
            t.Union[
                'models.AppBskyFeedDefs.ThreadViewPost',
                'models.AppBskyFeedDefs.NotFoundPost',
                'models.AppBskyFeedDefs.BlockedPost',
            ],
            Field(default=None, discriminator='py_type'),
        ]
    ] = None
    replies: t.Optional[
        t.List[
            te.Annotated[
                t.Union[
                    'models.AppBskyFeedDefs.ThreadViewPost',
                    'models.AppBskyFeedDefs.NotFoundPost',
                    'models.AppBskyFeedDefs.BlockedPost',
                ],
                Field(discriminator='py_type'),
            ]
        ]
    ] = None

    py_type: t.Literal['app.bsky.feed.defs#threadViewPost'] = Field(
        default='app.bsky.feed.defs#threadViewPost', alias='$type', frozen=True
    )


class NotFoundPost(base.ModelBase):
    not_found: bool = Field(frozen=True)
    uri: str

    py_type: t.Literal['app.bsky.feed.defs#notFoundPost'] = Field(
        default='app.bsky.feed.defs#notFoundPost', alias='$type', frozen=True
    )


class BlockedPost(base.ModelBase):
    author: 'models.AppBskyFeedDefs.BlockedAuthor'
    blocked: bool = Field(frozen=True)
    uri: str

    py_type: t.Literal['app.bsky.feed.defs#blockedPost'] = Field(
        default='app.bsky.feed.defs#blockedPost', alias='$type', frozen=True
    )


class BlockedAuthor(base.ModelBase):
    did: str
    viewer: t.Optional['models.AppBskyActorDefs.ViewerState'] = None

    py_type: t.Literal['app.bsky.feed.defs#blockedAuthor'] = Field(
        default='app.bsky.feed.defs#blockedAuthor', alias='$type', frozen=True
    )


class GeneratorView(base.ModelBase):
    cid: str
    creator: 'models.AppBskyActorDefs.ProfileView'
    did: str
    display_name: str
    indexed_at: str
    uri: str
    accepts_interactions: t.Optional[bool] = None
    avatar: t.Optional[str] = None
    description: t.Optional[str] = Field(default=None, max_length=3000)
    description_facets: t.Optional[t.List['models.AppBskyRichtextFacet.Main']] = None
    labels: t.Optional[t.List['models.ComAtprotoLabelDefs.Label']] = None
    like_count: t.Optional[int] = Field(default=None, ge=0)
    viewer: t.Optional['models.AppBskyFeedDefs.GeneratorViewerState'] = None

    py_type: t.Literal['app.bsky.feed.defs#generatorView'] = Field(
        default='app.bsky.feed.defs#generatorView', alias='$type', frozen=True
    )


class GeneratorViewerState(base.ModelBase):
    like: t.Optional[str] = None

    py_type: t.Literal['app.bsky.feed.defs#generatorViewerState'] = Field(
        default='app.bsky.feed.defs#generatorViewerState', alias='$type', frozen=True
    )


class SkeletonFeedPost(base.ModelBase):
    post: str
    feed_context: t.Optional[str] = Field(default=None, max_length=2000)
    reason: t.Optional[
        te.Annotated[
            t.Union['models.AppBskyFeedDefs.SkeletonReasonRepost'], Field(default=None, discriminator='py_type')
        ]
    ] = None

    py_type: t.Literal['app.bsky.feed.defs#skeletonFeedPost'] = Field(
        default='app.bsky.feed.defs#skeletonFeedPost', alias='$type', frozen=True
    )


class SkeletonReasonRepost(base.ModelBase):
    repost: str

    py_type: t.Literal['app.bsky.feed.defs#skeletonReasonRepost'] = Field(
        default='app.bsky.feed.defs#skeletonReasonRepost', alias='$type', frozen=True
    )


class ThreadgateView(base.ModelBase):
    cid: t.Optional[str] = None
    lists: t.Optional[t.List['models.AppBskyGraphDefs.ListViewBasic']] = None
    record: t.Optional['UnknownType'] = None
    uri: t.Optional[str] = None

    py_type: t.Literal['app.bsky.feed.defs#threadgateView'] = Field(
        default='app.bsky.feed.defs#threadgateView', alias='$type', frozen=True
    )


class Interaction(base.ModelBase):
    event: t.Optional[str] = None
    feed_context: t.Optional[str] = Field(default=None, max_length=2000)
    item: t.Optional[str] = None

    py_type: t.Literal['app.bsky.feed.defs#interaction'] = Field(
        default='app.bsky.feed.defs#interaction', alias='$type', frozen=True
    )


RequestLess = t.Literal[
    'app.bsky.feed.defs#requestLess'
]  #: Request that less content like the given feed item be shown in the feed

RequestMore = t.Literal[
    'app.bsky.feed.defs#requestMore'
]  #: Request that more content like the given feed item be shown in the feed

ClickthroughItem = t.Literal['app.bsky.feed.defs#clickthroughItem']  #: User clicked through to the feed item

ClickthroughAuthor = t.Literal[
    'app.bsky.feed.defs#clickthroughAuthor'
]  #: User clicked through to the author of the feed item

ClickthroughReposter = t.Literal[
    'app.bsky.feed.defs#clickthroughReposter'
]  #: User clicked through to the reposter of the feed item

ClickthroughEmbed = t.Literal[
    'app.bsky.feed.defs#clickthroughEmbed'
]  #: User clicked through to the embedded content of the feed item

InteractionSeen = t.Literal['app.bsky.feed.defs#interactionSeen']  #: Feed item was seen by user

InteractionLike = t.Literal['app.bsky.feed.defs#interactionLike']  #: User liked the feed item

InteractionRepost = t.Literal['app.bsky.feed.defs#interactionRepost']  #: User reposted the feed item

InteractionReply = t.Literal['app.bsky.feed.defs#interactionReply']  #: User replied to the feed item

InteractionQuote = t.Literal['app.bsky.feed.defs#interactionQuote']  #: User quoted the feed item

InteractionShare = t.Literal['app.bsky.feed.defs#interactionShare']  #: User shared the feed item
