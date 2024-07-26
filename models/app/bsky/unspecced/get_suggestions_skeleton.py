import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Params(base.ModelBase):
    """"""

    cursor: t.Optional[str] = None
    limit: t.Optional[int] = Field(default=50, ge=1, le=100)
    relative_to_did: t.Optional[str] = None
    viewer: t.Optional[str] = None


class Response(base.ModelBase):
    actors: t.List['models.AppBskyUnspeccedDefs.SkeletonSearchActor']
    cursor: t.Optional[str] = None
