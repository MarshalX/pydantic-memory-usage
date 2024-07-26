import typing as t

if t.TYPE_CHECKING:
    from models.unknown_type import UnknownType
from models import base


class Response(base.ModelBase):
    access_jwt: str
    did: str
    handle: str
    refresh_jwt: str
    active: t.Optional[bool] = None
    did_doc: t.Optional['UnknownType'] = None
    status: t.Optional[str] = None
