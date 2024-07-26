import typing as t

from models import base


class Data(base.ModelBase):
    use_count: int
    for_account: t.Optional[str] = None


class Response(base.ModelBase):
    code: str
