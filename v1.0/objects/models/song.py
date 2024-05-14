from dataclasses import dataclass
from models.note import Note
from models.session import Session
from queue import Queue

@dataclass
class Song:
    ID: int
    Name: str
    Seconds: int
    Notes: Queue
    Session: Session