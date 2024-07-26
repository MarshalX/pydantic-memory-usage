import typing as t

import typing_extensions as te
from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Data(base.ModelBase):
    reason_type: 'models.ComAtprotoModerationDefs.ReasonType'
    subject: te.Annotated[
        t.Union['models.ComAtprotoAdminDefs.RepoRef', 'models.ComAtprotoRepoStrongRef.Main'],
        Field(discriminator='py_type'),
    ]
    reason: t.Optional[str] = Field(default=None, max_length=20000)


class Response(base.ModelBase):
    created_at: str
    id: int
    reason_type: 'models.ComAtprotoModerationDefs.ReasonType'
    reported_by: str
    subject: te.Annotated[
        t.Union['models.ComAtprotoAdminDefs.RepoRef', 'models.ComAtprotoRepoStrongRef.Main'],
        Field(discriminator='py_type'),
    ]
    reason: t.Optional[str] = Field(default=None, max_length=20000)
