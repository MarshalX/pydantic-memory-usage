import typing as t

if t.TYPE_CHECKING:
    import models
from models import base


class Params(base.ModelBase):
    """"""

    feed: str


class Response(base.ModelBase):
    is_online: bool
    is_valid: bool
    view: 'models.AppBskyFeedDefs.GeneratorView'
