import typing as t

import typing_extensions as te
from pydantic import Field

if t.TYPE_CHECKING:
    import models
    from models.unknown_type import UnknownType
from models import base


class ModEventView(base.ModelBase):
    created_at: str
    created_by: str
    event: te.Annotated[
        t.Union[
            'models.ToolsOzoneModerationDefs.ModEventTakedown',
            'models.ToolsOzoneModerationDefs.ModEventReverseTakedown',
            'models.ToolsOzoneModerationDefs.ModEventComment',
            'models.ToolsOzoneModerationDefs.ModEventReport',
            'models.ToolsOzoneModerationDefs.ModEventLabel',
            'models.ToolsOzoneModerationDefs.ModEventAcknowledge',
            'models.ToolsOzoneModerationDefs.ModEventEscalate',
            'models.ToolsOzoneModerationDefs.ModEventMute',
            'models.ToolsOzoneModerationDefs.ModEventUnmute',
            'models.ToolsOzoneModerationDefs.ModEventMuteReporter',
            'models.ToolsOzoneModerationDefs.ModEventUnmuteReporter',
            'models.ToolsOzoneModerationDefs.ModEventEmail',
            'models.ToolsOzoneModerationDefs.ModEventResolveAppeal',
            'models.ToolsOzoneModerationDefs.ModEventDivert',
            'models.ToolsOzoneModerationDefs.ModEventTag',
        ],
        Field(discriminator='py_type'),
    ]
    id: int
    subject: te.Annotated[
        t.Union[
            'models.ComAtprotoAdminDefs.RepoRef',
            'models.ComAtprotoRepoStrongRef.Main',
            'models.ChatBskyConvoDefs.MessageRef',
        ],
        Field(discriminator='py_type'),
    ]
    subject_blob_cids: t.List[str]
    creator_handle: t.Optional[str] = None
    subject_handle: t.Optional[str] = None

    py_type: t.Literal['tools.ozone.moderation.defs#modEventView'] = Field(
        default='tools.ozone.moderation.defs#modEventView', alias='$type', frozen=True
    )


class ModEventViewDetail(base.ModelBase):
    created_at: str
    created_by: str
    event: te.Annotated[
        t.Union[
            'models.ToolsOzoneModerationDefs.ModEventTakedown',
            'models.ToolsOzoneModerationDefs.ModEventReverseTakedown',
            'models.ToolsOzoneModerationDefs.ModEventComment',
            'models.ToolsOzoneModerationDefs.ModEventReport',
            'models.ToolsOzoneModerationDefs.ModEventLabel',
            'models.ToolsOzoneModerationDefs.ModEventAcknowledge',
            'models.ToolsOzoneModerationDefs.ModEventEscalate',
            'models.ToolsOzoneModerationDefs.ModEventMute',
            'models.ToolsOzoneModerationDefs.ModEventUnmute',
            'models.ToolsOzoneModerationDefs.ModEventMuteReporter',
            'models.ToolsOzoneModerationDefs.ModEventUnmuteReporter',
            'models.ToolsOzoneModerationDefs.ModEventEmail',
            'models.ToolsOzoneModerationDefs.ModEventResolveAppeal',
            'models.ToolsOzoneModerationDefs.ModEventDivert',
            'models.ToolsOzoneModerationDefs.ModEventTag',
        ],
        Field(discriminator='py_type'),
    ]
    id: int
    subject: te.Annotated[
        t.Union[
            'models.ToolsOzoneModerationDefs.RepoView',
            'models.ToolsOzoneModerationDefs.RepoViewNotFound',
            'models.ToolsOzoneModerationDefs.RecordView',
            'models.ToolsOzoneModerationDefs.RecordViewNotFound',
        ],
        Field(discriminator='py_type'),
    ]
    subject_blobs: t.List['models.ToolsOzoneModerationDefs.BlobView']

    py_type: t.Literal['tools.ozone.moderation.defs#modEventViewDetail'] = Field(
        default='tools.ozone.moderation.defs#modEventViewDetail', alias='$type', frozen=True
    )


class SubjectStatusView(base.ModelBase):
    created_at: str
    id: int
    review_state: 'models.ToolsOzoneModerationDefs.SubjectReviewState'
    subject: te.Annotated[
        t.Union['models.ComAtprotoAdminDefs.RepoRef', 'models.ComAtprotoRepoStrongRef.Main'],
        Field(discriminator='py_type'),
    ]
    updated_at: str
    appealed: t.Optional[bool] = None
    comment: t.Optional[str] = None
    last_appealed_at: t.Optional[str] = None
    last_reported_at: t.Optional[str] = None
    last_reviewed_at: t.Optional[str] = None
    last_reviewed_by: t.Optional[str] = None
    mute_reporting_until: t.Optional[str] = None
    mute_until: t.Optional[str] = None
    subject_blob_cids: t.Optional[t.List[str]] = None
    subject_repo_handle: t.Optional[str] = None
    suspend_until: t.Optional[str] = None
    tags: t.Optional[t.List[str]] = None
    takendown: t.Optional[bool] = None

    py_type: t.Literal['tools.ozone.moderation.defs#subjectStatusView'] = Field(
        default='tools.ozone.moderation.defs#subjectStatusView', alias='$type', frozen=True
    )


SubjectReviewState = t.Union[
    'models.ToolsOzoneModerationDefs.ReviewOpen',
    'models.ToolsOzoneModerationDefs.ReviewEscalated',
    'models.ToolsOzoneModerationDefs.ReviewClosed',
    'models.ToolsOzoneModerationDefs.ReviewNone',
]  #: Subject review state

ReviewOpen = t.Literal[
    'tools.ozone.moderation.defs#reviewOpen'
]  #: Moderator review status of a subject: Open. Indicates that the subject needs to be reviewed by a moderator

ReviewEscalated = t.Literal[
    'tools.ozone.moderation.defs#reviewEscalated'
]  #: Moderator review status of a subject: Escalated. Indicates that the subject was escalated for review by a moderator

ReviewClosed = t.Literal[
    'tools.ozone.moderation.defs#reviewClosed'
]  #: Moderator review status of a subject: Closed. Indicates that the subject was already reviewed and resolved by a moderator

ReviewNone = t.Literal[
    'tools.ozone.moderation.defs#reviewNone'
]  #: Moderator review status of a subject: Unnecessary. Indicates that the subject does not need a review at the moment but there is probably some moderation related metadata available for it


class ModEventTakedown(base.ModelBase):
    comment: t.Optional[str] = None
    duration_in_hours: t.Optional[int] = None

    py_type: t.Literal['tools.ozone.moderation.defs#modEventTakedown'] = Field(
        default='tools.ozone.moderation.defs#modEventTakedown', alias='$type', frozen=True
    )


class ModEventReverseTakedown(base.ModelBase):
    comment: t.Optional[str] = None

    py_type: t.Literal['tools.ozone.moderation.defs#modEventReverseTakedown'] = Field(
        default='tools.ozone.moderation.defs#modEventReverseTakedown', alias='$type', frozen=True
    )


class ModEventResolveAppeal(base.ModelBase):
    comment: t.Optional[str] = None

    py_type: t.Literal['tools.ozone.moderation.defs#modEventResolveAppeal'] = Field(
        default='tools.ozone.moderation.defs#modEventResolveAppeal', alias='$type', frozen=True
    )


class ModEventComment(base.ModelBase):
    comment: str
    sticky: t.Optional[bool] = None

    py_type: t.Literal['tools.ozone.moderation.defs#modEventComment'] = Field(
        default='tools.ozone.moderation.defs#modEventComment', alias='$type', frozen=True
    )


class ModEventReport(base.ModelBase):
    report_type: 'models.ComAtprotoModerationDefs.ReasonType'
    comment: t.Optional[str] = None
    is_reporter_muted: t.Optional[bool] = None

    py_type: t.Literal['tools.ozone.moderation.defs#modEventReport'] = Field(
        default='tools.ozone.moderation.defs#modEventReport', alias='$type', frozen=True
    )


class ModEventLabel(base.ModelBase):
    create_label_vals: t.List[str]
    negate_label_vals: t.List[str]
    comment: t.Optional[str] = None

    py_type: t.Literal['tools.ozone.moderation.defs#modEventLabel'] = Field(
        default='tools.ozone.moderation.defs#modEventLabel', alias='$type', frozen=True
    )


class ModEventAcknowledge(base.ModelBase):
    comment: t.Optional[str] = None

    py_type: t.Literal['tools.ozone.moderation.defs#modEventAcknowledge'] = Field(
        default='tools.ozone.moderation.defs#modEventAcknowledge', alias='$type', frozen=True
    )


class ModEventEscalate(base.ModelBase):
    comment: t.Optional[str] = None

    py_type: t.Literal['tools.ozone.moderation.defs#modEventEscalate'] = Field(
        default='tools.ozone.moderation.defs#modEventEscalate', alias='$type', frozen=True
    )


class ModEventMute(base.ModelBase):
    duration_in_hours: int
    comment: t.Optional[str] = None

    py_type: t.Literal['tools.ozone.moderation.defs#modEventMute'] = Field(
        default='tools.ozone.moderation.defs#modEventMute', alias='$type', frozen=True
    )


class ModEventUnmute(base.ModelBase):
    comment: t.Optional[str] = None

    py_type: t.Literal['tools.ozone.moderation.defs#modEventUnmute'] = Field(
        default='tools.ozone.moderation.defs#modEventUnmute', alias='$type', frozen=True
    )


class ModEventMuteReporter(base.ModelBase):
    duration_in_hours: int
    comment: t.Optional[str] = None

    py_type: t.Literal['tools.ozone.moderation.defs#modEventMuteReporter'] = Field(
        default='tools.ozone.moderation.defs#modEventMuteReporter', alias='$type', frozen=True
    )


class ModEventUnmuteReporter(base.ModelBase):
    comment: t.Optional[str] = None

    py_type: t.Literal['tools.ozone.moderation.defs#modEventUnmuteReporter'] = Field(
        default='tools.ozone.moderation.defs#modEventUnmuteReporter', alias='$type', frozen=True
    )


class ModEventEmail(base.ModelBase):
    subject_line: str
    comment: t.Optional[str] = None
    content: t.Optional[str] = None

    py_type: t.Literal['tools.ozone.moderation.defs#modEventEmail'] = Field(
        default='tools.ozone.moderation.defs#modEventEmail', alias='$type', frozen=True
    )


class ModEventDivert(base.ModelBase):
    comment: t.Optional[str] = None

    py_type: t.Literal['tools.ozone.moderation.defs#modEventDivert'] = Field(
        default='tools.ozone.moderation.defs#modEventDivert', alias='$type', frozen=True
    )


class ModEventTag(base.ModelBase):
    add: t.List[str]
    remove: t.List[str]
    comment: t.Optional[str] = None

    py_type: t.Literal['tools.ozone.moderation.defs#modEventTag'] = Field(
        default='tools.ozone.moderation.defs#modEventTag', alias='$type', frozen=True
    )


class RepoView(base.ModelBase):
    did: str
    handle: str
    indexed_at: str
    moderation: 'models.ToolsOzoneModerationDefs.Moderation'
    related_records: t.List['UnknownType']
    deactivated_at: t.Optional[str] = None
    email: t.Optional[str] = None
    invite_note: t.Optional[str] = None
    invited_by: t.Optional['models.ComAtprotoServerDefs.InviteCode'] = None
    invites_disabled: t.Optional[bool] = None

    py_type: t.Literal['tools.ozone.moderation.defs#repoView'] = Field(
        default='tools.ozone.moderation.defs#repoView', alias='$type', frozen=True
    )


class RepoViewDetail(base.ModelBase):
    did: str
    handle: str
    indexed_at: str
    moderation: 'models.ToolsOzoneModerationDefs.ModerationDetail'
    related_records: t.List['UnknownType']
    deactivated_at: t.Optional[str] = None
    email: t.Optional[str] = None
    email_confirmed_at: t.Optional[str] = None
    invite_note: t.Optional[str] = None
    invited_by: t.Optional['models.ComAtprotoServerDefs.InviteCode'] = None
    invites: t.Optional[t.List['models.ComAtprotoServerDefs.InviteCode']] = None
    invites_disabled: t.Optional[bool] = None
    labels: t.Optional[t.List['models.ComAtprotoLabelDefs.Label']] = None

    py_type: t.Literal['tools.ozone.moderation.defs#repoViewDetail'] = Field(
        default='tools.ozone.moderation.defs#repoViewDetail', alias='$type', frozen=True
    )


class RepoViewNotFound(base.ModelBase):
    did: str

    py_type: t.Literal['tools.ozone.moderation.defs#repoViewNotFound'] = Field(
        default='tools.ozone.moderation.defs#repoViewNotFound', alias='$type', frozen=True
    )


class RecordView(base.ModelBase):
    blob_cids: t.List[str]
    cid: str
    indexed_at: str
    moderation: 'models.ToolsOzoneModerationDefs.Moderation'
    repo: 'models.ToolsOzoneModerationDefs.RepoView'
    uri: str
    value: 'UnknownType'

    py_type: t.Literal['tools.ozone.moderation.defs#recordView'] = Field(
        default='tools.ozone.moderation.defs#recordView', alias='$type', frozen=True
    )


class RecordViewDetail(base.ModelBase):
    blobs: t.List['models.ToolsOzoneModerationDefs.BlobView']
    cid: str
    indexed_at: str
    moderation: 'models.ToolsOzoneModerationDefs.ModerationDetail'
    repo: 'models.ToolsOzoneModerationDefs.RepoView'
    uri: str
    value: 'UnknownType'
    labels: t.Optional[t.List['models.ComAtprotoLabelDefs.Label']] = None

    py_type: t.Literal['tools.ozone.moderation.defs#recordViewDetail'] = Field(
        default='tools.ozone.moderation.defs#recordViewDetail', alias='$type', frozen=True
    )


class RecordViewNotFound(base.ModelBase):
    uri: str

    py_type: t.Literal['tools.ozone.moderation.defs#recordViewNotFound'] = Field(
        default='tools.ozone.moderation.defs#recordViewNotFound', alias='$type', frozen=True
    )


class Moderation(base.ModelBase):
    subject_status: t.Optional['models.ToolsOzoneModerationDefs.SubjectStatusView'] = None

    py_type: t.Literal['tools.ozone.moderation.defs#moderation'] = Field(
        default='tools.ozone.moderation.defs#moderation', alias='$type', frozen=True
    )


class ModerationDetail(base.ModelBase):
    subject_status: t.Optional['models.ToolsOzoneModerationDefs.SubjectStatusView'] = None

    py_type: t.Literal['tools.ozone.moderation.defs#moderationDetail'] = Field(
        default='tools.ozone.moderation.defs#moderationDetail', alias='$type', frozen=True
    )


class BlobView(base.ModelBase):
    cid: str
    created_at: str
    mime_type: str
    size: int
    details: t.Optional[
        te.Annotated[
            t.Union['models.ToolsOzoneModerationDefs.ImageDetails', 'models.ToolsOzoneModerationDefs.VideoDetails'],
            Field(default=None, discriminator='py_type'),
        ]
    ] = None
    moderation: t.Optional['models.ToolsOzoneModerationDefs.Moderation'] = None

    py_type: t.Literal['tools.ozone.moderation.defs#blobView'] = Field(
        default='tools.ozone.moderation.defs#blobView', alias='$type', frozen=True
    )


class ImageDetails(base.ModelBase):
    height: int
    width: int

    py_type: t.Literal['tools.ozone.moderation.defs#imageDetails'] = Field(
        default='tools.ozone.moderation.defs#imageDetails', alias='$type', frozen=True
    )


class VideoDetails(base.ModelBase):
    height: int
    length: int
    width: int

    py_type: t.Literal['tools.ozone.moderation.defs#videoDetails'] = Field(
        default='tools.ozone.moderation.defs#videoDetails', alias='$type', frozen=True
    )
