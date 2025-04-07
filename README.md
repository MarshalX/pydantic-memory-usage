# pydantic v2 memory usage with hundreds of models 

> [!NOTE]  
> That was a long journey. 
> I started with Pydantic v2.8.2 and ended up with v2.11.2. 
> The memory usage was reduced from 121MB to 64MB, which is a significant improvement.
> The time was reduced from 1.4s to 0.6s, which is also a significant improvement.

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

## Results with `2.11.2` 

### Used pydantic

```text
             pydantic version: 2.11.2
        pydantic-core version: 2.33.1
          pydantic-core build: profile=release pgo=false
                 install path: blabla/projects/pydantic-memory-usage/venv/lib/python3.9/site-packages/pydantic
               python version: 3.9.6 (default, Mar 12 2025, 20:22:46)  [Clang 17.0.0 (clang-1700.0.13.3)]
                     platform: macOS-15.3.2-arm64-arm-64bit
             related packages: typing_extensions-4.12.2
                       commit: unknown
```

### time

5 runs of `time python main.py` (with commented `@profile`):
```text
python main.py  5.86s user 0.08s system 98% cpu 6.065 total
python main.py  0.59s user 0.05s system 93% cpu 0.679 total
python main.py  0.60s user 0.05s system 93% cpu 0.690 total
python main.py  0.59s user 0.05s system 93% cpu 0.687 total
python main.py  0.56s user 0.05s system 93% cpu 0.650 total
python main.py  0.51s user 0.05s system 93% cpu 0.595 total
```

### mprof

![results_new.png](results_new.png)

```text
Filename: blabla/projects/pydantic-memory-usage/models/models_loader.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    29     33.7 MiB     33.7 MiB           1   @profile
    30                                         def __rebuild_all_models() -> None:
    31                                             # load models to the scope
    32     33.7 MiB      0.0 MiB           1       import models  # noqa
    33     33.7 MiB      0.0 MiB           1       from models.unknown_type import UnknownType, UnknownInputType  # noqa
    34                                         
    35     64.7 MiB      0.0 MiB         369       for __model in __get_models_to_rebuild_set():
    36     64.7 MiB     30.9 MiB         368           __model.model_rebuild()


Filename: blabla/projects/pydantic-memory-usage/main.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4     17.5 MiB     17.5 MiB           1   @profile
     5                                         def main() -> None:
     6     64.7 MiB     47.2 MiB           1       import models  # noqa
```
