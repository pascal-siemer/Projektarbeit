from dataclasses import dataclass


@dataclass
class Question:
    prompt: str
    answers: list[str]
    indexCorrect: int
