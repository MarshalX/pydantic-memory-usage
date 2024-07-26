import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class InviteCode(base.ModelBase):
    available: int
    code: str
    created_at: str
    created_by: str
    disabled: bool
    for_account: str
    uses: t.List['models.ComAtprotoServerDefs.InviteCodeUse']

    py_type: t.Literal['com.atproto.server.defs#inviteCode'] = Field(
        default='com.atproto.server.defs#inviteCode', alias='$type', frozen=True
    )


class InviteCodeUse(base.ModelBase):
    used_at: str
    used_by: str

    py_type: t.Literal['com.atproto.server.defs#inviteCodeUse'] = Field(
        default='com.atproto.server.defs#inviteCodeUse', alias='$type', frozen=True
    )
