import typing_extensions as te

from models import base

#: Data raw data type.
Data: te.TypeAlias = bytes


class Response(base.ModelBase):
    blob: str
