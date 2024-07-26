import typing as t

from models import base


class Data(base.ModelBase):
    content_markdown: str
    name: str
    subject: str
    created_by: t.Optional[str] = None
