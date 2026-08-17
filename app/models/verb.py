from dataclasses import dataclass

from app.core.root import Root
from app.core.bab import Bab


@dataclass(frozen=True)
class Verb:
    root: Root
    bab: Bab
    past: str
    present: str