import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Params(base.ModelBase):
    """"""

    appealed: t.Optional[bool] = None
    comment: t.Optional[str] = None
    cursor: t.Optional[str] = None
    exclude_tags: t.Optional[t.List[str]] = None
    ignore_subjects: t.Optional[t.List[str]] = None
    include_muted: t.Optional[bool] = None
    last_reviewed_by: t.Optional[str] = None
    limit: t.Optional[int] = Field(default=50, ge=1, le=100)
    only_muted: t.Optional[bool] = None
    reported_after: t.Optional[str] = None
    reported_before: t.Optional[str] = None
    review_state: t.Optional[str] = None
    reviewed_after: t.Optional[str] = None
    reviewed_before: t.Optional[str] = None
    sort_direction: t.Optional[str] = None
    sort_field: t.Optional[str] = None
    subject: t.Optional[str] = None
    tags: t.Optional[t.List[str]] = None
    takendown: t.Optional[bool] = None


class Response(base.ModelBase):
    subject_statuses: t.List['models.ToolsOzoneModerationDefs.SubjectStatusView']
    cursor: t.Optional[str] = None
