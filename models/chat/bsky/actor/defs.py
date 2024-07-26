import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class ProfileViewBasic(base.ModelBase):
    did: str
    handle: str
    associated: t.Optional['models.AppBskyActorDefs.ProfileAssociated'] = None
    avatar: t.Optional[str] = None
    chat_disabled: t.Optional[bool] = None
    display_name: t.Optional[str] = Field(default=None, max_length=640)
    labels: t.Optional[t.List['models.ComAtprotoLabelDefs.Label']] = None
    viewer: t.Optional['models.AppBskyActorDefs.ViewerState'] = None

    py_type: t.Literal['chat.bsky.actor.defs#profileViewBasic'] = Field(
        default='chat.bsky.actor.defs#profileViewBasic', alias='$type', frozen=True
    )
