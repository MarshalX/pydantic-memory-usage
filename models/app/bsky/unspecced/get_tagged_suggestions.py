import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Params(base.ModelBase):
    """"""


class Response(base.ModelBase):
    suggestions: t.List['models.AppBskyUnspeccedGetTaggedSuggestions.Suggestion']


class Suggestion(base.ModelBase):
    subject: str
    subject_type: str
    tag: str

    py_type: t.Literal['app.bsky.unspecced.getTaggedSuggestions#suggestion'] = Field(
        default='app.bsky.unspecced.getTaggedSuggestions#suggestion', alias='$type', frozen=True
    )
