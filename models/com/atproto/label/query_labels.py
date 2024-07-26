import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Params(base.ModelBase):
    """"""

    uri_patterns: t.List[str]
    cursor: t.Optional[str] = None
    limit: t.Optional[int] = Field(default=50, ge=1, le=250)
    sources: t.Optional[t.List[str]] = None


class Response(base.ModelBase):
    labels: t.List['models.ComAtprotoLabelDefs.Label']
    cursor: t.Optional[str] = None
