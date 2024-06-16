from dataclasses import dataclass

@dataclass
class Globals:
    scoreMultiplierMap = {
        -2: -1.5,
        -1: -3.5,
        0: 0,
        1: 1.5,
        2: 3.5,
    }

    maxMultiplier = 12
    baseScore = 25
    
    spawnInSpeed = 300

    backgroundColor = "gray12"
    mainRectangleColor = (135,206,235) # skyblue

    whiteCyan = ((135,206,235), (255,255,255))

    rectangleBorder = 4
    rectangleRadius = 12

    screenWidth = 1920
    screenHeight = 1080
    screenSize = (screenWidth, screenHeight)

    centerRectangleDimension = 500

    sidePanelX = 300
    SidePanelY = 450
    
    baseOffset = 125

    noteSize = 125
    noteSizeStart = 75
    noteSizeDiff = noteSize - noteSizeStart
    
    spawnTranslate = (100 - noteSize)

    sizeScoreDiscrepancy = 90

    scoreDisplayMS = 500

