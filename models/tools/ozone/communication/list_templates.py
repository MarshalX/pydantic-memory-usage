import typing as t

if t.TYPE_CHECKING:
    import models
from models import base


class Response(base.ModelBase):
    communication_templates: t.List['models.ToolsOzoneCommunicationDefs.TemplateView']
