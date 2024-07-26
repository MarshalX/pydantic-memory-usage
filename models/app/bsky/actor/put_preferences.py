import typing as t

if t.TYPE_CHECKING:
    import models
from models import base


class Data(base.ModelBase):
    preferences: 'models.AppBskyActorDefs.Preferences'
