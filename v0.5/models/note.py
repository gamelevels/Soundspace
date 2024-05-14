from dataclasses import dataclass

@dataclass
class Note:
    X: int
    Y: int
    Delay: int
    Color: tuple