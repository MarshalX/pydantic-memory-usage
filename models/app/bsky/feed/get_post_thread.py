import typing as t

import typing_extensions as te
from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Params(base.ModelBase):
    """"""

    uri: str
    depth: t.Optional[int] = Field(default=6, ge=0, le=1000)
    parent_height: t.Optional[int] = Field(default=80, ge=0, le=1000)


class Response(base.ModelBase):
    thread: te.Annotated[
        t.Union[
            'models.AppBskyFeedDefs.ThreadViewPost',
            'models.AppBskyFeedDefs.NotFoundPost',
            'models.AppBskyFeedDefs.BlockedPost',
        ],
        Field(discriminator='py_type'),
    ]
