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
rscale = 60
around = False

def r(t):
    return rscale * (2*math.sin(2*t))

t = 0.0
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
    x = int(r(t) * math.cos(t))
    y = int(r(t) * math.sin(t))
    xc = x + rect.centerx
    yc = -y + rect.centery

    if (len(points) == 0 or points[-1] != (xc, yc)) and not around:
        points.append( (xc, yc) )
    t += .01
    if t > 2*math.pi:
        t=t-2*math.pi
        around = True
          
    # draw axes
    pyg.draw.line(screen, (50,50,50), (rect.centerx,0), (rect.centerx,rect.bottom), 2)
    pyg.draw.line(screen, (50,50,50), (0,rect.centery), (rect.right,rect.centery), 2) 

    xe = rect.width*math.cos(t)
    ye = rect.width*math.sin(t)

    #draw theta line
    pyg.draw.line(screen, (100,100,100), rect.center, (rect.centerx+xe, rect.centery-ye), 1)
    pyg.draw.line(screen, (100,100,100), rect.center, (rect.centerx-xe, rect.centery+ye), 1)

    #draw arrow
    xa = rect.centerx + rect.height/3*math.cos(t)
    ya = rect.centery - rect.height/3*math.sin(t)
    t1 = t + 5*math.pi/6
    t2 = t + 7*math.pi/6
    xa1 = xa + 15*math.cos(t1)
    ya1 = ya - 15*math.sin(t1)
    xa2 = xa + 15*math.cos(t2)
    ya2 = ya - 15*math.sin(t2)
    
    pyg.draw.line(screen, (100,100,100), (xa,ya), (xa1,ya1), 2)
    pyg.draw.line(screen, (100,100,100), (xa,ya), (xa2,ya2), 2)

    #draw r line
    pyg.draw.line(screen, (255,255,255), rect.center, (xc,yc), 2)

    #draw current point
    pyg.draw.circle(screen, (0,255,255), (xc,yc), 5, 0)

    #draw graph up to point
    if len(points)>1:
        pyg.draw.lines(screen, (0,255,255), False, points, 2)

    tstring = "  Theta = " + str(round(t,2))
    ttext = font.render(tstring, True, (255,255,255))
    ttext_rect = ttext.get_rect()
    ttext_rect.left = xa
    ttext_rect.centery = ya
    screen.blit(ttext, ttext_rect)

    rstring = "  radius = " + str(round(r(t)/rscale,2))
    rtext = font.render(rstring, True, (0,255,255))
    rtext_rect = rtext.get_rect()
    rtext_rect.midleft = (xc,yc)
    screen.blit(rtext, rtext_rect)
    
    #update
    clock.tick(60)
    pyg.display.update()

pyg.quit()
        
