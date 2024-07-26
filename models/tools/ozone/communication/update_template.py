import typing as t

from models import base


class Data(base.ModelBase):
    id: str
    content_markdown: t.Optional[str] = None
    disabled: t.Optional[bool] = None
    name: t.Optional[str] = None
    subject: t.Optional[str] = None
    updated_by: t.Optional[str] = None
