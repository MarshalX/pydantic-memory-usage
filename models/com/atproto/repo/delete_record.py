import typing as t

from models import base


class Data(base.ModelBase):
    collection: str
    repo: str
    rkey: str
    swap_commit: t.Optional[str] = None
    swap_record: t.Optional[str] = None
