import typing as t

if t.TYPE_CHECKING:
    from models.unknown_type import UnknownInputType, UnknownType
from models import base


class Data(base.ModelBase):
    also_known_as: t.Optional[t.List[str]] = None
    rotation_keys: t.Optional[t.List[str]] = None
    services: t.Optional['UnknownInputType'] = None
    token: t.Optional[str] = None
    verification_methods: t.Optional['UnknownInputType'] = None


class Response(base.ModelBase):
    operation: 'UnknownType'
