import typing as t

from models import base


class Data(base.ModelBase):
    delete_after: t.Optional[str] = None
