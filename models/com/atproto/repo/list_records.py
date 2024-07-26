import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
    from models.unknown_type import UnknownType
from models import base


class Params(base.ModelBase):
    """"""

    collection: str
    repo: str
    cursor: t.Optional[str] = None
    limit: t.Optional[int] = Field(default=50, ge=1, le=100)
    reverse: t.Optional[bool] = None
    rkey_end: t.Optional[str] = None
    rkey_start: t.Optional[str] = None


class Response(base.ModelBase):
    records: t.List['models.ComAtprotoRepoListRecords.Record']
    cursor: t.Optional[str] = None


class Record(base.ModelBase):
    cid: str
    uri: str
    value: 'UnknownType'

    py_type: t.Literal['com.atproto.repo.listRecords#record'] = Field(
        default='com.atproto.repo.listRecords#record', alias='$type', frozen=True
    )
