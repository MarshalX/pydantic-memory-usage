import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Main(base.ModelBase):
    external: 'models.AppBskyEmbedExternal.External'

    py_type: t.Literal['app.bsky.embed.external'] = Field(default='app.bsky.embed.external', alias='$type', frozen=True)


class External(base.ModelBase):
    description: str
    title: str
    uri: str
    thumb: t.Optional[str] = None

    py_type: t.Literal['app.bsky.embed.external#external'] = Field(
        default='app.bsky.embed.external#external', alias='$type', frozen=True
    )


class View(base.ModelBase):
    external: 'models.AppBskyEmbedExternal.ViewExternal'

    py_type: t.Literal['app.bsky.embed.external#view'] = Field(
        default='app.bsky.embed.external#view', alias='$type', frozen=True
    )


class ViewExternal(base.ModelBase):
    description: str
    title: str
    uri: str
    thumb: t.Optional[str] = None

    py_type: t.Literal['app.bsky.embed.external#viewExternal'] = Field(
        default='app.bsky.embed.external#viewExternal', alias='$type', frozen=True
    )
