import typing as t

import typing_extensions as te
from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Data(base.ModelBase):
    subject: te.Annotated[
        t.Union[
            'models.ComAtprotoAdminDefs.RepoRef',
            'models.ComAtprotoRepoStrongRef.Main',
            'models.ComAtprotoAdminDefs.RepoBlobRef',
        ],
        Field(discriminator='py_type'),
    ]
    deactivated: t.Optional['models.ComAtprotoAdminDefs.StatusAttr'] = None
    takedown: t.Optional['models.ComAtprotoAdminDefs.StatusAttr'] = None


class Response(base.ModelBase):
    subject: te.Annotated[
        t.Union[
            'models.ComAtprotoAdminDefs.RepoRef',
            'models.ComAtprotoRepoStrongRef.Main',
            'models.ComAtprotoAdminDefs.RepoBlobRef',
        ],
        Field(discriminator='py_type'),
    ]
    takedown: t.Optional['models.ComAtprotoAdminDefs.StatusAttr'] = None
