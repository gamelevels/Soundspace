from src import mapload
from src import boundaries
from src import noteload
from src import score
from src import renderui as UI
from models.appvars import Globals
from models.note import Note
import pygame as pg
from collections import deque

songName = "piles"

pg.mixer.pre_init(44100, -16, 2, 2048)

MainScreen = pg.display.set_mode((0,0), pg.FULLSCREEN)
FrameClock = pg.time.Clock()
BackgroundColor = pg.Color(Globals.backgroundColor)
LockedArea = UI.RenderBoundaries()
LockedArea.centerx -= 200
LockedArea.left += 135
LockedArea.top += 60

mySong = mapload.LoadSong(songName)
noteQueue = deque(mySong.Notes.queue)

StartTime = pg.time.get_ticks()
musicStarted = False

passedNotes = set()
hitNotes = set()

displayingNotes = set()

pg.init()

mouseCursor = pg.image.load("cursor.png").convert_alpha()

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            done = True
        elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            print(pg.mouse.get_pos())

    MainScreen.fill(BackgroundColor)
    boundaries.CheckBoundaries(LockedArea)

    UI.RenderUI(MainScreen, mySong)
    CurrentTime = pg.time.get_ticks()-500

    if CurrentTime > 0:
        if not musicStarted:
            pg.mixer.init()
            pg.mixer.music.load(f'maps/{songName}.mp3')
            pg.mixer.music.set_volume(.3)
            pg.mixer.music.play(-1)
            musicStarted = True

        largestNote: Note = Note(0,0,0,(0,0,0))
        largestSize = 0

        pg.mouse.set_visible(False)
        if pg.mouse.get_focused():
            MainScreen.blit(mouseCursor, pg.mouse.get_pos())

        for note in noteQueue:
            timeOffset = CurrentTime - note.Delay
            if 0 <= timeOffset <= Globals.spawnInSpeed: 
                size = Globals.noteSizeDiff + (Globals.noteSizeDiff * timeOffset/Globals.spawnInSpeed)
                noteRectangle = noteload.RenderNote(note.X, note.Y, int(size))

                if largestSize < size:
                    pg.draw.rect(MainScreen, (255,0,0,.50), noteRectangle, 0, 6)
                else:
                    pg.draw.rect(MainScreen, note.Color, noteRectangle, 6, 6)

                pg.display.flip()

                if note.Delay > largestNote.Delay:
                    largestNote = note
                    largestSize = size
                    mousePos = pg.mouse.get_pos()
                    if abs(mousePos[0] - noteRectangle.x) < 60 and abs(mousePos[1] - noteRectangle.y) < 60:
                        if 100-Globals.sizeScoreDiscrepancy < size <= 100:
                            if note.Delay not in hitNotes:
                                hit = pg.mixer.Sound("sounds/hit.wav")
                                hit.play()
                                score.hit(mySong)
                                passedNotes.add(note.Delay)
                                hitNotes.add(note.Delay)
                
            elif timeOffset > Globals.spawnInSpeed:
                if note.Delay not in passedNotes:
                    score.miss(mySong)
                    passedNotes.add(note.Delay)
                break 

        while noteQueue and CurrentTime - noteQueue[0].Delay > Globals.spawnInSpeed:
            noteQueue.popleft()

        pg.display.flip()
    FrameClock.tick(144)
