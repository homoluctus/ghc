from pathlib import Path

import pytest

from ghc.stream import FileHandler


class TestFileHandler:
    @pytest.fixture(params=['test.md', 'new/test.md'])
    def filename(self, request):
        filename = request.param
        yield filename
        Path(filename).unlink()

    def test_file_handler(self, filename: str):
        msg = 'hello world'

        with FileHandler(filename=filename) as fd:
            fd.write(msg)

        assert Path(filename).exists() is True

        with open(filename) as fd:
            actual_msg = fd.read().replace('\n', '')

        assert actual_msg == msg
