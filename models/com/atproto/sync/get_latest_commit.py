from models import base


class Params(base.ModelBase):
    """"""

    did: str


class Response(base.ModelBase):
    cid: str
    rev: str
