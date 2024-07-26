import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Response(base.ModelBase):
    available_user_domains: t.List[str]
    did: str
    contact: t.Optional['models.ComAtprotoServerDescribeServer.Contact'] = None
    invite_code_required: t.Optional[bool] = None
    links: t.Optional['models.ComAtprotoServerDescribeServer.Links'] = None
    phone_verification_required: t.Optional[bool] = None


class Links(base.ModelBase):
    privacy_policy: t.Optional[str] = None
    terms_of_service: t.Optional[str] = None

    py_type: t.Literal['com.atproto.server.describeServer#links'] = Field(
        default='com.atproto.server.describeServer#links', alias='$type', frozen=True
    )


class Contact(base.ModelBase):
    email: t.Optional[str] = None

    py_type: t.Literal['com.atproto.server.describeServer#contact'] = Field(
        default='com.atproto.server.describeServer#contact', alias='$type', frozen=True
    )
