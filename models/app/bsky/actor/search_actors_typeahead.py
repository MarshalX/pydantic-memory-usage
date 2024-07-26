import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Params(base.ModelBase):
    """"""

    limit: t.Optional[int] = Field(default=10, ge=1, le=100)
    q: t.Optional[str] = None
    term: t.Optional[str] = None


class Response(base.ModelBase):
    actors: t.List['models.AppBskyActorDefs.ProfileViewBasic']
