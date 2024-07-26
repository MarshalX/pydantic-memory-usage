import typing_extensions as te

from models import base


class Params(base.ModelBase):
    """"""

    did: str


#: Response raw data type.
Response: te.TypeAlias = bytes
