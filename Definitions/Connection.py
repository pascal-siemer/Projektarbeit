from dataclasses import dataclass
from typing import Any

from Definitions.Player import Player


@dataclass
class Connection:
    websocket: Any
    player: Player