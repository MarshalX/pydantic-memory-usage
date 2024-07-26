import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Response(base.ModelBase):
    passwords: t.List['models.ComAtprotoServerListAppPasswords.AppPassword']


class AppPassword(base.ModelBase):
    created_at: str
    name: str
    privileged: t.Optional[bool] = None

    py_type: t.Literal['com.atproto.server.listAppPasswords#appPassword'] = Field(
        default='com.atproto.server.listAppPasswords#appPassword', alias='$type', frozen=True
    )
