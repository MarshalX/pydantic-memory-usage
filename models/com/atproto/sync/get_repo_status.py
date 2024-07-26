import typing as t

from models import base


class Params(base.ModelBase):
    """"""

    did: str


class Response(base.ModelBase):
    active: bool
    did: str
    rev: t.Optional[str] = None
    status: t.Optional[str] = None
