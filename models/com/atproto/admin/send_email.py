import typing as t

from models import base


class Data(base.ModelBase):
    content: str
    recipient_did: str
    sender_did: str
    comment: t.Optional[str] = None
    subject: t.Optional[str] = None


class Response(base.ModelBase):
    sent: bool
