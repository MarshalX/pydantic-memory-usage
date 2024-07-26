import typing as t

from pydantic import Field

from models import base


class Record(base.ModelBase):
    created_at: str
    list: str
    subject: str

    py_type: t.Literal['app.bsky.graph.listitem'] = Field(default='app.bsky.graph.listitem', alias='$type', frozen=True)
