import typing as t

import typing_extensions as te
from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Params(base.ModelBase):
    """"""

    message_id: str
    after: t.Optional[int] = None
    before: t.Optional[int] = None
    convo_id: t.Optional[str] = None


class Response(base.ModelBase):
    messages: t.List[
        te.Annotated[
            t.Union['models.ChatBskyConvoDefs.MessageView', 'models.ChatBskyConvoDefs.DeletedMessageView'],
            Field(discriminator='py_type'),
        ]
    ]
