import typing as t

from pydantic import Field

from models import base


class Record(base.ModelBase):
    created_at: str
    subject: str

    py_type: t.Literal['app.bsky.graph.listblock'] = Field(
        default='app.bsky.graph.listblock', alias='$type', frozen=True
    )
