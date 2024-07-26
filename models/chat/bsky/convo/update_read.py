import typing as t

if t.TYPE_CHECKING:
    import models
from models import base


class Data(base.ModelBase):
    convo_id: str
    message_id: t.Optional[str] = None


class Response(base.ModelBase):
    convo: 'models.ChatBskyConvoDefs.ConvoView'
