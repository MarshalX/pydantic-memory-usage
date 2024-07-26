import typing as t

if t.TYPE_CHECKING:
    from models.unknown_type import UnknownInputType, UnknownType
from models import base


class Data(base.ModelBase):
    handle: str
    did: t.Optional[str] = None
    email: t.Optional[str] = None
    invite_code: t.Optional[str] = None
    password: t.Optional[str] = None
    plc_op: t.Optional['UnknownInputType'] = None
    recovery_key: t.Optional[str] = None
    verification_code: t.Optional[str] = None
    verification_phone: t.Optional[str] = None


class Response(base.ModelBase):
    access_jwt: str
    did: str
    handle: str
    refresh_jwt: str
    did_doc: t.Optional['UnknownType'] = None
