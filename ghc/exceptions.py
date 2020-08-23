class Base(Exception):
    """ghc base exception class"""


class TemplateNotFoundError(Base):
    """Raised when the specified template is not found"""


class GitHubRequestError(Base):
    """Raised when GitHub responses status code is not 200"""
