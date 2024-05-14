from dataclasses import dataclass

@dataclass
class Globals:
    ScoreMultiplierMap = {
        -2: -1.5,
        -1: -3.5,
        0: 0,
        1: 1.5,
        2: 3.5,
    }