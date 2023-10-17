from dataclasses import dataclass, field
from functools import cached_property
from mechanics.element import Element

@dataclass
class Card:
    index: int
    name: str
    question: str
    response: str
    categ: Element
    image_file: str


    image_prompt: str | None = None

    def __repr__(self):
        message = f"{self.name}\n"
        message += f"{self.question}\n"
        message += f"{self.response}\n"
        message += f"{self.image_file}"
        return message

    def to_json(self):
        return {
            "index": self.index,
            "name": self.name,
            "categ": self.categ.name,
            "image_file": self.image_file,
        }

    @cached_property
    def snake_case_name(self):
        return self.name.lower().replace(" ", "_")
