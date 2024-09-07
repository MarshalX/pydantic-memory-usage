# pydantic v2 memory usage with hundreds of complicated models 

I tried to simplify the large number of complicated models as much as possible. 412 Pydantic models share the same configuration, using strict mode and population by name. The models extensively employ Union and Tagged Union types. They are loaded in the main module and then rebuilt in a separate module. The memory usage increases by over 100MB for all models upon startup.

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

## Results with `2.8.2`

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

### time

5 runs of `time python main.py` (with commented `@profile`):
```text
python main.py  1.39s user 0.07s system 82% cpu 1.776 total
python main.py  1.32s user 0.05s system 97% cpu 1.402 total
python main.py  1.43s user 0.07s system 97% cpu 1.526 total
python main.py  1.38s user 0.06s system 99% cpu 1.444 total
python main.py  1.30s user 0.06s system 98% cpu 1.378 total
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

## Results with `2.9.0` 

### Used pydantic

```text
             pydantic version: 2.9.0
        pydantic-core version: 2.23.2
          pydantic-core build: profile=release pgo=false
                 install path: blabla/projects/pydantic-memory-usage/venv/lib/python3.9/site-packages/pydantic
               python version: 3.9.6 (default, Mar 29 2024, 10:51:09)  [Clang 15.0.0 (clang-1500.3.9.4)]
                     platform: macOS-14.6.1-arm64-arm-64bit
             related packages: typing_extensions-4.12.2
                       commit: unknown
```

### time

5 runs of `time python main.py` (with commented `@profile`):
```text
python main.py  1.13s user 0.08s system 81% cpu 1.483 total
python main.py  1.03s user 0.06s system 97% cpu 1.116 total
python main.py  1.16s user 0.06s system 97% cpu 1.256 total
python main.py  1.11s user 0.06s system 97% cpu 1.209 total
python main.py  1.04s user 0.06s system 98% cpu 1.118 total
```

### mprof

![results_new.png](results_new.png)

```text
Filename: blabla/projects/pydantic-memory-usage/models/models_loader.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    29     49.0 MiB     49.0 MiB           1   @profile
    30                                         def __rebuild_all_models() -> None:
    31                                             # load models to the scope
    32     49.0 MiB      0.0 MiB           1       import models  # noqa
    33     49.0 MiB      0.0 MiB           1       from models.unknown_type import UnknownType, UnknownInputType  # noqa
    34                                         
    35    129.2 MiB      0.0 MiB         369       for __model in __get_models_to_rebuild_set():
    36    129.2 MiB     80.2 MiB         368           __model.model_rebuild()


Filename: blabla/projects/pydantic-memory-usage/main.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4     19.4 MiB     19.4 MiB           1   @profile
     5                                         def main() -> None:
     6    129.3 MiB    109.8 MiB           1       import models  # noqa
```
