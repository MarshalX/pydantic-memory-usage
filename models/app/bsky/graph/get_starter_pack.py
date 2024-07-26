import typing as t

if t.TYPE_CHECKING:
    import models
from models import base


class Params(base.ModelBase):
    """"""

    starter_pack: str


class Response(base.ModelBase):
    starter_pack: 'models.AppBskyGraphDefs.StarterPackView'
