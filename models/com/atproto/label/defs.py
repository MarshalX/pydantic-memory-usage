import typing as t

from pydantic import Field

if t.TYPE_CHECKING:
    import models
from models import base


class Label(base.ModelBase):
    cts: str
    src: str
    uri: str
    val: str = Field(max_length=128)
    cid: t.Optional[str] = None
    exp: t.Optional[str] = None
    neg: t.Optional[bool] = None
    sig: t.Optional[t.Union[str, bytes]] = None
    ver: t.Optional[int] = None

    py_type: t.Literal['com.atproto.label.defs#label'] = Field(
        default='com.atproto.label.defs#label', alias='$type', frozen=True
    )


class SelfLabels(base.ModelBase):
    values: t.List['models.ComAtprotoLabelDefs.SelfLabel'] = Field(max_length=10)

    py_type: t.Literal['com.atproto.label.defs#selfLabels'] = Field(
        default='com.atproto.label.defs#selfLabels', alias='$type', frozen=True
    )


class SelfLabel(base.ModelBase):
    val: str = Field(max_length=128)

    py_type: t.Literal['com.atproto.label.defs#selfLabel'] = Field(
        default='com.atproto.label.defs#selfLabel', alias='$type', frozen=True
    )


class LabelValueDefinition(base.ModelBase):
    blurs: str
    identifier: str = Field(max_length=100)
    locales: t.List['models.ComAtprotoLabelDefs.LabelValueDefinitionStrings']
    severity: str
    adult_only: t.Optional[bool] = None
    default_setting: t.Optional[str] = None

    py_type: t.Literal['com.atproto.label.defs#labelValueDefinition'] = Field(
        default='com.atproto.label.defs#labelValueDefinition', alias='$type', frozen=True
    )


class LabelValueDefinitionStrings(base.ModelBase):
    description: str = Field(max_length=100000)
    lang: str
    name: str = Field(max_length=640)

    py_type: t.Literal['com.atproto.label.defs#labelValueDefinitionStrings'] = Field(
        default='com.atproto.label.defs#labelValueDefinitionStrings', alias='$type', frozen=True
    )


LabelValue = t.Union[
    t.Literal['!hide'],
    t.Literal['!no-promote'],
    t.Literal['!warn'],
    t.Literal['!no-unauthenticated'],
    t.Literal['dmca-violation'],
    t.Literal['doxxing'],
    t.Literal['porn'],
    t.Literal['sexual'],
    t.Literal['nudity'],
    t.Literal['nsfl'],
    t.Literal['gore'],
]  #: Label value
