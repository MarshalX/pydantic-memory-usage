from models import base


class Data(base.ModelBase):
    convo_id: str


class Response(base.ModelBase):
    convo_id: str
    rev: str
