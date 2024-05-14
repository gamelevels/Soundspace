from models.song import Song
from models.session import Session
from models.appvars import Globals
import src.renderui as UI
from math import ceil
import pygame as pg

def hit(song: Song) -> None:
    pg.mixer.Sound("../sounds/hit.wav").play()
    calculate(song.Session)

def miss(song: Song) -> None:
    calculate(song.Session, False)

def calculate(session: Session, hit: bool = True) -> None:
    session.NotesPlayed += 1
    if not hit:
        if session.Multiplier != 1:
            session.Multiplier -= 1

        session.Misses += 1
        session.Combo = 0


    if session.NotesPlayed > 0:
        session.Accuracy = round((session.Hits / session.NotesPlayed) * 100, 2)
    
    if hit:
        if session.Multiplier != Globals.maxMultiplier and session.Combo != 0:
            session.Multiplier = ceil(session.Combo/10)

        session.Hits += 1
        session.Combo += 1
        session.Score += Globals.baseScore * session.Multiplier




