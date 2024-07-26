import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class FeedItem(base.ModelBase):
    uri: str

    py_type: t.Literal['app.bsky.graph.starterpack#feedItem'] = Field(
        default='app.bsky.graph.starterpack#feedItem', alias='$type', frozen=True
    )


class Record(base.ModelBase):
    created_at: str
    list: str
    name: str = Field(min_length=1, max_length=500)
    description: t.Optional[str] = Field(default=None, max_length=3000)
    description_facets: t.Optional[t.List['models.AppBskyRichtextFacet.Main']] = None
    feeds: t.Optional[t.List['models.AppBskyGraphStarterpack.FeedItem']] = Field(default=None, max_length=3)

    py_type: t.Literal['app.bsky.graph.starterpack'] = Field(
        default='app.bsky.graph.starterpack', alias='$type', frozen=True
    )
