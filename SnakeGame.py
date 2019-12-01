import pygame
import random 
import time 

# bvhghghjbu

def make_apple(screen, x, y, image):
        # c = (155, 50, 75)
        # pygame.draw.circle(screen, c, (x,y), 10)
        screen.blit(image, (x-10,y-10)) 

def Get_cord():
        x = (random.randrange(10, 630)) 
        y = (random.randrange(10, 470))
        return (x,y)

def checker_circle(points, position, counter, chord):
    points = points + [position]
    points = points[-100-(counter*10):]
    circleX = chord[0]
    circleY = chord[1]
    cordinatex = points[-1][0]
    cordinatey = points[-1][1]
    if position[0] >= circleX-10 and position[0] <= circleX+10 and position[1] >= circleY-10 and position[1] <= circleY+10:
        is_dot_reached = True
        chord = Get_cord()
        counter += 1
    return (points, counter, chord)

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    c = (155, 50, 75)
    is_dot_reached = False

    radius = 8
    x = 0
    y = 0
    mode = 'blue'
    points = [(320, 240)]
    chord = Get_cord()
    circleX = chord[0]
    circleY = chord[1]
    counter = 0
    pressed = pygame.key.get_pressed()
    point2 = []
    point3 = []
    image1 = pygame.image.load("apple.png") 
    image = pygame.transform.scale(image1, (20,20))
    direction = (3,0)
    while True:
        pressed = pygame.key.get_pressed()
        print("running", points)
         
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
         
        for event in pygame.event.get(): 
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                # determine if a letter key was pressed 
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius 
                    radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)

        screen.fill((255, 255, 0))

        if pressed[pygame.K_UP]: 
            direction = (0,-1)
        if pressed[pygame.K_DOWN]: 
            direction = (0,1)
        if pressed[pygame.K_LEFT]: 
            direction = (-1, 0)
        if pressed[pygame.K_RIGHT]: 
            direction = (1, 0)

        pos = points[-1]
        posx = pos[0]
        posy = pos[1]
        point2 = points
        color = (255,255,255)
        
        if posx >= 0 and posx <= 640 and posy >= 0 and posy <= 480:
            position = (direction[0]+posx, direction[1]+posy)
            (points, counter, chord) = checker_circle(points, position, counter, chord)
        else:
            counter = 0
            points = [(320, 240)]
            chord = Get_cord()
        if pos in point2:
            point3 = point2
            point3.pop()
            if pos in point3:
                counter = 0
                points = [(320, 240)]
                chord = Get_cord()

        circleX = chord[0]
        circleY = chord[1]
        # if is_dot_reached == False:
        make_apple(screen, circleX, circleY, image)
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
            pygame.draw.circle(screen, color, (posx-4,posy-4), 8)
            pygame.draw.circle(screen, color, (posx+4,posy+4), 8)            
            pygame.draw.circle(screen, color, (posx-4,posy+4), 8)
            pygame.draw.circle(screen, color, (posx+4,posy-4), 8)
            pygame.draw.circle(screen, (20,10,20), (posx,posy), 5)

        font = pygame.font.SysFont("comicsansms", 20)
        text = font.render(("score " + str(counter)), True, (250, 128, 255))
        screen.blit(text,(630 - text.get_width(), 15))
        pygame.display.flip()     
        clock.tick(100)
 
def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    pressed = pygame.key.get_pressed()
     
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
     
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        dd = int(aprogress * start[0] + progress * end[0])
        cc = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (dd, cc), width)

main()
