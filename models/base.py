from pydantic import BaseModel, ConfigDict, alias_generators


def _alias_generator(name: str) -> str:
    camel_name = alias_generators.to_camel(name)

    if camel_name.endswith('_'):
        camel_name = camel_name[:-1]

    return camel_name


class ModelBase(BaseModel):
    model_config = ConfigDict(extra='allow', alias_generator=_alias_generator, populate_by_name=True, strict=True)
