from models.song import Song
from models.note import Note
from models.session import Session
from src.colors import NewRGB
from queue import Queue
from models.appvars import Globals


def LoadSong(songName: str) -> Song | None:
    try:
        with open(f"../maps/{songName}.txt", "r") as song:
            songData = song.read().split(",")
            songID = songData[0]

            actualSong = Song(
                ID=songID, 
                Name=songName,
                Seconds=int(songData[-1].split("|")[-1])/1000,
                Notes=Queue(maxsize=len(songData)),
                Session=Session()
            )

            for note in songData:
                if note != songID:
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
        print(e)
        return None