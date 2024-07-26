import typing as t

from models import base


class Data(base.ModelBase):
    did: str
    disabled: t.Optional[bool] = None
    role: t.Optional[str] = None
