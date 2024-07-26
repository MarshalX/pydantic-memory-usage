import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    from models.unknown_type import UnknownInputType
from models import base


class Data(base.ModelBase):
    collection: str
    record: 'UnknownInputType'
    repo: str
    rkey: str = Field(max_length=15)
    swap_commit: t.Optional[str] = None
    swap_record: t.Optional[str] = None
    validate_: t.Optional[bool] = None


class Response(base.ModelBase):
    cid: str
    uri: str
