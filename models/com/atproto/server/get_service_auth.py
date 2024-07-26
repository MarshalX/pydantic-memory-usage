from models import base


class Params(base.ModelBase):
    """"""

    aud: str


class Response(base.ModelBase):
    token: str
