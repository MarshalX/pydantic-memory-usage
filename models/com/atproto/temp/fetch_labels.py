import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Params(base.ModelBase):
    """"""

    limit: t.Optional[int] = Field(default=50, ge=1, le=250)
    since: t.Optional[int] = None


class Response(base.ModelBase):
    labels: t.List['models.ComAtprotoLabelDefs.Label']
