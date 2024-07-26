import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Data(base.ModelBase):
    items: t.List['models.ChatBskyConvoSendMessageBatch.BatchItem'] = Field(max_length=100)


class Response(base.ModelBase):
    items: t.List['models.ChatBskyConvoDefs.MessageView']


class BatchItem(base.ModelBase):
    convo_id: str
    message: 'models.ChatBskyConvoDefs.MessageInput'

    py_type: t.Literal['chat.bsky.convo.sendMessageBatch#batchItem'] = Field(
        default='chat.bsky.convo.sendMessageBatch#batchItem', alias='$type', frozen=True
    )
