import typing as t

import typing_extensions as te
from pydantic import Field

if t.TYPE_CHECKING:
    import models
    from models.unknown_type import UnknownType
from models import base


class Data(base.ModelBase):
    repo: str
    writes: t.List[
        te.Annotated[
            t.Union[
                'models.ComAtprotoRepoApplyWrites.Create',
                'models.ComAtprotoRepoApplyWrites.Update',
                'models.ComAtprotoRepoApplyWrites.Delete',
            ],
            Field(discriminator='py_type'),
        ]
    ]
    swap_commit: t.Optional[str] = None
    validate_: t.Optional[bool] = None


class Create(base.ModelBase):
    collection: str
    value: 'UnknownType'
    rkey: t.Optional[str] = Field(default=None, max_length=15)

    py_type: t.Literal['com.atproto.repo.applyWrites#create'] = Field(
        default='com.atproto.repo.applyWrites#create', alias='$type', frozen=True
    )


class Update(base.ModelBase):
    collection: str
    rkey: str
    value: 'UnknownType'

    py_type: t.Literal['com.atproto.repo.applyWrites#update'] = Field(
        default='com.atproto.repo.applyWrites#update', alias='$type', frozen=True
    )


class Delete(base.ModelBase):
    collection: str
    rkey: str

    py_type: t.Literal['com.atproto.repo.applyWrites#delete'] = Field(
        default='com.atproto.repo.applyWrites#delete', alias='$type', frozen=True
    )
