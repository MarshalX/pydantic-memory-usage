import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Params(base.ModelBase):
    """"""

    cursor: t.Optional[str] = None
    limit: t.Optional[int] = Field(default=500, ge=1, le=1000)


class Response(base.ModelBase):
    blobs: t.List['models.ComAtprotoRepoListMissingBlobs.RecordBlob']
    cursor: t.Optional[str] = None


class RecordBlob(base.ModelBase):
    cid: str
    record_uri: str

    py_type: t.Literal['com.atproto.repo.listMissingBlobs#recordBlob'] = Field(
        default='com.atproto.repo.listMissingBlobs#recordBlob', alias='$type', frozen=True
    )
