import typing as t

from models import base


class Params(base.ModelBase):
    """"""

    uri: str
    cid: t.Optional[str] = None
