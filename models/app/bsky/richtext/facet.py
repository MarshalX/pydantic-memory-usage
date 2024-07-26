import typing as t

import typing_extensions as te
from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Main(base.ModelBase):
    features: t.List[
        te.Annotated[
            t.Union[
                'models.AppBskyRichtextFacet.Mention',
                'models.AppBskyRichtextFacet.Link',
                'models.AppBskyRichtextFacet.Tag',
            ],
            Field(discriminator='py_type'),
        ]
    ]
    index: 'models.AppBskyRichtextFacet.ByteSlice'

    py_type: t.Literal['app.bsky.richtext.facet'] = Field(default='app.bsky.richtext.facet', alias='$type', frozen=True)


class Mention(base.ModelBase):
    did: str

    py_type: t.Literal['app.bsky.richtext.facet#mention'] = Field(
        default='app.bsky.richtext.facet#mention', alias='$type', frozen=True
    )


class Link(base.ModelBase):
    uri: str

    py_type: t.Literal['app.bsky.richtext.facet#link'] = Field(
        default='app.bsky.richtext.facet#link', alias='$type', frozen=True
    )


class Tag(base.ModelBase):
    tag: str = Field(max_length=640)

    py_type: t.Literal['app.bsky.richtext.facet#tag'] = Field(
        default='app.bsky.richtext.facet#tag', alias='$type', frozen=True
    )


class ByteSlice(base.ModelBase):
    byte_end: int = Field(ge=0)
    byte_start: int = Field(ge=0)

    py_type: t.Literal['app.bsky.richtext.facet#byteSlice'] = Field(
        default='app.bsky.richtext.facet#byteSlice', alias='$type', frozen=True
    )
