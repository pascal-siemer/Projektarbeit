from dataclasses import dataclass


@dataclass
class Request:
    Type: str
    Flags: list[str]
    Player: str
    Data: str
