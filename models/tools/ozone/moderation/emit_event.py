import typing as t

import typing_extensions as te
from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Data(base.ModelBase):
    created_by: str
    event: te.Annotated[
        t.Union[
            'models.ToolsOzoneModerationDefs.ModEventTakedown',
            'models.ToolsOzoneModerationDefs.ModEventAcknowledge',
            'models.ToolsOzoneModerationDefs.ModEventEscalate',
            'models.ToolsOzoneModerationDefs.ModEventComment',
            'models.ToolsOzoneModerationDefs.ModEventLabel',
            'models.ToolsOzoneModerationDefs.ModEventReport',
            'models.ToolsOzoneModerationDefs.ModEventMute',
            'models.ToolsOzoneModerationDefs.ModEventUnmute',
            'models.ToolsOzoneModerationDefs.ModEventMuteReporter',
            'models.ToolsOzoneModerationDefs.ModEventUnmuteReporter',
            'models.ToolsOzoneModerationDefs.ModEventReverseTakedown',
            'models.ToolsOzoneModerationDefs.ModEventEmail',
            'models.ToolsOzoneModerationDefs.ModEventTag',
        ],
        Field(discriminator='py_type'),
    ]
    subject: te.Annotated[
        t.Union['models.ComAtprotoAdminDefs.RepoRef', 'models.ComAtprotoRepoStrongRef.Main'],
        Field(discriminator='py_type'),
    ]
    subject_blob_cids: t.Optional[t.List[str]] = None
