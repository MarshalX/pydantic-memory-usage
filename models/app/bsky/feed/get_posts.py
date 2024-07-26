import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Params(base.ModelBase):
    """"""

    uris: t.List[str] = Field(max_length=25)


class Response(base.ModelBase):
    posts: t.List['models.AppBskyFeedDefs.PostView']
