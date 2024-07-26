import typing as t

import typing_extensions as te
from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Record(base.ModelBase):
    avatar: t.Optional[str] = None
    banner: t.Optional[str] = None
    created_at: t.Optional[str] = None
    description: t.Optional[str] = Field(default=None, max_length=2560)
    display_name: t.Optional[str] = Field(default=None, max_length=640)
    joined_via_starter_pack: t.Optional['models.ComAtprotoRepoStrongRef.Main'] = None
    labels: t.Optional[
        te.Annotated[t.Union['models.ComAtprotoLabelDefs.SelfLabels'], Field(default=None, discriminator='py_type')]
    ] = None

    py_type: t.Literal['app.bsky.actor.profile'] = Field(default='app.bsky.actor.profile', alias='$type', frozen=True)
