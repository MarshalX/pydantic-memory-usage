import typing as t

import typing_extensions as te

from models import base


class Params(base.ModelBase):
    """"""

    did: str
    since: t.Optional[str] = None


#: Response raw data type.
Response: te.TypeAlias = bytes
