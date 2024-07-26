import typing as t

import typing_extensions as te

from models import base


class Params(base.ModelBase):
    """"""

    cids: t.List[str]
    did: str


#: Response raw data type.
Response: te.TypeAlias = bytes
