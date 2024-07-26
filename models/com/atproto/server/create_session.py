import typing as t

if t.TYPE_CHECKING:
    from models.unknown_type import UnknownType
from models import base


class Data(base.ModelBase):
    identifier: str
    password: str
    auth_factor_token: t.Optional[str] = None


class Response(base.ModelBase):
    access_jwt: str
    did: str
    handle: str
    refresh_jwt: str
    active: t.Optional[bool] = None
    did_doc: t.Optional['UnknownType'] = None
    email: t.Optional[str] = None
    email_auth_factor: t.Optional[bool] = None
    email_confirmed: t.Optional[bool] = None
    status: t.Optional[str] = None
