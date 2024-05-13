from dataclasses import dataclass

@dataclass
class Session:
    Multiplier: int = 1

    Combo: int = 0

    Score: int = 0
    
    Misses: int = 0
    Hits: int = 0
    NotesPlayed: int = 0
    
    TimeRemaining: int = 0 
    Accuracy: float = 0