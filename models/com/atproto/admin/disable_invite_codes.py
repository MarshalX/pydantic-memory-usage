import typing as t

from models import base


class Data(base.ModelBase):
    accounts: t.Optional[t.List[str]] = None
    codes: t.Optional[t.List[str]] = None
