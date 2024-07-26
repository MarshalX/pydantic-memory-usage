import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Response(base.ModelBase):
    appview: t.Optional['models.ToolsOzoneServerGetConfig.ServiceConfig'] = None
    blob_divert: t.Optional['models.ToolsOzoneServerGetConfig.ServiceConfig'] = None
    chat: t.Optional['models.ToolsOzoneServerGetConfig.ServiceConfig'] = None
    pds: t.Optional['models.ToolsOzoneServerGetConfig.ServiceConfig'] = None
    viewer: t.Optional['models.ToolsOzoneServerGetConfig.ViewerConfig'] = None


class ServiceConfig(base.ModelBase):
    url: t.Optional[str] = None

    py_type: t.Literal['tools.ozone.server.getConfig#serviceConfig'] = Field(
        default='tools.ozone.server.getConfig#serviceConfig', alias='$type', frozen=True
    )


class ViewerConfig(base.ModelBase):
    role: t.Optional[str] = None

    py_type: t.Literal['tools.ozone.server.getConfig#viewerConfig'] = Field(
        default='tools.ozone.server.getConfig#viewerConfig', alias='$type', frozen=True
    )
