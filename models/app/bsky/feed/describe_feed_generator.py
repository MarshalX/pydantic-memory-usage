import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Response(base.ModelBase):
    did: str
    feeds: t.List['models.AppBskyFeedDescribeFeedGenerator.Feed']
    links: t.Optional['models.AppBskyFeedDescribeFeedGenerator.Links'] = None


class Feed(base.ModelBase):
    uri: str

    py_type: t.Literal['app.bsky.feed.describeFeedGenerator#feed'] = Field(
        default='app.bsky.feed.describeFeedGenerator#feed', alias='$type', frozen=True
    )


class Links(base.ModelBase):
    privacy_policy: t.Optional[str] = None
    terms_of_service: t.Optional[str] = None

    py_type: t.Literal['app.bsky.feed.describeFeedGenerator#links'] = Field(
        default='app.bsky.feed.describeFeedGenerator#links', alias='$type', frozen=True
    )
