import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
    from models.unknown_type import UnknownType
from models import base


class Params(base.ModelBase):
    """"""

    cursor: t.Optional[str] = None
    limit: t.Optional[int] = Field(default=50, ge=1, le=100)
    priority: t.Optional[bool] = None
    seen_at: t.Optional[str] = None


class Response(base.ModelBase):
    notifications: t.List['models.AppBskyNotificationListNotifications.Notification']
    cursor: t.Optional[str] = None
    priority: t.Optional[bool] = None
    seen_at: t.Optional[str] = None


class Notification(base.ModelBase):
    author: 'models.AppBskyActorDefs.ProfileView'
    cid: str
    indexed_at: str
    is_read: bool
    reason: str
    record: 'UnknownType'
    uri: str
    labels: t.Optional[t.List['models.ComAtprotoLabelDefs.Label']] = None
    reason_subject: t.Optional[str] = None

    py_type: t.Literal['app.bsky.notification.listNotifications#notification'] = Field(
        default='app.bsky.notification.listNotifications#notification', alias='$type', frozen=True
    )
