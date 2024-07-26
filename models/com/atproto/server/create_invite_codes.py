import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Data(base.ModelBase):
    code_count: int = None
    use_count: int
    for_accounts: t.Optional[t.List[str]] = None


class Response(base.ModelBase):
    codes: t.List['models.ComAtprotoServerCreateInviteCodes.AccountCodes']


class AccountCodes(base.ModelBase):
    account: str
    codes: t.List[str]

    py_type: t.Literal['com.atproto.server.createInviteCodes#accountCodes'] = Field(
        default='com.atproto.server.createInviteCodes#accountCodes', alias='$type', frozen=True
    )
