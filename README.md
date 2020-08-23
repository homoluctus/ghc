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
  - [Output markdown](#output-markdown)
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
  --token TOKEN         Personal Access Token to access the private repository
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
ghc homoluctus --token xxxxxxxx -f json -t python aws | jq
```

<details>
<summary>Result</summary>

```json
{
  "count": 2,
  "repositories": [
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
      "description": "Scan the vulnerability of Docker images stored in ECR",
      "is_archive": false,
      "is_template": false,
      "language": "Python",
      "language_logo_url": "https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python_24x24.png",
      "name": "ecranner",
      "url": "https://github.com/homoluctus/ecranner"
    }
  ]
}
```

</details>

### Output markdown


```bash
nghc homoluctus --token xxxxxxx -f md -t python aws
```

<details>
<summary>Result (Raw)</summary>

```markdown
# Repositories

Total Count: 2

|Name|URL|Language|Archived|Template|Description|
|:--:|:--:|:--:|:--:|:--:|:--|
|pyinsights|https://github.com/homoluctus/pyinsights|![Python](https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python_24x24.png)|False|False|The CLI tool to query AWS CloudWatch Logs Insights :mag:|
|ecranner|https://github.com/homoluctus/ecranner|![Python](https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python_24x24.png)|False|False|Scan the vulnerability of Docker images stored in ECR|

```

</details>

<details>
<summary>Result</summary>

# Repositories

Total Count: 2

|Name|URL|Language|Archived|Template|Description|
|:--:|:--:|:--:|:--:|:--:|:--|
|pyinsights|https://github.com/homoluctus/pyinsights|![Python](https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python_24x24.png)|False|False|The CLI tool to query AWS CloudWatch Logs Insights :mag:|
|ecranner|https://github.com/homoluctus/ecranner|![Python](https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python_24x24.png)|False|False|Scan the vulnerability of Docker images stored in ECR|

</details>

## Roadmap

- [ ] Ignore filter
- [ ] Output to user-defined template
