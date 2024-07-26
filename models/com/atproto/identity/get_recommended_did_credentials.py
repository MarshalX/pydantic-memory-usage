import typing as t

if t.TYPE_CHECKING:
    from models.unknown_type import UnknownType
from models import base


class Response(base.ModelBase):
    also_known_as: t.Optional[t.List[str]] = None
    rotation_keys: t.Optional[t.List[str]] = None
    services: t.Optional['UnknownType'] = None
    verification_methods: t.Optional['UnknownType'] = None
