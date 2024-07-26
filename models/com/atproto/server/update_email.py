import typing as t

from models import base


class Data(base.ModelBase):
    email: str
    email_auth_factor: t.Optional[bool] = None
    token: t.Optional[str] = None
