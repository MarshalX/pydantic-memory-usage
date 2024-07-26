# pydantic v2 memory usage with hundreds of complicated models 

I tried to simplify this abnormal number of completed models as much as possible. 
There are 412 pydantic models that use the same config with strict mode and population by name. 
The model itself uses Union and Tagged Union types a lot.
The models are loaded in the main module and then rebuilded in the separate module. 
The memory usage is growing more than 100MB per all models on startup.

Copied from another discussion:
> A little about load_models. Because of so deep, nested, and sometimes a bit recursive model structure this is important to load models in a strict order to resolve dependencies of each other. Keeping such order could be hard to achieve from our code generator. Which is a fully automated process. That's why model rebuilding happens in runtime when all the models are defined already. load_models at the end calls model_rebuild for each existing model but the model_rebuild method is pretty smart to does nothing if the model is completely loaded (all types are resolved correctly). So there is no overhead.

## Reproduce

Install main deps:
```bash
pip install pydantic typing_extensions
```

Install deps to reproduce memory growth:
```bash
pip install memory-profiler matplotlib
```

Run the command:
```bash
mprof run python -m main && mprof plot -o mprofile.png
```

## Results

### Used pydantic

```text
             pydantic version: 2.8.2
        pydantic-core version: 2.20.1
          pydantic-core build: profile=release pgo=false
                 install path: blabla/projects/pydantic-memory-usage/venv/lib/python3.9/site-packages/pydantic
               python version: 3.9.6 (default, Mar 29 2024, 10:51:09)  [Clang 15.0.0 (clang-1500.3.9.4)]
                     platform: macOS-14.5-arm64-arm-64bit
             related packages: typing_extensions-4.12.2
                       commit: unknown
```

### mprof

![results.png](results.png)

```text
Filename: blabla/projects/pydantic-memory-usage/models/models_loader.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    29     43.8 MiB     43.8 MiB           1   @profile
    30                                         def __rebuild_all_models() -> None:
    31                                             # load models to the scope
    32     43.8 MiB      0.0 MiB           1       import models  # noqa
    33     43.8 MiB      0.0 MiB           1       from models.unknown_type import UnknownType, UnknownInputType  # noqa
    34                                         
    35    121.3 MiB      0.0 MiB         369       for __model in __get_models_to_rebuild_set():
    36    121.3 MiB     77.5 MiB         368           __model.model_rebuild()


Filename: blabla/projects/pydantic-memory-usage/main.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4     18.5 MiB     18.5 MiB           1   @profile
     5                                         def main() -> None:
     6    121.3 MiB    102.8 MiB           1       import models  # noqa
```
