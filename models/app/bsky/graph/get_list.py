import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Params(base.ModelBase):
    """"""

    list: str
    cursor: t.Optional[str] = None
    limit: t.Optional[int] = Field(default=50, ge=1, le=100)


class Response(base.ModelBase):
    items: t.List['models.AppBskyGraphDefs.ListItemView']
    list: 'models.AppBskyGraphDefs.ListView'
    cursor: t.Optional[str] = None
