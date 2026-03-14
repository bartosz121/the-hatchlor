from importlib.metadata import PackageNotFoundError, version

try:  # noqa: RUF067
    __version__ = version("{{ cookiecutter.project_slug }}")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError
