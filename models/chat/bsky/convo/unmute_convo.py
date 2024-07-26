import typing as t

if t.TYPE_CHECKING:
    import models
from models import base


class Data(base.ModelBase):
    convo_id: str


class Response(base.ModelBase):
    convo: 'models.ChatBskyConvoDefs.ConvoView'
