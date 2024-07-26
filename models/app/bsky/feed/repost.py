import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Record(base.ModelBase):
    created_at: str
    subject: 'models.ComAtprotoRepoStrongRef.Main'

    py_type: t.Literal['app.bsky.feed.repost'] = Field(default='app.bsky.feed.repost', alias='$type', frozen=True)
