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
    repos: t.List['models.ComAtprotoSyncListRepos.Repo']
    cursor: t.Optional[str] = None


class Repo(base.ModelBase):
    did: str
    head: str
    rev: str
    active: t.Optional[bool] = None
    status: t.Optional[str] = None

    py_type: t.Literal['com.atproto.sync.listRepos#repo'] = Field(
        default='com.atproto.sync.listRepos#repo', alias='$type', frozen=True
    )
