import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Params(base.ModelBase):
    """"""

    actor: str
    cursor: t.Optional[str] = None
    limit: t.Optional[int] = Field(default=50, ge=1, le=100)


class Response(base.ModelBase):
    starter_packs: t.List['models.AppBskyGraphDefs.StarterPackViewBasic']
    cursor: t.Optional[str] = None
