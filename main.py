from memory_profiler import profile


@profile
def main() -> None:
    import models  # noqa


if __name__ == '__main__':
    main()
