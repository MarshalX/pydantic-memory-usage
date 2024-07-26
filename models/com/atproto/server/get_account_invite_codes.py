import typing as t

if t.TYPE_CHECKING:
    import models
from models import base


class Params(base.ModelBase):
    """"""

    create_available: t.Optional[bool] = None
    include_used: t.Optional[bool] = None


class Response(base.ModelBase):
    codes: t.List['models.ComAtprotoServerDefs.InviteCode']
