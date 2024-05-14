
from objects.models.song import Song
from objects.models.note import Note
from objects.models.session import Session
from queue import Queue
from objects.globals import Globals


class Song:
    def __init__(self):
        return
    
    @property
    def song(self) -> Song | None:
        return
    
    @song.setter
    def song(self, mapName: str) -> None:
