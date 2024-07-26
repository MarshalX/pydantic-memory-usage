import typing as t

from models import base


class Data(base.ModelBase):
    did: t.Optional[str] = None


class Response(base.ModelBase):
    signing_key: str
