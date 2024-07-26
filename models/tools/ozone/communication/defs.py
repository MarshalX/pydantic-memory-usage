import typing as t

from pydantic import Field

from models import base


class TemplateView(base.ModelBase):
    content_markdown: str
    created_at: str
    disabled: bool
    id: str
    last_updated_by: str
    name: str
    updated_at: str
    subject: t.Optional[str] = None

    py_type: t.Literal['tools.ozone.communication.defs#templateView'] = Field(
        default='tools.ozone.communication.defs#templateView', alias='$type', frozen=True
    )
