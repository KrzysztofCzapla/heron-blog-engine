from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional

import toml

DEFAULT_CONFIG_PATH = Path(__file__).parent.parent.absolute() / "pyproject.toml"


@dataclass
class HeronConfigFields:
    homepage: str = "homepage"
    repo: str = "repo"
    blog_page_template: str = "blog_page_template"
    main_page_template: str = "main_page_template"


@dataclass
class HeronConfigLoader:
    config: dict

    @classmethod
    def load(cls) -> dict:
        return toml.load(DEFAULT_CONFIG_PATH).get("heron-blog-engine")

    @classmethod
    def get_config(cls, key: Optional[str] = None) -> Any:
        """If key is provided return only the value, otherwise the whole config"""
        return cls.load().get(key) if key is not None else cls.load()