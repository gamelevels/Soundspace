from dataclasses import dataclass

@dataclass
class Score:
    Text: str
    POS: tuple[int, int]
    StartMS: int
    DisplayMS: int