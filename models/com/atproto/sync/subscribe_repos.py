import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Params(base.ModelBase):
    """"""

    cursor: t.Optional[int] = None


class Commit(base.ModelBase):
    blobs: t.List[str]
    blocks: t.Union[str, bytes]
    commit: str
    ops: t.List['models.ComAtprotoSyncSubscribeRepos.RepoOp'] = Field(max_length=200)
    rebase: bool
    repo: str
    rev: str
    seq: int
    time: str
    too_big: bool
    prev: t.Optional[str] = None
    since: t.Optional[str] = None

    py_type: t.Literal['com.atproto.sync.subscribeRepos#commit'] = Field(
        default='com.atproto.sync.subscribeRepos#commit', alias='$type', frozen=True
    )


class Identity(base.ModelBase):
    did: str
    seq: int
    time: str
    handle: t.Optional[str] = None

    py_type: t.Literal['com.atproto.sync.subscribeRepos#identity'] = Field(
        default='com.atproto.sync.subscribeRepos#identity', alias='$type', frozen=True
    )


class Account(base.ModelBase):
    active: bool
    did: str
    seq: int
    time: str
    status: t.Optional[str] = None

    py_type: t.Literal['com.atproto.sync.subscribeRepos#account'] = Field(
        default='com.atproto.sync.subscribeRepos#account', alias='$type', frozen=True
    )


class Handle(base.ModelBase):
    did: str
    handle: str
    seq: int
    time: str

    py_type: t.Literal['com.atproto.sync.subscribeRepos#handle'] = Field(
        default='com.atproto.sync.subscribeRepos#handle', alias='$type', frozen=True
    )


class Migrate(base.ModelBase):
    did: str
    seq: int
    time: str
    migrate_to: t.Optional[str] = None

    py_type: t.Literal['com.atproto.sync.subscribeRepos#migrate'] = Field(
        default='com.atproto.sync.subscribeRepos#migrate', alias='$type', frozen=True
    )


class Tombstone(base.ModelBase):
    did: str
    seq: int
    time: str

    py_type: t.Literal['com.atproto.sync.subscribeRepos#tombstone'] = Field(
        default='com.atproto.sync.subscribeRepos#tombstone', alias='$type', frozen=True
    )


class Info(base.ModelBase):
    name: str
    message: t.Optional[str] = None

    py_type: t.Literal['com.atproto.sync.subscribeRepos#info'] = Field(
        default='com.atproto.sync.subscribeRepos#info', alias='$type', frozen=True
    )


class RepoOp(base.ModelBase):
    action: str
    path: str
    cid: t.Optional[str] = None

    py_type: t.Literal['com.atproto.sync.subscribeRepos#repoOp'] = Field(
        default='com.atproto.sync.subscribeRepos#repoOp', alias='$type', frozen=True
    )
