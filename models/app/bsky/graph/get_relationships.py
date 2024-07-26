import typing as t

import typing_extensions as te
from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Params(base.ModelBase):
    """"""

    actor: str
    others: t.Optional[t.List[str]] = Field(default=None, max_length=30)


class Response(base.ModelBase):
    relationships: t.List[
        te.Annotated[
            t.Union['models.AppBskyGraphDefs.Relationship', 'models.AppBskyGraphDefs.NotFoundActor'],
            Field(discriminator='py_type'),
        ]
    ]
    actor: t.Optional[str] = None
