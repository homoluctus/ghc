from dataclasses import dataclass
from typing import ClassVar, List, Optional


@dataclass
class LanguageLogo:
    url: ClassVar[str] = 'https://cdn.jsdelivr.net/npm/' \
        + 'programming-languages-logos/src/{lang}/{lang}_24x24.png'

    supported_lang: ClassVar[List[str]] = [
        'c', 'csharp', 'cpp', 'css', 'go', 'haskell',
        'html', 'java', 'javascript', 'kotlin', 'lua',
        'php', 'python', 'r', 'ruby', 'swift', 'typescript'
    ]

    @classmethod
    def from_lang(cls, lang: str) -> Optional[str]:
        lang = lang.lower()
        if lang in cls.supported_lang:
            return cls.url.format(lang=lang)
        return None
