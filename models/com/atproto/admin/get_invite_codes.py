import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Params(base.ModelBase):
    """"""

    cursor: t.Optional[str] = None
    limit: t.Optional[int] = Field(default=100, ge=1, le=500)
    sort: t.Optional[str] = None


class Response(base.ModelBase):
    codes: t.List['models.ComAtprotoServerDefs.InviteCode']
    cursor: t.Optional[str] = None
