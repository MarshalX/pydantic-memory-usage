import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Params(base.ModelBase):
    """"""

    algorithm: t.Optional[str] = None
    cursor: t.Optional[str] = None
    limit: t.Optional[int] = Field(default=50, ge=1, le=100)


class Response(base.ModelBase):
    feed: t.List['models.AppBskyFeedDefs.FeedViewPost']
    cursor: t.Optional[str] = None
