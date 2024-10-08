import typing as t

import typing_extensions as te
from pydantic import Field

if t.TYPE_CHECKING:
    import models

UnknownRecordType: te.TypeAlias = t.Union[
    'models.AppBskyActorProfile.Record',
    'models.AppBskyFeedGenerator.Record',
    'models.AppBskyFeedLike.Record',
    'models.AppBskyFeedPost.Record',
    'models.AppBskyFeedRepost.Record',
    'models.AppBskyFeedThreadgate.Record',
    'models.AppBskyGraphBlock.Record',
    'models.AppBskyGraphFollow.Record',
    'models.AppBskyGraphList.Record',
    'models.AppBskyGraphListblock.Record',
    'models.AppBskyGraphListitem.Record',
    'models.AppBskyGraphStarterpack.Record',
    'models.AppBskyLabelerService.Record',
    'models.ChatBskyActorDeclaration.Record',
]
UnknownRecordTypePydantic = te.Annotated[
    t.Union[
        'models.AppBskyActorProfile.Record',
        'models.AppBskyFeedGenerator.Record',
        'models.AppBskyFeedLike.Record',
        'models.AppBskyFeedPost.Record',
        'models.AppBskyFeedRepost.Record',
        'models.AppBskyFeedThreadgate.Record',
        'models.AppBskyGraphBlock.Record',
        'models.AppBskyGraphFollow.Record',
        'models.AppBskyGraphList.Record',
        'models.AppBskyGraphListblock.Record',
        'models.AppBskyGraphListitem.Record',
        'models.AppBskyGraphStarterpack.Record',
        'models.AppBskyLabelerService.Record',
        'models.ChatBskyActorDeclaration.Record',
    ],
    Field(discriminator='py_type'),
]
UnknownType: te.TypeAlias = t.Union[UnknownRecordTypePydantic]
UnknownInputType: te.TypeAlias = t.Union[UnknownType, t.Dict[str, t.Any]]
