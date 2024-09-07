import typing as t

from pydantic import BaseModel

if t.TYPE_CHECKING:
    import models


class Profile(BaseModel):
    viewer: t.Optional['models.Defs.Viewer'] = None


class Viewer(BaseModel):
    blabla: t.Optional[bool] = None
