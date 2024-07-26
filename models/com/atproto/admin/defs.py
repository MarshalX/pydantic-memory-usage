import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
    from models.unknown_type import UnknownType
from models import base


class StatusAttr(base.ModelBase):
    applied: bool
    ref: t.Optional[str] = None

    py_type: t.Literal['com.atproto.admin.defs#statusAttr'] = Field(
        default='com.atproto.admin.defs#statusAttr', alias='$type', frozen=True
    )


class AccountView(base.ModelBase):
    did: str
    handle: str
    indexed_at: str
    deactivated_at: t.Optional[str] = None
    email: t.Optional[str] = None
    email_confirmed_at: t.Optional[str] = None
    invite_note: t.Optional[str] = None
    invited_by: t.Optional['models.ComAtprotoServerDefs.InviteCode'] = None
    invites: t.Optional[t.List['models.ComAtprotoServerDefs.InviteCode']] = None
    invites_disabled: t.Optional[bool] = None
    related_records: t.Optional[t.List['UnknownType']] = None

    py_type: t.Literal['com.atproto.admin.defs#accountView'] = Field(
        default='com.atproto.admin.defs#accountView', alias='$type', frozen=True
    )


class RepoRef(base.ModelBase):
    did: str

    py_type: t.Literal['com.atproto.admin.defs#repoRef'] = Field(
        default='com.atproto.admin.defs#repoRef', alias='$type', frozen=True
    )


class RepoBlobRef(base.ModelBase):
    cid: str
    did: str
    record_uri: t.Optional[str] = None

    py_type: t.Literal['com.atproto.admin.defs#repoBlobRef'] = Field(
        default='com.atproto.admin.defs#repoBlobRef', alias='$type', frozen=True
    )
