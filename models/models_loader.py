from memory_profiler import profile


def __get_models_to_rebuild_set() -> set:
    from types import ModuleType

    not_rebuilt_classes = {'BaseModel', 'ModelBase'}

    # use a set to remove duplicates
    models_to_rebuild = set()

    import models

    for var_name in dir(models).copy():
        var_value = getattr(models, var_name)
        if not isinstance(var_value, ModuleType):
            continue

        for name, value in vars(var_value).items():
            if name.startswith('_') or name in not_rebuilt_classes:
                continue

            if hasattr(value, 'model_rebuild'):
                models_to_rebuild.add(value)

    return models_to_rebuild


@profile
def __rebuild_all_models() -> None:
    # load models to the scope
    import models  # noqa
    from models.unknown_type import UnknownType, UnknownInputType  # noqa

    for __model in __get_models_to_rebuild_set():
        __model.model_rebuild()


def __on_load() -> None:
    __rebuild_all_models()


def load_models() -> None:
    __on_load()
