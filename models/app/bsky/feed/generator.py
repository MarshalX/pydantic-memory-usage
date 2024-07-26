import typing as t

import typing_extensions as te
from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Record(base.ModelBase):
    created_at: str
    did: str
    display_name: str = Field(max_length=240)
    accepts_interactions: t.Optional[bool] = None
    avatar: t.Optional[str] = None
    description: t.Optional[str] = Field(default=None, max_length=3000)
    description_facets: t.Optional[t.List['models.AppBskyRichtextFacet.Main']] = None
    labels: t.Optional[
        te.Annotated[t.Union['models.ComAtprotoLabelDefs.SelfLabels'], Field(default=None, discriminator='py_type')]
    ] = None

    py_type: t.Literal['app.bsky.feed.generator'] = Field(default='app.bsky.feed.generator', alias='$type', frozen=True)
