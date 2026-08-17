from dataclasses import dataclass


@dataclass(frozen=True)
class Root:
    fa: str
    ayn: str
    lam: str

    @property
    def letters(self) -> tuple[str, str, str]:
        return self.fa, self.ayn, self.lam

    @property
    def text(self) -> str:
        return f"{self.fa}{self.ayn}{self.lam}"