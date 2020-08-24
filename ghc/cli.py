import argparse
from dataclasses import dataclass
from typing import Any, List, Optional

from ghc import __version__
from ghc.exceptions import GitHubTokenUnsetError
from ghc.utils import get_env


@dataclass
class CliOption:
    owner: str

    fmt: str = 'json'
    token: Optional[str] = None
    topics: Optional[List[str]] = None
    filename: Optional[str] = None

    def __post_init__(self) -> None:
        self.fmt = self.fmt.lower()

        if self.token is None:
            self.token = get_env('GHC_TOKEN', ignore_error=True)

        self.exists_token()

    def exists_token(self) -> None:
        if not self.token:
            raise GitHubTokenUnsetError()


def get_parser() -> argparse.ArgumentParser:
    return argparse.ArgumentParser(
        prog='ghc',
        allow_abbrev=False,
        description='List up GitHub user / org repositories filtered by topics'
    )


def setup_options(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        'owner',
        help='Repository user or organization name to search'
    )

    parser.add_argument(
        '--token',
        help='''
        Personal Access Token to access repositories.
        Use the environment variable "GHC_TOKEN" instead.
        '''
    )

    parser.add_argument(
        '-t', '--topics',
        nargs='*',
        help='Filter repository using topics'
    )

    parser.add_argument(
        '-f', '--format',
        dest='fmt',
        default='json',
        choices=['json', 'md'],
        help='Format the results with json or md (markdown). Default is json'
    )

    parser.add_argument(
        '-o', '--output',
        dest='filename',
        help='Filename to output the results. Output stdout if not specified'
    )

    parser.add_argument(
        '-V', '--version',
        action='version',
        version='%(prog)s {}'.format(__version__),
        help='Show command version'
    )


def parse_options(args: Any = None) -> CliOption:
    parser = get_parser()
    setup_options(parser)
    options = vars(parser.parse_args(args))
    return CliOption(**options)
