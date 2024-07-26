import typing as t

import typing_extensions as te
from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Params(base.ModelBase):
    """"""

    dids: t.List[str]
    detailed: t.Optional[bool] = None


class Response(base.ModelBase):
    views: t.List[
        te.Annotated[
            t.Union['models.AppBskyLabelerDefs.LabelerView', 'models.AppBskyLabelerDefs.LabelerViewDetailed'],
            Field(discriminator='py_type'),
        ]
    ]
