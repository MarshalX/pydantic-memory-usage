import typing as t

if t.TYPE_CHECKING:
    import models
from models import base


class Params(base.ModelBase):
    """"""

    feeds: t.List[str]


class Response(base.ModelBase):
    feeds: t.List['models.AppBskyFeedDefs.GeneratorView']
