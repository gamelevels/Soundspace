from dataclasses import dataclass
from objects.globals import Globals

'''
speed multiplier:
    display faster
    more score per combo
'''

@dataclass
class Session:
    def __init__(self, SpeedMultiplier: int = 0) -> None:
        self.Multiplier: int = 1
        self.Score: int = 0

        self.Combo: int = 0

        self.Misses: int = 0
        self.Hits: int = 0
        self.NotePlayed: int = 0
        
        self.TimeRemaining: int = 0
        self.Accuracy: float = 0


        # Logic to work out eventually
        #self.SpeedMultiplier = SpeedMultiplier
        #self.DisplaySpeed: int = 100

    # @property
    # def Multiplier(self) -> int:
    #     return
    
    # @Multiplier.setter
    # def Multiplier(self, multi: int) -> None:
    #     self._multiplier: int = 1 + Globals.ScoreMultiplierMap[self.SpeedMultiplier]
         
