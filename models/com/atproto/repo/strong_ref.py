import typing as t

from pydantic import Field

from models import base


class Main(base.ModelBase):
    cid: str
    uri: str

    py_type: t.Literal['com.atproto.repo.strongRef'] = Field(
        default='com.atproto.repo.strongRef', alias='$type', frozen=True
    )
