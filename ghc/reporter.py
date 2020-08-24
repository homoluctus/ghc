import json
from dataclasses import InitVar, dataclass, field
from pathlib import Path
from typing import IO, Any, Optional

from jinja2 import Environment, FileSystemLoader, Template

from ghc.exceptions import ReportError, TemplateNotFoundError
from ghc.stream import stream


@dataclass
class Reporter:
    def report(self, fd: IO[str], record: Any) -> None:
        raise NotImplementedError()


@dataclass
class JsonReporter(Reporter):
    indent: int = 2
    ensure_ascii: bool = False
    allow_nan: bool = True
    sort_keys: bool = True

    def report(self, fd: IO[str], record: Any) -> None:
        json.dump(
            record, fd, indent=self.indent,
            ensure_ascii=self.ensure_ascii, allow_nan=self.allow_nan,
            sort_keys=self.sort_keys)


BASE_DIR = Path(__file__).parent
TEMPLATE_DIR = f'{BASE_DIR}/templates'


@dataclass
class MrkdwnReporter(Reporter):
    tpl_path: InitVar[Optional[str]] = None

    search_path: str = field(init=False, default=TEMPLATE_DIR)
    template_name: str = field(init=False, default='default.j2')

    def __post_init__(self, tpl_path: Optional[str] = None) -> None:
        if tpl_path:
            p = Path(tpl_path)
            self.exists(p)
            self.search_path = str(p.parent)
            self.template_name = p.name

    @staticmethod
    def exists(tpl_path: Path) -> None:
        if tpl_path.exists() is False:
            raise TemplateNotFoundError(f'{tpl_path!r} is not found')

    def load_template(self) -> Template:
        env = Environment(
            loader=FileSystemLoader(self.search_path),
            autoescape=True,
            keep_trailing_newline=True)
        return env.get_template(self.template_name)

    def report(self, fd: IO[str], record: Any) -> None:
        tpl = self.load_template()
        tpl.stream(record).dump(fd)


REPORTER_MAP = {
    'json': JsonReporter,
    'md': MrkdwnReporter
}


def report(record: Any, fmt: str, filename: Optional[str] = None) -> None:
    try:
        with stream(filename) as fd:
            reporter = REPORTER_MAP[fmt]()
            reporter.report(fd, record)
    except TemplateNotFoundError:
        raise
    except Exception as err:
        raise ReportError(err)
