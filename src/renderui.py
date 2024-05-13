import pygame as pg
from models.song import Song
from models.appvars import Globals

def RenderSidePanels(xOffset: int) -> pg.Rect:
    return pg.Rect(Globals.screenWidth/2-Globals.sidePanelX/2+xOffset,
                Globals.screenHeight/2-Globals.SidePanelY/2,
                Globals.sidePanelX,
                Globals.SidePanelY)

def RenderMainPanel() -> pg.Rect:
    return pg.Rect(Globals.screenWidth/2-Globals.centerRectangleDimension/2,
                Globals.screenHeight/2-Globals.centerRectangleDimension/2,
                Globals.centerRectangleDimension,
                Globals.centerRectangleDimension)

def RenderBoundaries() -> pg.Rect:
    return pg.Rect((Globals.screenWidth/2-Globals.centerRectangleDimension/2)-25,
                (Globals.screenHeight/2-Globals.centerRectangleDimension/2)-150,
                Globals.centerRectangleDimension+50,
                Globals.centerRectangleDimension+50)

def RenderFont(label: str, font: pg.font):
    return font.render(label, True, (255, 255, 255))

def RenderText(screen: pg.display, text: str, font: pg.font, pos) -> None:
    textFont = font.render(text, True, (255, 255, 255))
    textLabel = textFont.get_rect(center=pos)
    screen.blit(textFont, textLabel)

def RenderUI(MainScreen: pg.display, currentSong: Song) -> None:
    pg.draw.rect(MainScreen, Globals.mainRectangleColor, RenderMainPanel(), 3, 12) 

    leftSide = RenderSidePanels(-450)
    rightSide = RenderSidePanels(450)

    pg.draw.rect(MainScreen, Globals.mainRectangleColor, leftSide, 4, 4) 
    pg.draw.rect(MainScreen, Globals.mainRectangleColor, rightSide, 4, 4) 

    pg.font.init()
    font = pg.font.SysFont('Arial', 36)
    RenderText(MainScreen, f"Song: {currentSong.Name}", font, (leftSide.centerx, leftSide.top + 40))

    font = pg.font.SysFont('calibri', 36)
    RenderText(MainScreen, "Combo", font, (leftSide.centerx, leftSide.top + 100))

    font = pg.font.SysFont('microsoft', 40)
    RenderText(MainScreen, str(currentSong.Session.Combo), font, (leftSide.centerx, leftSide.top + 140))
    RenderText(MainScreen, str(currentSong.Session.Score), font, leftSide.center)

    font = pg.font.SysFont(None, 36)
    RenderText(MainScreen, "Misses", font, (leftSide.centerx, leftSide.bottom - 180))

    font = pg.font.SysFont('microsoft', 40)
    RenderText(MainScreen, str(currentSong.Session.Misses), font, (leftSide.centerx, leftSide.bottom - 150))

    font = pg.font.SysFont(None, 36)
    RenderText(MainScreen, "Notes", font, (leftSide.centerx, leftSide.bottom - 100))
    RenderText(MainScreen, f"{currentSong.Session.Hits}/{currentSong.Session.NotesPlayed}", font, (leftSide.centerx, leftSide.bottom - 70))

    font = pg.font.SysFont(None, 50)
    RenderText(MainScreen, f"{currentSong.Session.Multiplier}x", font, (rightSide.centerx, rightSide.top + 60))

    font = pg.font.SysFont(None, 45)
    RenderText(MainScreen, f"{currentSong.Session.Accuracy}%", font, rightSide.center)
