import typing as t

from pydantic import Field

from models import base


class Record(base.ModelBase):
    allow_incoming: str

    py_type: t.Literal['chat.bsky.actor.declaration'] = Field(
        default='chat.bsky.actor.declaration', alias='$type', frozen=True
    )
