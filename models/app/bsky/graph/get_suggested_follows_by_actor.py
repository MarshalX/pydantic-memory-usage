import typing as t

if t.TYPE_CHECKING:
    import models
from models import base


class Params(base.ModelBase):
    """"""

    actor: str


class Response(base.ModelBase):
    suggestions: t.List['models.AppBskyActorDefs.ProfileView']
