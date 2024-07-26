import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
    from models.unknown_type import UnknownType
from models import base


class ListViewBasic(base.ModelBase):
    cid: str
    name: str = Field(min_length=1, max_length=64)
    purpose: 'models.AppBskyGraphDefs.ListPurpose'
    uri: str
    avatar: t.Optional[str] = None
    indexed_at: t.Optional[str] = None
    labels: t.Optional[t.List['models.ComAtprotoLabelDefs.Label']] = None
    list_item_count: t.Optional[int] = Field(default=None, ge=0)
    viewer: t.Optional['models.AppBskyGraphDefs.ListViewerState'] = None

    py_type: t.Literal['app.bsky.graph.defs#listViewBasic'] = Field(
        default='app.bsky.graph.defs#listViewBasic', alias='$type', frozen=True
    )


class ListView(base.ModelBase):
    cid: str
    creator: 'models.AppBskyActorDefs.ProfileView'
    indexed_at: str
    name: str = Field(min_length=1, max_length=64)
    purpose: 'models.AppBskyGraphDefs.ListPurpose'
    uri: str
    avatar: t.Optional[str] = None
    description: t.Optional[str] = Field(default=None, max_length=3000)
    description_facets: t.Optional[t.List['models.AppBskyRichtextFacet.Main']] = None
    labels: t.Optional[t.List['models.ComAtprotoLabelDefs.Label']] = None
    list_item_count: t.Optional[int] = Field(default=None, ge=0)
    viewer: t.Optional['models.AppBskyGraphDefs.ListViewerState'] = None

    py_type: t.Literal['app.bsky.graph.defs#listView'] = Field(
        default='app.bsky.graph.defs#listView', alias='$type', frozen=True
    )


class ListItemView(base.ModelBase):
    subject: 'models.AppBskyActorDefs.ProfileView'
    uri: str

    py_type: t.Literal['app.bsky.graph.defs#listItemView'] = Field(
        default='app.bsky.graph.defs#listItemView', alias='$type', frozen=True
    )


class StarterPackView(base.ModelBase):
    cid: str
    creator: 'models.AppBskyActorDefs.ProfileViewBasic'
    indexed_at: str
    record: 'UnknownType'
    uri: str
    feeds: t.Optional[t.List['models.AppBskyFeedDefs.GeneratorView']] = Field(default=None, max_length=3)
    joined_all_time_count: t.Optional[int] = Field(default=None, ge=0)
    joined_week_count: t.Optional[int] = Field(default=None, ge=0)
    labels: t.Optional[t.List['models.ComAtprotoLabelDefs.Label']] = None
    list: t.Optional['models.AppBskyGraphDefs.ListViewBasic'] = None
    list_items_sample: t.Optional[t.List['models.AppBskyGraphDefs.ListItemView']] = Field(default=None, max_length=12)

    py_type: t.Literal['app.bsky.graph.defs#starterPackView'] = Field(
        default='app.bsky.graph.defs#starterPackView', alias='$type', frozen=True
    )


class StarterPackViewBasic(base.ModelBase):
    cid: str
    creator: 'models.AppBskyActorDefs.ProfileViewBasic'
    indexed_at: str
    record: 'UnknownType'
    uri: str
    joined_all_time_count: t.Optional[int] = Field(default=None, ge=0)
    joined_week_count: t.Optional[int] = Field(default=None, ge=0)
    labels: t.Optional[t.List['models.ComAtprotoLabelDefs.Label']] = None
    list_item_count: t.Optional[int] = Field(default=None, ge=0)

    py_type: t.Literal['app.bsky.graph.defs#starterPackViewBasic'] = Field(
        default='app.bsky.graph.defs#starterPackViewBasic', alias='$type', frozen=True
    )


ListPurpose = t.Union[
    'models.AppBskyGraphDefs.Modlist', 'models.AppBskyGraphDefs.Curatelist', 'models.AppBskyGraphDefs.Referencelist'
]  #: List purpose

Modlist = t.Literal[
    'app.bsky.graph.defs#modlist'
]  #: A list of actors to apply an aggregate moderation action (mute/block) on.

Curatelist = t.Literal[
    'app.bsky.graph.defs#curatelist'
]  #: A list of actors used for curation purposes such as list feeds or interaction gating.

Referencelist = t.Literal[
    'app.bsky.graph.defs#referencelist'
]  #: A list of actors used for only for reference purposes such as within a starter pack.


class ListViewerState(base.ModelBase):
    blocked: t.Optional[str] = None
    muted: t.Optional[bool] = None

    py_type: t.Literal['app.bsky.graph.defs#listViewerState'] = Field(
        default='app.bsky.graph.defs#listViewerState', alias='$type', frozen=True
    )


class NotFoundActor(base.ModelBase):
    actor: str
    not_found: bool = Field(frozen=True)

    py_type: t.Literal['app.bsky.graph.defs#notFoundActor'] = Field(
        default='app.bsky.graph.defs#notFoundActor', alias='$type', frozen=True
    )


class Relationship(base.ModelBase):
    did: str
    followed_by: t.Optional[str] = None
    following: t.Optional[str] = None

    py_type: t.Literal['app.bsky.graph.defs#relationship'] = Field(
        default='app.bsky.graph.defs#relationship', alias='$type', frozen=True
    )
