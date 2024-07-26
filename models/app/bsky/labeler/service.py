import typing as t

import typing_extensions as te
from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Record(base.ModelBase):
    created_at: str
    policies: 'models.AppBskyLabelerDefs.LabelerPolicies'
    labels: t.Optional[
        te.Annotated[t.Union['models.ComAtprotoLabelDefs.SelfLabels'], Field(default=None, discriminator='py_type')]
    ] = None

    py_type: t.Literal['app.bsky.labeler.service'] = Field(
        default='app.bsky.labeler.service', alias='$type', frozen=True
    )
