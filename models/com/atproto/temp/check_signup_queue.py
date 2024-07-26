import typing as t

from models import base


class Response(base.ModelBase):
    activated: bool
    estimated_time_ms: t.Optional[int] = None
    place_in_queue: t.Optional[int] = None
