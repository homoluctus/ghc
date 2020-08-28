import json
from pathlib import Path
from typing import TypeVar


JsonType = TypeVar('JsonType')

BASE_DIR = Path(__file__).parent
FIXTURE_DIR = f'{BASE_DIR}/fixtures'


def load_json(filename: str) -> JsonType:
    fp = f'{FIXTURE_DIR}/{filename}'

    with open(fp) as fd:
        return json.load(fd)
