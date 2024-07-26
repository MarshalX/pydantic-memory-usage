import typing as t

if t.TYPE_CHECKING:
    from models.unknown_type import UnknownType
from models import base


class Params(base.ModelBase):
    """"""

    repo: str


class Response(base.ModelBase):
    collections: t.List[str]
    did: str
    did_doc: 'UnknownType'
    handle: str
    handle_is_correct: bool
