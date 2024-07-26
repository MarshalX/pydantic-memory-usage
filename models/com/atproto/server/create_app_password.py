import typing as t

from pydantic import Field

from models import base


class Data(base.ModelBase):
    name: str
    privileged: t.Optional[bool] = None


class AppPassword(base.ModelBase):
    created_at: str
    name: str
    password: str
    privileged: t.Optional[bool] = None

    py_type: t.Literal['com.atproto.server.createAppPassword#appPassword'] = Field(
        default='com.atproto.server.createAppPassword#appPassword', alias='$type', frozen=True
    )
