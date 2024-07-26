from models import base


class Response(base.ModelBase):
    activated: bool
    expected_blobs: int
    imported_blobs: int
    indexed_records: int
    private_state_values: int
    repo_blocks: int
    repo_commit: str
    repo_rev: str
    valid_did: bool
