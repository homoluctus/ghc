from ghc.cli import parse_options
from ghc.github import search_repositories_by_topics
from ghc.logger import get_logger
from ghc.reporter import report


logger = get_logger(__name__)


def main() -> bool:
    options = parse_options()

    try:
        result = search_repositories_by_topics(
            options.token, owner=options.owner, topics=options.topics)
    except Exception as err:
        logger.error(err)
        logger.error('Failed to request to GitHub')
        return False
    else:
        logger.info('Succeeded to request to GitHub')

    try:
        report(result, fmt=options.fmt, filename=options.filename)
    except Exception as err:
        logger.error(err)
        logger.error('Failed to output the result')
        return False
    else:
        logger.info('Completed report!!')

    return True


if __name__ == '__main__':
    main()
