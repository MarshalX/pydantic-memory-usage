import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Params(base.ModelBase):
    """"""

    uri: str
    cid: t.Optional[str] = None
    cursor: t.Optional[str] = None
    limit: t.Optional[int] = Field(default=50, ge=1, le=100)


class Response(base.ModelBase):
    likes: t.List['models.AppBskyFeedGetLikes.Like']
    uri: str
    cid: t.Optional[str] = None
    cursor: t.Optional[str] = None


class Like(base.ModelBase):
    actor: 'models.AppBskyActorDefs.ProfileView'
    created_at: str
    indexed_at: str

    py_type: t.Literal['app.bsky.feed.getLikes#like'] = Field(
        default='app.bsky.feed.getLikes#like', alias='$type', frozen=True
    )
