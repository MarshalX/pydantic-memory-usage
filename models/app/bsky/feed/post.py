import typing as t

import typing_extensions as te
from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class ReplyRef(base.ModelBase):
    parent: 'models.ComAtprotoRepoStrongRef.Main'
    root: 'models.ComAtprotoRepoStrongRef.Main'

    py_type: t.Literal['app.bsky.feed.post#replyRef'] = Field(
        default='app.bsky.feed.post#replyRef', alias='$type', frozen=True
    )


class Entity(base.ModelBase):
    index: 'models.AppBskyFeedPost.TextSlice'
    type: str
    value: str

    py_type: t.Literal['app.bsky.feed.post#entity'] = Field(
        default='app.bsky.feed.post#entity', alias='$type', frozen=True
    )


class TextSlice(base.ModelBase):
    end: int = Field(ge=0)
    start: int = Field(ge=0)

    py_type: t.Literal['app.bsky.feed.post#textSlice'] = Field(
        default='app.bsky.feed.post#textSlice', alias='$type', frozen=True
    )


class Record(base.ModelBase):
    created_at: str
    text: str = Field(max_length=3000)
    embed: t.Optional[
        te.Annotated[
            t.Union[
                'models.AppBskyEmbedImages.Main',
                'models.AppBskyEmbedExternal.Main',
                'models.AppBskyEmbedRecord.Main',
                'models.AppBskyEmbedRecordWithMedia.Main',
            ],
            Field(default=None, discriminator='py_type'),
        ]
    ] = None
    entities: t.Optional[t.List['models.AppBskyFeedPost.Entity']] = None
    facets: t.Optional[t.List['models.AppBskyRichtextFacet.Main']] = None
    labels: t.Optional[
        te.Annotated[t.Union['models.ComAtprotoLabelDefs.SelfLabels'], Field(default=None, discriminator='py_type')]
    ] = None
    langs: t.Optional[t.List[str]] = Field(default=None, max_length=3)
    reply: t.Optional['models.AppBskyFeedPost.ReplyRef'] = None
    tags: t.Optional[t.List[str]] = Field(default=None, max_length=8)

    py_type: t.Literal['app.bsky.feed.post'] = Field(default='app.bsky.feed.post', alias='$type', frozen=True)
