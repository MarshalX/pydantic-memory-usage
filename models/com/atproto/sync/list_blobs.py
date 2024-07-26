import typing as t

from pydantic import Field

from models import base


class Params(base.ModelBase):
    """"""

    did: str
    cursor: t.Optional[str] = None
    limit: t.Optional[int] = Field(default=500, ge=1, le=1000)
    since: t.Optional[str] = None


class Response(base.ModelBase):
    cids: t.List[str]
    cursor: t.Optional[str] = None
