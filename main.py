from types import ModuleType

import models

# use a set to remove duplicates
models_to_rebuild = set()
not_rebuilt_classes = {'BaseModel',}

for var_name in dir(models).copy():
    var_value = getattr(models, var_name)
    if not isinstance(var_value, ModuleType):
        continue

    for name, value in vars(var_value).items():
        if name.startswith('_') or name in not_rebuilt_classes:
            continue

        if hasattr(value, 'model_rebuild'):
            models_to_rebuild.add(value)

print(f'Models to rebuild: {models_to_rebuild}')
for model in models_to_rebuild:
    print(f'Rebuilding {model}')
    model.model_rebuild()

print('Success')
