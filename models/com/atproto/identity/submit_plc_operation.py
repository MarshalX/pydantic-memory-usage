import typing as t

if t.TYPE_CHECKING:
    from models.unknown_type import UnknownInputType
from models import base


class Data(base.ModelBase):
    operation: 'UnknownInputType'
