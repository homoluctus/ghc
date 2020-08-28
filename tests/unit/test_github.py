from ghc.github import Repository
from tests.utils import load_json


def test_repository():
    source = load_json('source/repository.json')
    expectation = load_json('correct/repository.json')

    actual_result = [Repository(**x).to_dict() for x in source]

    assert actual_result == expectation
