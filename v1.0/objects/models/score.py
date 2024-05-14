from dataclasses import dataclass

@dataclass
class Score:
    Text: str
    POS: tuple[int, int]
    StartMS: int
    DisplayMS: int = 500
    YIndexGrow: int = 0