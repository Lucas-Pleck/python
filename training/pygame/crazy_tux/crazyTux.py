import pygame
import time
import random

from pygame.constants import GL_GREEN_SIZE

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

block_color = (53,115,255)

tux_width = 75


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Crazy TUX')
clock = pygame.time.Clock()

bg=pygame.image.load('bg.png')
tuxImg = pygame.image.load('tux.png')
windowsImage = pygame.image.load('windows.png')



def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy, thingw, thingh, color):
     gameDisplay.blit(windowsImage,[thingx, thingy, thingw, thingh])
    

def car(x,y):
    gameDisplay.blit(tuxImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',40)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
    
    

def crash():
    message_display('You have been COMMERCIALIZED')
    
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 5
    thing_width = 100
    thing_height = 100



    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                if event.key == pygame.K_RIGHT:
                    x_change = 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)
        gameDisplay.blit(bg,(0,0))

        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)


        
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)

        if x > display_width - tux_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)

        if y < thing_starty+thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x+tux_width > thing_startx and x + tux_width < thing_startx+thing_width:
                print('x crossover')
                crash()
        
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()