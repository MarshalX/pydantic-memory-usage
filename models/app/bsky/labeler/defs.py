import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class LabelerView(base.ModelBase):
    cid: str
    creator: 'models.AppBskyActorDefs.ProfileView'
    indexed_at: str
    uri: str
    labels: t.Optional[t.List['models.ComAtprotoLabelDefs.Label']] = None
    like_count: t.Optional[int] = Field(default=None, ge=0)
    viewer: t.Optional['models.AppBskyLabelerDefs.LabelerViewerState'] = None

    py_type: t.Literal['app.bsky.labeler.defs#labelerView'] = Field(
        default='app.bsky.labeler.defs#labelerView', alias='$type', frozen=True
    )


class LabelerViewDetailed(base.ModelBase):
    cid: str
    creator: 'models.AppBskyActorDefs.ProfileView'
    indexed_at: str
    policies: 'models.AppBskyLabelerDefs.LabelerPolicies'
    uri: str
    labels: t.Optional[t.List['models.ComAtprotoLabelDefs.Label']] = None
    like_count: t.Optional[int] = Field(default=None, ge=0)
    viewer: t.Optional['models.AppBskyLabelerDefs.LabelerViewerState'] = None

    py_type: t.Literal['app.bsky.labeler.defs#labelerViewDetailed'] = Field(
        default='app.bsky.labeler.defs#labelerViewDetailed', alias='$type', frozen=True
    )


class LabelerViewerState(base.ModelBase):
    like: t.Optional[str] = None

    py_type: t.Literal['app.bsky.labeler.defs#labelerViewerState'] = Field(
        default='app.bsky.labeler.defs#labelerViewerState', alias='$type', frozen=True
    )


class LabelerPolicies(base.ModelBase):
    label_values: t.List['models.ComAtprotoLabelDefs.LabelValue']
    label_value_definitions: t.Optional[t.List['models.ComAtprotoLabelDefs.LabelValueDefinition']] = None

    py_type: t.Literal['app.bsky.labeler.defs#labelerPolicies'] = Field(
        default='app.bsky.labeler.defs#labelerPolicies', alias='$type', frozen=True
    )
