import typing as t

if t.TYPE_CHECKING:
    import models
from models import base


class Params(base.ModelBase):
    """"""

    dids: t.List[str]


class Response(base.ModelBase):
    infos: t.List['models.ComAtprotoAdminDefs.AccountView']
