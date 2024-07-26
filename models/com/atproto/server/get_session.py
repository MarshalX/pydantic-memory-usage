import typing as t

if t.TYPE_CHECKING:
    from models.unknown_type import UnknownType
from models import base


class Response(base.ModelBase):
    did: str
    handle: str
    active: t.Optional[bool] = None
    did_doc: t.Optional['UnknownType'] = None
    email: t.Optional[str] = None
    email_auth_factor: t.Optional[bool] = None
    email_confirmed: t.Optional[bool] = None
    status: t.Optional[str] = None
