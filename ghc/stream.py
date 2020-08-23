import sys
from dataclasses import dataclass, field
from typing import IO, Optional, Union


@dataclass
class StreamHandler:
    stream: IO[str] = sys.stdout

    def __enter__(self) -> IO[str]:
        return self._open()

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.close()

    def _open(self) -> IO[str]:
        return self.stream

    def flush(self) -> None:
        try:
            if self.stream and hasattr(self.stream, 'flush'):
                self.stream.flush()
        except Exception:
            pass

    def close(self) -> None:
        pass


@dataclass
class FileHandler(StreamHandler):
    filename: str

    mode: str = 'wt'
    encoding: str = 'utf-8'
    newline: Optional[str] = None

    stream: Optional[IO[str]] = field(init=False, default=None)  # type: ignore

    def _open(self) -> IO[str]:
        if self.stream is None:
            self.stream = open(
                self.filename, mode=self.mode,
                newline=self.newline, encoding=self.encoding)
        return self.stream

    def close(self) -> None:
        if self.stream:
            self.stream.close()


def stream(
        filename: Optional[str] = None) -> Union[FileHandler, StreamHandler]:
    if filename:
        return FileHandler(filename)
    return StreamHandler()
