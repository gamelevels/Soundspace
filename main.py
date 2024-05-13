from src import mapload
from src import boundaries
from src import noteload
from src import score
from src import renderui as UI
from models.score import Score
from models.appvars import Globals
from models import handler as Handler
from models.note import Note
import pygame as pg
from collections import deque
from random import randint

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

nextTimeInterval = 0

mouseCursor = pg.image.load("cursor.png").convert_alpha()

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            done = True

    MainScreen.fill(BackgroundColor)
    boundaries.CheckBoundaries(LockedArea)

    UI.RenderUI(MainScreen, mySong)
    CurrentTime = pg.time.get_ticks()-500
    UI.RenderScoreDisplay(MainScreen, CurrentTime)
    MainPanel =  UI.RenderMainPanel()
    ScorePOS = [MainPanel.center[0] + randint(-100,100), MainPanel.center[1] + 280 + randint(-10,10)]
    TimePOS = [MainPanel.center[0], MainPanel.center[1] - 270]

    if CurrentTime > 0:
        if not musicStarted:
            pg.mixer.init()
            pg.mixer.music.load(f'maps/{songName}.mp3')
            pg.mixer.music.set_volume(.3)
            pg.mixer.music.play(-1)
            musicStarted = True

        UI.RenderTimeRemaining(MainScreen, mySong.Seconds + mySong.Session.TimeRemaining, TimePOS)

        print(f"current: {CurrentTime} | seconds: {mySong.Seconds} | remaining: {mySong.Session.TimeRemaining}")
        if CurrentTime > nextTimeInterval:
            nextTimeInterval += 1000
            mySong.Session.TimeRemaining -= 1

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
                                # need to rewrite this, kept adding to it and didnt organize it properly
                                # will refactor with a v2
                                scoredisplay = Score(Text=f"+{mySong.Session.Multiplier * Globals.baseScore}", POS=ScorePOS, StartMS=CurrentTime, DisplayMS=500)
                                Handler.Handler.displayScore.append(scoredisplay)
                                Handler.HandleScore(CurrentTime)
                                
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
