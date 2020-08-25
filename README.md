# ghc (GitHub Collector)

![PyPI](https://img.shields.io/pypi/v/ghc)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ghc)
![GitHub](https://img.shields.io/github/license/homoluctus/ghc)

List up GitHub user / org repositories filtered by topics

<!-- TOC depthFrom:2 -->

- [Feature](#feature)
- [Installtion](#installtion)
- [Usage](#usage)
- [Examples](#examples)
  - [Output JSON](#output-json)
  - [Output Markdown](#output-markdown)
  - [Use GHC_TOKEN instead of --token option](#use-ghc_token-instead-of---token-option)
- [Roadmap](#roadmap)

<!-- /TOC -->

## Feature

- List up GitHub org repositories
  - filtered by topics
- Support several formats
  - JSON
  - Markdown
- Output the results to stdout or file

## Installtion

```bash
pip install ghc
```

## Usage

```
usage: ghc [-h] [--token TOKEN] [-t [TOPICS [TOPICS ...]]] [-f {json,md}] [-o FILENAME] [-V] owner

List up GitHub user / org repositories filtered by topics

positional arguments:
  owner                 Repository user or organization name to search

optional arguments:
  -h, --help            show this help message and exit
  --token TOKEN         Personal Access Token to access the private repository. Use the environment variable "GHC_TOKEN" instead.
  -t [TOPICS [TOPICS ...]], --topics [TOPICS [TOPICS ...]]
                        Filter repository using topics
  -f {json,md}, --format {json,md}
                        Format the results with json or md (markdown). Default is json
  -o FILENAME, --output FILENAME
                        Filename to output the results. Output stdout if not specified
  -V, --version         Show command version
```

## Examples

### Output JSON

```bash
ghc homoluctus --token xxxxxxxx -f json -t python
```

<details>
<summary>Result</summary>

```json
{
  "count": 11,
  "repositories": [
    {
      "description": null,
      "is_archive": false,
      "is_template": false,
      "language": "Python",
      "language_logo_url": "https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python_24x24.png",
      "name": "algorithms",
      "url": "https://github.com/homoluctus/algorithms"
    },
    {
      "description": "Sample for logging decorator",
      "is_archive": false,
      "is_template": false,
      "language": "Python",
      "language_logo_url": "https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python_24x24.png",
      "name": "decolog",
      "url": "https://github.com/homoluctus/decolog"
    },
    {
      "description": "This tool helps to migrate DynamoDB to MySQL",
      "is_archive": false,
      "is_template": false,
      "language": "Python",
      "language_logo_url": "https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python_24x24.png",
      "name": "dymy",
      "url": "https://github.com/homoluctus/dymy"
    },
    {
      "description": "Scan the vulnerability of Docker images stored in ECR",
      "is_archive": false,
      "is_template": false,
      "language": "Python",
      "language_logo_url": "https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python_24x24.png",
      "name": "ecranner",
      "url": "https://github.com/homoluctus/ecranner"
    },
    {
      "description": "List up GitHub user / org repositories filtered by topics (ghc = GitHub Collector)",
      "is_archive": false,
      "is_template": false,
      "language": "Python",
      "language_logo_url": "https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python_24x24.png",
      "name": "ghc",
      "url": "https://github.com/homoluctus/ghc"
    },
    {
      "description": "Python logging outputs as JSON",
      "is_archive": false,
      "is_template": false,
      "language": "Python",
      "language_logo_url": "https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python_24x24.png",
      "name": "json-pyformatter",
      "url": "https://github.com/homoluctus/json-pyformatter"
    },
    {
      "description": "Analysis tool for Postfix log in /var/log/maillog",
      "is_archive": false,
      "is_template": false,
      "language": "Python",
      "language_logo_url": "https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python_24x24.png",
      "name": "maillogger",
      "url": "https://github.com/homoluctus/maillogger"
    },
    {
      "description": "Notify today's wether information",
      "is_archive": false,
      "is_template": false,
      "language": "Python",
      "language_logo_url": "https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python_24x24.png",
      "name": "ohtenki",
      "url": "https://github.com/homoluctus/ohtenki"
    },
    {
      "description": "Audit action for python dependencies (requirements.txt, Pipfile and poetry.lock)",
      "is_archive": false,
      "is_template": false,
      "language": "Shell",
      "language_logo_url": null,
      "name": "pip-audit-action",
      "url": "https://github.com/homoluctus/pip-audit-action"
    },
    {
      "description": "The CLI tool to query AWS CloudWatch Logs Insights :mag:",
      "is_archive": false,
      "is_template": false,
      "language": "Python",
      "language_logo_url": "https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python_24x24.png",
      "name": "pyinsights",
      "url": "https://github.com/homoluctus/pyinsights"
    },
    {
      "description": "GitHub template for Python3.8",
      "is_archive": false,
      "is_template": true,
      "language": "Makefile",
      "language_logo_url": null,
      "name": "python-template",
      "url": "https://github.com/homoluctus/python-template"
    }
  ]
}
```

</details>

### Output Markdown


```bash
nghc homoluctus --token xxxxxxx -f md -t python
```

<details>
<summary>Result (Raw)</summary>

```markdown
# Repositories

Total Count: 11

|Name|URL|Language|Description|
|:--:|:--:|:--:|:--|
|algorithms|https://github.com/homoluctus/algorithms|![Python](https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python_24x24.png)|None|
|decolog|https://github.com/homoluctus/decolog|![Python](https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python_24x24.png)|Sample for logging decorator|
|dymy|https://github.com/homoluctus/dymy|![Python](https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python_24x24.png)|This tool helps to migrate DynamoDB to MySQL|
|ecranner|https://github.com/homoluctus/ecranner|![Python](https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python_24x24.png)|Scan the vulnerability of Docker images stored in ECR|
|ghc|https://github.com/homoluctus/ghc|![Python](https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python_24x24.png)|List up GitHub user / org repositories filtered by topics (ghc = GitHub Collector)|
|json-pyformatter|https://github.com/homoluctus/json-pyformatter|![Python](https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python_24x24.png)|Python logging outputs as JSON|
|maillogger|https://github.com/homoluctus/maillogger|![Python](https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python_24x24.png)|Analysis tool for Postfix log in /var/log/maillog|
|ohtenki|https://github.com/homoluctus/ohtenki|![Python](https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python_24x24.png)|Notify today&#39;s wether information|
|pip-audit-action|https://github.com/homoluctus/pip-audit-action|Shell|Audit action for python dependencies (requirements.txt, Pipfile and poetry.lock)|
|pyinsights|https://github.com/homoluctus/pyinsights|![Python](https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python_24x24.png)|The CLI tool to query AWS CloudWatch Logs Insights :mag:|
|python-template ![template](https://img.shields.io/badge/template-green.svg)|https://github.com/homoluctus/python-template|Makefile|GitHub template for Python3.8|

> Generated by [ghc](https://github.com/homoluctus/ghc)

```

</details>

<details>
<summary>Result</summary>

# Repositories

Total Count: 11

|Name|URL|Language|Description|
|:--:|:--:|:--:|:--|
|algorithms|https://github.com/homoluctus/algorithms|![Python](https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python_24x24.png)|None|
|decolog|https://github.com/homoluctus/decolog|![Python](https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python_24x24.png)|Sample for logging decorator|
|dymy|https://github.com/homoluctus/dymy|![Python](https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python_24x24.png)|This tool helps to migrate DynamoDB to MySQL|
|ecranner|https://github.com/homoluctus/ecranner|![Python](https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python_24x24.png)|Scan the vulnerability of Docker images stored in ECR|
|ghc|https://github.com/homoluctus/ghc|![Python](https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python_24x24.png)|List up GitHub user / org repositories filtered by topics (ghc = GitHub Collector)|
|json-pyformatter|https://github.com/homoluctus/json-pyformatter|![Python](https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python_24x24.png)|Python logging outputs as JSON|
|maillogger|https://github.com/homoluctus/maillogger|![Python](https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python_24x24.png)|Analysis tool for Postfix log in /var/log/maillog|
|ohtenki|https://github.com/homoluctus/ohtenki|![Python](https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python_24x24.png)|Notify today&#39;s wether information|
|pip-audit-action|https://github.com/homoluctus/pip-audit-action|Shell|Audit action for python dependencies (requirements.txt, Pipfile and poetry.lock)|
|pyinsights|https://github.com/homoluctus/pyinsights|![Python](https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python_24x24.png)|The CLI tool to query AWS CloudWatch Logs Insights :mag:|
|python-template ![template](https://img.shields.io/badge/template-green.svg)|https://github.com/homoluctus/python-template|Makefile|GitHub template for Python3.8|

> Generated by [ghc](https://github.com/homoluctus/ghc)

</details>

### Use GHC_TOKEN instead of --token option

```bash
GHC_TOKEN=xxxxxxxx ghc homoluctus -f json -t python aws
```

## Roadmap

- [ ] Ignore filter
- [ ] Output to user-defined template
