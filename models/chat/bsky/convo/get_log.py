import typing as t

import typing_extensions as te
from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Params(base.ModelBase):
    """"""

    cursor: t.Optional[str] = None


class Response(base.ModelBase):
    logs: t.List[
        te.Annotated[
            t.Union[
                'models.ChatBskyConvoDefs.LogBeginConvo',
                'models.ChatBskyConvoDefs.LogLeaveConvo',
                'models.ChatBskyConvoDefs.LogCreateMessage',
                'models.ChatBskyConvoDefs.LogDeleteMessage',
            ],
            Field(discriminator='py_type'),
        ]
    ]
    cursor: t.Optional[str] = None
