import typing as t

if t.TYPE_CHECKING:
    import models
from models import base


class Data(base.ModelBase):
    convo_id: str
    message: 'models.ChatBskyConvoDefs.MessageInput'
