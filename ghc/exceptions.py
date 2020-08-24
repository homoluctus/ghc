class Base(Exception):
    """ghc base exception class"""


class TemplateNotFoundError(Base):
    """Raised when the specified template is not found"""


class GitHubRequestError(Base):
    """Raised when GitHub responses status code is not 200"""


class GitHubTokenUnsetError(Base):
    """Raised when GitHub personal access token is not set"""

    msg = 'GitHub Personal Access Token is not set.\n' \
        + 'Please specify --token option or ' \
        + 'set environment variable "GHC_TOKEN"'

    def __init__(self) -> None:
        super().__init__(self.msg)


class ReportError(Base):
    """Raised when fails to output the results"""
