import os
from typing import Any


def get_env(
        name: str,
        *,
        ignore_error: bool = False,
        default: Any = None) -> Any:
    try:
        os.environ[name]
    except KeyError as err:
        if ignore_error is False:
            raise err
        return default
