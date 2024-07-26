import typing as t

import typing_extensions as te
from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Params(base.ModelBase):
    """"""

    convo_id: str
    cursor: t.Optional[str] = None
    limit: t.Optional[int] = Field(default=50, ge=1, le=100)


class Response(base.ModelBase):
    messages: t.List[
        te.Annotated[
            t.Union['models.ChatBskyConvoDefs.MessageView', 'models.ChatBskyConvoDefs.DeletedMessageView'],
            Field(discriminator='py_type'),
        ]
    ]
    cursor: t.Optional[str] = None
