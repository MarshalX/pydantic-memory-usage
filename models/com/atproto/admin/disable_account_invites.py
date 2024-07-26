import typing as t

from models import base


class Data(base.ModelBase):
    account: str
    note: t.Optional[str] = None
