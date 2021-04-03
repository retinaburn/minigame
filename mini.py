import pygame
from pygame.locals import *
import os
import time

os.putenv('SDL_VIDEODRIVER','fbcon')
pygame.init()
pygame.display.init()
pygame.joystick.init()

print "Found {} joysticks".format(pygame.joystick.get_count())
joy = pygame.joystick.Joystick(0)
joy.init()
print "Name: {}".format(joy.get_name())

MENU_BUTTON = 11
DPAD = JOYHATMOTION
HEIGHT = 0
WIDTH = 0
import curses

#Add x,y co-ordinates together
def add(first, second):
    x = first[0] + second[0]
    y = first[1] + second[1]
    return (x,y)

def fence(player):
    global HEIGHT, WIDTH
    y,x = player
    if y < 0:
        y = 0
    elif y > (HEIGHT - 2):
        y = HEIGHT - 2
    if x < 0:
        x = 0
    elif x > (WIDTH - 2):
        x = WIDTH - 2
    return (y,x)

def main(screen):
    global HEIGHT, WIDTH
    screen = curses.initscr()
    curses.curs_set(0)
    HEIGHT, WIDTH = screen.getmaxyx()
    player = (HEIGHT/2,WIDTH/2)

    #print "Screen: Height: {}, Width: {}".format(h, w)
    #win = curses.newwin(h, w, 0, 0)
    screen.clear()
    screen.addch(player[0],player[1],curses.ACS_DIAMOND)
    screen.refresh()

    running = True

    dpad_down = False
    next_position = (0,0)
    while(running):
        for event in pygame.event.get():
            if event.type == JOYBUTTONUP and event.button == MENU_BUTTON:
                curses.endwin()
                running = False
            if event.type == DPAD:
                screen.addstr(1,0, "Event Value: {}".format(event.value))
                if event.value == (0,0):
                    dpad_down = False
                else:
                    dpad_down = True

                next_position = (0,0)
                if event.value[1] == 1: #Up
                    next_position = add(next_position,(-1,0))
                elif event.value[1] == -1: #Down
                    next_position = add(next_position,(1,0))
                if event.value[0] == 1: #Right
                    next_position = add(next_position,(0,1))
                if event.value[0] == -1: #Left
                    next_position = add(next_position,(0,-1))
            

            screen.addstr(0,0, "Event: {}".format(event))
            screen.refresh()
            #print "Event: {}".format(event)
            
        if dpad_down:
            screen.addstr(2,0, "Position: {}".format(player))
            screen.addstr(3,0, "Fenced Position: {}".format(fence(player)))
            #clear last position
            screen.addch(player[0],player[1],' ')
            player = fence(add(player, next_position))
            #screen.addstr(3,0, "Position: {}".format(player))
            screen.addch(player[0],player[1],curses.ACS_DIAMOND)
            screen.refresh()
    #End While
    

if __name__ == '__main__':
    curses.wrapper(main)


