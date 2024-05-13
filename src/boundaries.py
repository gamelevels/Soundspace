import pygame as pg

def CheckBoundaries(boundary: tuple) -> None:
    mx,my = pg.mouse.get_pos()
    if not boundary.collidepoint(mx, my):
        if mx < boundary.left:
            mx = boundary.left
        elif mx > boundary.right:
            mx = boundary.right
        if my < boundary.top:
            my = boundary.top
        elif my > boundary.bottom:
            my = boundary.bottom

        pg.mouse.set_pos(mx, my)