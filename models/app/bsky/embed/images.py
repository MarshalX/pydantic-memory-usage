import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Main(base.ModelBase):
    images: t.List['models.AppBskyEmbedImages.Image'] = Field(max_length=4)

    py_type: t.Literal['app.bsky.embed.images'] = Field(default='app.bsky.embed.images', alias='$type', frozen=True)


class Image(base.ModelBase):
    alt: str
    image: str
    aspect_ratio: t.Optional['models.AppBskyEmbedImages.AspectRatio'] = None

    py_type: t.Literal['app.bsky.embed.images#image'] = Field(
        default='app.bsky.embed.images#image', alias='$type', frozen=True
    )


class AspectRatio(base.ModelBase):
    height: int = Field(ge=1)
    width: int = Field(ge=1)

    py_type: t.Literal['app.bsky.embed.images#aspectRatio'] = Field(
        default='app.bsky.embed.images#aspectRatio', alias='$type', frozen=True
    )


class View(base.ModelBase):
    images: t.List['models.AppBskyEmbedImages.ViewImage'] = Field(max_length=4)

    py_type: t.Literal['app.bsky.embed.images#view'] = Field(
        default='app.bsky.embed.images#view', alias='$type', frozen=True
    )


class ViewImage(base.ModelBase):
    alt: str
    fullsize: str
    thumb: str
    aspect_ratio: t.Optional['models.AppBskyEmbedImages.AspectRatio'] = None

    py_type: t.Literal['app.bsky.embed.images#viewImage'] = Field(
        default='app.bsky.embed.images#viewImage', alias='$type', frozen=True
    )
