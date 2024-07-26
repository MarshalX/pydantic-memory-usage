import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Params(base.ModelBase):
    """"""

    added_labels: t.Optional[t.List[str]] = None
    added_tags: t.Optional[t.List[str]] = None
    comment: t.Optional[str] = None
    created_after: t.Optional[str] = None
    created_before: t.Optional[str] = None
    created_by: t.Optional[str] = None
    cursor: t.Optional[str] = None
    has_comment: t.Optional[bool] = None
    include_all_user_records: t.Optional[bool] = None
    limit: t.Optional[int] = Field(default=50, ge=1, le=100)
    removed_labels: t.Optional[t.List[str]] = None
    removed_tags: t.Optional[t.List[str]] = None
    report_types: t.Optional[t.List[str]] = None
    sort_direction: t.Optional[str] = None
    subject: t.Optional[str] = None
    types: t.Optional[t.List[str]] = None


class Response(base.ModelBase):
    events: t.List['models.ToolsOzoneModerationDefs.ModEventView']
    cursor: t.Optional[str] = None
