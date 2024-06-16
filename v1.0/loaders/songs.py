
from objects.models.song import Song
from objects.models.note import Note
from source.logs import Logs
from objects.models.session import Session
from queue import Queue
from objects.globals import Globals

class Song:
    def GetSong(mapName: str) -> Song | None:
        try:
            song = open(f"../maps/{mapName}.txt")
            if song is None:
                raise FileNotFoundError(f"Unable to locate song {mapName}!")
        
            mapData = song.read().split(",")
            mapID = mapData[0]

            actualSong = Song(
                ID=mapID, 
                Name=mapName,
                Seconds=int(mapData[-1].split("|")[-1])/1000,
                Notes=Queue(maxsize=len(mapData)),
                Session=Session()
            )

            for note in mapData:
                if note != mapID:
                    noteData = note.split("|")
                    note = Note(
                        X = float(noteData[0]),
                        Y = float(noteData[1]),
                        Delay = int(noteData[2]),
                        Color = Globals.whiteCyan[0] if actualSong.Notes.qsize() % 3 == 0 else Globals.whiteCyan[1]
                    )

                    actualSong.Notes.put(note)

            return actualSong
        
        except Exception as e:
            return print(e)