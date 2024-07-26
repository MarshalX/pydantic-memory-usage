import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Params(base.ModelBase):
    """"""

    q: str
    author: t.Optional[str] = None
    cursor: t.Optional[str] = None
    domain: t.Optional[str] = None
    lang: t.Optional[str] = None
    limit: t.Optional[int] = Field(default=25, ge=1, le=100)
    mentions: t.Optional[str] = None
    since: t.Optional[str] = None
    sort: t.Optional[str] = None
    tag: t.Optional[t.List[str]] = None
    until: t.Optional[str] = None
    url: t.Optional[str] = None


class Response(base.ModelBase):
    posts: t.List['models.AppBskyFeedDefs.PostView']
    cursor: t.Optional[str] = None
    hits_total: t.Optional[int] = None
