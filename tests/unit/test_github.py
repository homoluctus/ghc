from typing import List, Optional

import pytest

from ghc.github import Repository, SearchQueryString
from tests.utils import load_json


def test_repository():
    source = load_json('source/repository.json')
    expectation = load_json('correct/repository.json')

    actual_result = [Repository(**x).to_dict() for x in source]

    assert actual_result == expectation


@pytest.mark.parametrize(
    'owner, topics, expectation',
    (
        (
            'homoluctus',
            ['python'],
            'user:homoluctus topic:python'
        ),
        (
            'homoluctus',
            ['python', 'golang'],
            'user:homoluctus topic:python topic:golang'
        ),
        (
            'homoluctus',
            None,
            'user:homoluctus'
        ),
    )
)
def test_search_query_string(
        owner: str,
        topics: Optional[List[str]],
        expectation: str):
    q = SearchQueryString(owner, topics).to_string()
    assert q == expectation
