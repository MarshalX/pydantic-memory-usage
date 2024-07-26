import typing as t

from pydantic import Field

from models import base


class Record(base.ModelBase):
    created_at: str
    subject: str

    py_type: t.Literal['app.bsky.graph.block'] = Field(default='app.bsky.graph.block', alias='$type', frozen=True)
