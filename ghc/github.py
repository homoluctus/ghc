from dataclasses import InitVar, asdict, dataclass, field
from operator import itemgetter
from typing import Any, ClassVar, Dict, List, Optional, Tuple, Union

import requests

from ghc.exceptions import GitHubRequestError
from ghc.logo import LanguageLogo
from ghc.query import SEARCH_REPOSITORY


@dataclass
class Repository:
    isArchived: InitVar[bool]
    isTemplate: InitVar[bool]
    primaryLanguage: InitVar[Optional[Dict[str, str]]]

    name: str
    url: str
    description: Optional[str] = ''
    language: Optional[str] = field(init=False, default=None)
    language_logo_url: Optional[str] = field(init=False, default=None)
    is_archive: bool = field(init=False)
    is_template: bool = field(init=False)

    def __post_init__(self, isArchived, isTemplate, primaryLanguage) -> None:
        self.is_archive = isArchived
        self.is_template = isTemplate

        if primaryLanguage and (lang := primaryLanguage.get('name')):
            self.language = lang
            self.language_logo_url = LanguageLogo.from_lang(lang)

    def to_dict(self) -> Dict[str, Union[str, bool]]:
        return asdict(self)


@dataclass
class SearchQueryString:
    delimiter: ClassVar[str] = ' '
    q_user: ClassVar[str] = 'user:{user}'
    q_topic: ClassVar[str] = 'topic:{topic}'

    owner: str
    topics: Optional[List[str]] = None

    def to_string(self) -> str:
        query = self.q_user.format(user=self.owner)

        if self.topics:
            topics_str = [self.q_topic.format(topic=t) for t in self.topics]
            query += f'{self.delimiter}{self.delimiter.join(topics_str)}'

        return query


@dataclass
class GraphqlVariables:
    search_query_str: Optional[str] = None
    end_cursor: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class GitHub:
    url: ClassVar[str] = 'https://api.github.com/graphql'

    token: Optional[str] = None

    def build_headers(self) -> Dict[str, str]:
        headers = {}

        if self.token:
            headers['Authorization'] = f'token {self.token}'

        return headers

    def request(
            self,
            variables: GraphqlVariables,
            timeout: Union[int, Tuple[float, float]] = (20, 60),) -> Any:
        payload = {
            'query': SEARCH_REPOSITORY,
            'variables': variables.to_dict()
        }

        headers = self.build_headers()
        res = requests.post(
            self.url, headers=headers,
            json=payload, timeout=timeout)

        if res.status_code != 200:
            res.raise_for_status()

        try:
            body = res.json()
            result: Dict[str, Any] = body['data']['search']
        except KeyError:
            raise GitHubRequestError(f'Unexpected response: {res}')

        if (pagination := result.get('pageInfo')) \
                and pagination.get('hasNextPage'):
            variables.end_cursor = pagination['endCursor']
            tmp = self.request(variables=variables, timeout=timeout)
            result['edges'].extend(tmp['edges'])

        return result


def search_repositories_by_topics(
        token: Optional[str] = None,
        **kwargs: Any) -> Dict[str, Any]:
    client = GitHub(token=token)
    search_query_str = SearchQueryString(**kwargs).to_string()

    res = client.request(variables=GraphqlVariables(search_query_str))
    result = {'count': res['repositoryCount']}
    tmp = [
        Repository(**edge['node']).to_dict()
        for edge in res['edges']]
    result['repositories'] = sorted(tmp, key=itemgetter('name'))
    return result
