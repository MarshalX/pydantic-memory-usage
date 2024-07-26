import typing as t

from models import base


class Data(base.ModelBase):
    actor: str
    allow_access: bool
    ref: t.Optional[str] = None
