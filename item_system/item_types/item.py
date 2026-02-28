# ruff: noqa

from dataclasses import dataclass
from uuid import uuid4


@dataclass(kw_only=True)
class Item:
    name: str
    id: str = str(uuid4())
