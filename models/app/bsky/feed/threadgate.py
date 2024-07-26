import typing as t

import typing_extensions as te
from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class MentionRule(base.ModelBase):
    py_type: t.Literal['app.bsky.feed.threadgate#mentionRule'] = Field(
        default='app.bsky.feed.threadgate#mentionRule', alias='$type', frozen=True
    )


class FollowingRule(base.ModelBase):
    py_type: t.Literal['app.bsky.feed.threadgate#followingRule'] = Field(
        default='app.bsky.feed.threadgate#followingRule', alias='$type', frozen=True
    )


class ListRule(base.ModelBase):
    list: str

    py_type: t.Literal['app.bsky.feed.threadgate#listRule'] = Field(
        default='app.bsky.feed.threadgate#listRule', alias='$type', frozen=True
    )


class Record(base.ModelBase):
    created_at: str
    post: str
    allow: t.Optional[
        t.List[
            te.Annotated[
                t.Union[
                    'models.AppBskyFeedThreadgate.MentionRule',
                    'models.AppBskyFeedThreadgate.FollowingRule',
                    'models.AppBskyFeedThreadgate.ListRule',
                ],
                Field(discriminator='py_type'),
            ]
        ]
    ] = Field(default=None, max_length=5)

    py_type: t.Literal['app.bsky.feed.threadgate'] = Field(
        default='app.bsky.feed.threadgate', alias='$type', frozen=True
    )
