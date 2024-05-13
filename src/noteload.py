from models.appvars import Globals
import pygame

def RenderNote(xOffset: float, yOffset: float, size: int = None) -> pygame.Rect:
    xOffset *= 125
    yOffset *= 125

    screenWidth = Globals.screenWidth
    screenHeight = Globals.screenHeight

    spawnTranslate = (100 - Globals.noteSize)

    if xOffset == 0:
        xOffset -= 25 + spawnTranslate
    elif xOffset == 250:
        xOffset += 25 + spawnTranslate
    elif yOffset == 0:
        yOffset -= 25 + spawnTranslate
    else:
        yOffset += 25 + spawnTranslate

    xOffset = min(max(0, xOffset), screenWidth - Globals.noteSize)
    yOffset = min(max(0, yOffset), screenHeight - Globals.noteSize)

    noteSize = Globals.noteSize
    if size != None:
        noteSize = size

    return pygame.Rect((screenWidth/2-noteSize/2)-Globals.baseOffset+yOffset,
            (screenHeight/2-noteSize/2)-Globals.baseOffset+xOffset,
            noteSize,
            noteSize)
    

