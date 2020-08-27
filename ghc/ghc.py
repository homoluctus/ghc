import sys

from ghc.cli import parse_options
from ghc.exceptions import (
    GitHubRequestError, GitHubTokenUnsetError, ReportError,
    TemplateNotFoundError
)
from ghc.github import search_repositories_by_topics
from ghc.logger import get_logger
from ghc.reporter import report


logger = get_logger(__name__)


def main() -> bool:
    logger.info('START')

    try:
        options = parse_options()

        result = search_repositories_by_topics(
            options.token, owner=options.owner, topics=options.topics)
        logger.info('Succeeded to request to GitHub')

        report(result, fmt=options.fmt, filename=options.filename)
        logger.info('Completed report!!')
    except GitHubTokenUnsetError as err:
        logger.error(err)
        sys.exit(1)
    except GitHubRequestError as err:
        logger.error(err)
        logger.error('Failed to request to GitHub')
        sys.exit(1)
    except (TemplateNotFoundError, ReportError) as err:
        logger.error(err)
        logger.error('Failed to output the result')
        sys.exit(1)
    except Exception as err:
        logger.error(err)
        sys.exit(1)

    logger.info('DONE')
    return True


if __name__ == '__main__':
    sys.exit(main())
