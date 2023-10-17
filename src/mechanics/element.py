from dataclasses import dataclass


@dataclass
class Element:
    name: str

    def with_ascii_color(self, text: str) -> str:
        return f"{text}\033[0m"

    def __repr__(self):
        return self.name
    
    def __hash__(self) -> int:
        return hash(self.name)
