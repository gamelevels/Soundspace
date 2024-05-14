from dataclasses import dataclass
from models.song import Song
from models.score import Score
from src import renderui as UI
import pygame as pg

class Handler:
    displayScore: list[Score] = []

def HandleScore(CurrentTime: int):
    for score_display in Handler.displayScore:
        if CurrentTime - score_display.StartMS >= score_display.DisplayMS:
            Handler.displayScore.remove(score_display)