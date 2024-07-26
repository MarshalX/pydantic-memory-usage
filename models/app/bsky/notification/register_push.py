from models import base


class Data(base.ModelBase):
    app_id: str
    platform: str
    service_did: str
    token: str
