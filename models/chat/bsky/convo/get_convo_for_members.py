import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Params(base.ModelBase):
    """"""

    members: t.List[str] = Field(min_length=1, max_length=10)


class Response(base.ModelBase):
    convo: 'models.ChatBskyConvoDefs.ConvoView'
