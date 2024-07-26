import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Params(base.ModelBase):
    """"""

    cursor: t.Optional[int] = None


class Labels(base.ModelBase):
    labels: t.List['models.ComAtprotoLabelDefs.Label']
    seq: int

    py_type: t.Literal['com.atproto.label.subscribeLabels#labels'] = Field(
        default='com.atproto.label.subscribeLabels#labels', alias='$type', frozen=True
    )


class Info(base.ModelBase):
    name: str
    message: t.Optional[str] = None

    py_type: t.Literal['com.atproto.label.subscribeLabels#info'] = Field(
        default='com.atproto.label.subscribeLabels#info', alias='$type', frozen=True
    )
