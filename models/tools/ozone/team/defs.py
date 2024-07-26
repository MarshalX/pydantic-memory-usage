import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Member(base.ModelBase):
    did: str
    role: str
    created_at: t.Optional[str] = None
    disabled: t.Optional[bool] = None
    last_updated_by: t.Optional[str] = None
    profile: t.Optional['models.AppBskyActorDefs.ProfileViewDetailed'] = None
    updated_at: t.Optional[str] = None

    py_type: t.Literal['tools.ozone.team.defs#member'] = Field(
        default='tools.ozone.team.defs#member', alias='$type', frozen=True
    )


RoleAdmin = t.Literal[
    'tools.ozone.team.defs#roleAdmin'
]  #: Admin role. Highest level of access, can perform all actions.

RoleModerator = t.Literal['tools.ozone.team.defs#roleModerator']  #: Moderator role. Can perform most actions.

RoleTriage = t.Literal[
    'tools.ozone.team.defs#roleTriage'
]  #: Triage role. Mostly intended for monitoring and escalating issues.
