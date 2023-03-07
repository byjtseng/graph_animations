import pygame as pyg
import math
import random

BLACK = (0,0,0)
pyg.init()
screen = pyg.display.set_mode([1200,800])
rect = screen.get_rect()
pyg.display.set_caption('Graphs')
pause = False
clock = pyg.time.Clock()
font = pyg.font.SysFont("Arial", 16)
yscale = 10
xscale = 3
xspeed = 3

def f(x):
    return ( x**3 - 4*x)

x = -xscale
xc = 0
dx = 2*xscale / rect.width

points = []

# main loop
while not pause:
    # player input testing
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            pause = True
          
    # pos = pygame.mouse.get_pos()
    
    screen.fill(BLACK)
    # updates the positions of everything
    y = f(x)
    yc = round(rect.centery - y / yscale * rect.height/2)
    
    if len(points) == 0 or points[-1] != (xc, yc):
        points.append( (xc, yc) )
    x += dx * xspeed
    xc += 1 * xspeed

    if xc > rect.right:
        pause = True
          
    # draw axes
    pyg.draw.line(screen, (50,50,50), (rect.centerx,0), (rect.centerx,rect.bottom), 2)
    pyg.draw.line(screen, (50,50,50), (0,rect.centery), (rect.right,rect.centery), 2) 

    #draw x line
    pyg.draw.line(screen, (100,100,100), (xc,rect.top), (xc,rect.bottom), 2)

    #draw current point
    pyg.draw.circle(screen, (0,255,255), (xc,yc), 5, 0)

    #draw graph up to point
    if len(points)>1:
        pyg.draw.lines(screen, (0,255,255), False, points, 2)

    xstring = "  x = " + str(round(x,2))
    xtext = font.render(xstring, True, (255,255,255))
    xtext_rect = xtext.get_rect()
    xtext_rect.left = xc
    xtext_rect.centery = 20
    screen.blit(xtext, xtext_rect)

    ystring = "  y = " + str(round(y,2))
    ytext = font.render(ystring, True, (0,255,255))
    ytext_rect = ytext.get_rect()
    ytext_rect.midleft = (xc,yc)
    screen.blit(ytext, ytext_rect)
    
    #update
    clock.tick(60)
    pyg.display.update()

pyg.quit()
        
