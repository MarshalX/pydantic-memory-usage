import typing as t

import typing_extensions as te
from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Main(base.ModelBase):
    media: te.Annotated[
        t.Union['models.AppBskyEmbedImages.Main', 'models.AppBskyEmbedExternal.Main'], Field(discriminator='py_type')
    ]
    record: 'models.AppBskyEmbedRecord.Main'

    py_type: t.Literal['app.bsky.embed.recordWithMedia'] = Field(
        default='app.bsky.embed.recordWithMedia', alias='$type', frozen=True
    )


class View(base.ModelBase):
    media: te.Annotated[
        t.Union['models.AppBskyEmbedImages.View', 'models.AppBskyEmbedExternal.View'], Field(discriminator='py_type')
    ]
    record: 'models.AppBskyEmbedRecord.View'

    py_type: t.Literal['app.bsky.embed.recordWithMedia#view'] = Field(
        default='app.bsky.embed.recordWithMedia#view', alias='$type', frozen=True
    )
