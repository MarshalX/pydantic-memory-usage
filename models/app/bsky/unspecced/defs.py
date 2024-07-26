import typing as t

from pydantic import Field

from models import base


class SkeletonSearchPost(base.ModelBase):
    uri: str

    py_type: t.Literal['app.bsky.unspecced.defs#skeletonSearchPost'] = Field(
        default='app.bsky.unspecced.defs#skeletonSearchPost', alias='$type', frozen=True
    )


class SkeletonSearchActor(base.ModelBase):
    did: str

    py_type: t.Literal['app.bsky.unspecced.defs#skeletonSearchActor'] = Field(
        default='app.bsky.unspecced.defs#skeletonSearchActor', alias='$type', frozen=True
    )
