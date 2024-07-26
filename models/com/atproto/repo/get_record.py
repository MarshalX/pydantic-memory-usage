import typing as t

if t.TYPE_CHECKING:
    from models.unknown_type import UnknownType
from models import base


class Params(base.ModelBase):
    """"""

    collection: str
    repo: str
    rkey: str
    cid: t.Optional[str] = None


class Response(base.ModelBase):
    uri: str
    value: 'UnknownType'
    cid: t.Optional[str] = None
