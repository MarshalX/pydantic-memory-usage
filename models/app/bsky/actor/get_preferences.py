import typing as t

if t.TYPE_CHECKING:
    import models
from models import base


class Params(base.ModelBase):
    """"""


class Response(base.ModelBase):
    preferences: 'models.AppBskyActorDefs.Preferences'
