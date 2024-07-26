import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Params(base.ModelBase):
    """"""

    actor: str


class Response(base.ModelBase):
    all: 'models.ChatBskyModerationGetActorMetadata.Metadata'
    day: 'models.ChatBskyModerationGetActorMetadata.Metadata'
    month: 'models.ChatBskyModerationGetActorMetadata.Metadata'


class Metadata(base.ModelBase):
    convos: int
    convos_started: int
    messages_received: int
    messages_sent: int

    py_type: t.Literal['chat.bsky.moderation.getActorMetadata#metadata'] = Field(
        default='chat.bsky.moderation.getActorMetadata#metadata', alias='$type', frozen=True
    )
