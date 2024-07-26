import typing as t

from models import base


class Params(base.ModelBase):
    """"""

    priority: t.Optional[bool] = None
    seen_at: t.Optional[str] = None


class Response(base.ModelBase):
    count: int
