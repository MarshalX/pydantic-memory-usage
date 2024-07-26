import typing as t

if t.TYPE_CHECKING:
    import models
from models import base


class Data(base.ModelBase):
    interactions: t.List['models.AppBskyFeedDefs.Interaction']


class Response(base.ModelBase):
    pass
