
from objects.models.song import Song
from objects.models.note import Note
from source.logs import Logs
from objects.models.session import Session
from queue import Queue
from objects.globals import Globals


class Song:
    def GetSong(mapName: str) -> Song | None:
        try:
            song = open(f"../maps/{mapName}.text")
            if song is None:
                raise FileNotFoundError(f"Unable to locate song {mapName}!")
        
        except Exception as error:
            print(error)
        