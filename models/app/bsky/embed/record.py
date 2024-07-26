import typing as t

import typing_extensions as te
from pydantic import Field

if t.TYPE_CHECKING:
    import models
    from models.unknown_type import UnknownType
from models import base


class Main(base.ModelBase):
    record: 'models.ComAtprotoRepoStrongRef.Main'

    py_type: t.Literal['app.bsky.embed.record'] = Field(default='app.bsky.embed.record', alias='$type', frozen=True)


class View(base.ModelBase):
    record: te.Annotated[
        t.Union[
            'models.AppBskyEmbedRecord.ViewRecord',
            'models.AppBskyEmbedRecord.ViewNotFound',
            'models.AppBskyEmbedRecord.ViewBlocked',
            'models.AppBskyFeedDefs.GeneratorView',
            'models.AppBskyGraphDefs.ListView',
            'models.AppBskyLabelerDefs.LabelerView',
            'models.AppBskyGraphDefs.StarterPackViewBasic',
        ],
        Field(discriminator='py_type'),
    ]

    py_type: t.Literal['app.bsky.embed.record#view'] = Field(
        default='app.bsky.embed.record#view', alias='$type', frozen=True
    )


class ViewRecord(base.ModelBase):
    author: 'models.AppBskyActorDefs.ProfileViewBasic'
    cid: str
    indexed_at: str
    uri: str
    value: 'UnknownType'
    embeds: t.Optional[
        t.List[
            te.Annotated[
                t.Union[
                    'models.AppBskyEmbedImages.View',
                    'models.AppBskyEmbedExternal.View',
                    'models.AppBskyEmbedRecord.View',
                    'models.AppBskyEmbedRecordWithMedia.View',
                ],
                Field(discriminator='py_type'),
            ]
        ]
    ] = None
    labels: t.Optional[t.List['models.ComAtprotoLabelDefs.Label']] = None
    like_count: t.Optional[int] = None
    reply_count: t.Optional[int] = None
    repost_count: t.Optional[int] = None

    py_type: t.Literal['app.bsky.embed.record#viewRecord'] = Field(
        default='app.bsky.embed.record#viewRecord', alias='$type', frozen=True
    )


class ViewNotFound(base.ModelBase):
    not_found: bool = Field(frozen=True)
    uri: str

    py_type: t.Literal['app.bsky.embed.record#viewNotFound'] = Field(
        default='app.bsky.embed.record#viewNotFound', alias='$type', frozen=True
    )


class ViewBlocked(base.ModelBase):
    author: 'models.AppBskyFeedDefs.BlockedAuthor'
    blocked: bool = Field(frozen=True)
    uri: str

    py_type: t.Literal['app.bsky.embed.record#viewBlocked'] = Field(
        default='app.bsky.embed.record#viewBlocked', alias='$type', frozen=True
    )
