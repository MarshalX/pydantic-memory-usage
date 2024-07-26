import typing as t

import typing_extensions as te
from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class MessageRef(base.ModelBase):
    convo_id: str
    did: str
    message_id: str

    py_type: t.Literal['chat.bsky.convo.defs#messageRef'] = Field(
        default='chat.bsky.convo.defs#messageRef', alias='$type', frozen=True
    )


class MessageInput(base.ModelBase):
    text: str = Field(max_length=10000)
    embed: t.Optional[
        te.Annotated[t.Union['models.AppBskyEmbedRecord.Main'], Field(default=None, discriminator='py_type')]
    ] = None
    facets: t.Optional[t.List['models.AppBskyRichtextFacet.Main']] = None

    py_type: t.Literal['chat.bsky.convo.defs#messageInput'] = Field(
        default='chat.bsky.convo.defs#messageInput', alias='$type', frozen=True
    )


class MessageView(base.ModelBase):
    id: str
    rev: str
    sender: 'models.ChatBskyConvoDefs.MessageViewSender'
    sent_at: str
    text: str = Field(max_length=10000)
    embed: t.Optional[
        te.Annotated[t.Union['models.AppBskyEmbedRecord.View'], Field(default=None, discriminator='py_type')]
    ] = None
    facets: t.Optional[t.List['models.AppBskyRichtextFacet.Main']] = None

    py_type: t.Literal['chat.bsky.convo.defs#messageView'] = Field(
        default='chat.bsky.convo.defs#messageView', alias='$type', frozen=True
    )


class DeletedMessageView(base.ModelBase):
    id: str
    rev: str
    sender: 'models.ChatBskyConvoDefs.MessageViewSender'
    sent_at: str

    py_type: t.Literal['chat.bsky.convo.defs#deletedMessageView'] = Field(
        default='chat.bsky.convo.defs#deletedMessageView', alias='$type', frozen=True
    )


class MessageViewSender(base.ModelBase):
    did: str

    py_type: t.Literal['chat.bsky.convo.defs#messageViewSender'] = Field(
        default='chat.bsky.convo.defs#messageViewSender', alias='$type', frozen=True
    )


class ConvoView(base.ModelBase):
    id: str
    members: t.List['models.ChatBskyActorDefs.ProfileViewBasic']
    muted: bool
    rev: str
    unread_count: int
    last_message: t.Optional[
        te.Annotated[
            t.Union['models.ChatBskyConvoDefs.MessageView', 'models.ChatBskyConvoDefs.DeletedMessageView'],
            Field(default=None, discriminator='py_type'),
        ]
    ] = None

    py_type: t.Literal['chat.bsky.convo.defs#convoView'] = Field(
        default='chat.bsky.convo.defs#convoView', alias='$type', frozen=True
    )


class LogBeginConvo(base.ModelBase):
    convo_id: str
    rev: str

    py_type: t.Literal['chat.bsky.convo.defs#logBeginConvo'] = Field(
        default='chat.bsky.convo.defs#logBeginConvo', alias='$type', frozen=True
    )


class LogLeaveConvo(base.ModelBase):
    convo_id: str
    rev: str

    py_type: t.Literal['chat.bsky.convo.defs#logLeaveConvo'] = Field(
        default='chat.bsky.convo.defs#logLeaveConvo', alias='$type', frozen=True
    )


class LogCreateMessage(base.ModelBase):
    convo_id: str
    message: te.Annotated[
        t.Union['models.ChatBskyConvoDefs.MessageView', 'models.ChatBskyConvoDefs.DeletedMessageView'],
        Field(discriminator='py_type'),
    ]
    rev: str

    py_type: t.Literal['chat.bsky.convo.defs#logCreateMessage'] = Field(
        default='chat.bsky.convo.defs#logCreateMessage', alias='$type', frozen=True
    )


class LogDeleteMessage(base.ModelBase):
    convo_id: str
    message: te.Annotated[
        t.Union['models.ChatBskyConvoDefs.MessageView', 'models.ChatBskyConvoDefs.DeletedMessageView'],
        Field(discriminator='py_type'),
    ]
    rev: str

    py_type: t.Literal['chat.bsky.convo.defs#logDeleteMessage'] = Field(
        default='chat.bsky.convo.defs#logDeleteMessage', alias='$type', frozen=True
    )
