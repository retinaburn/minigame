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

import curses

DO_COLOR = 0
HAS_COLOR = 0
HAS_IC = 0
HAS_IL = 0
LONG_NAME = 0
TERM_NAME = 0
LOG_LINES = ['','','','']
#Add x,y co-ordinates together
def add(first, second):
    x = first[0] + second[0]
    y = first[1] + second[1]
    return (x,y)


def main(screen):
    global LOG_LINES
    global DO_COLOR,HAS_COLOR,HAS_IC,HAS_IL,LONG_NAME,TERM_NAME

    screen = curses.initscr()
    curses.curs_set(0)
    h, w = screen.getmaxyx()
    player = (h/2,w/2)

    DO_COLOR = curses.can_change_color()
    HAS_COLOR = curses.has_colors()
    HAS_IC = curses.has_ic()
    HAS_IL = curses.has_il()
    LONG_NAME = curses.longname()
    TERM_NAME = curses.termname()
    print "Do Color: {}\nHas Color: {}\nHas insert/delete character capabilities: {}\nHas insert/delete line capabilities: {}\nLong Name: {}\nTerminal Name: {}".format(DO_COLOR, HAS_COLOR, HAS_IC, HAS_IL, LONG_NAME, TERM_NAME)
    print "LOG_LINES: {}".format(LOG_LINES)

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

                if event.value[1] == 1: #Up
                    next_position = (-1,0)
                elif event.value[1] == -1: #Down
                    next_position = (1,0)
                if event.value[0] == 1: #Right
                    next_position = (0,1)
                if event.value[0] == -1: #Left
                    next_position = (0,-1)
            

            screen.addstr(0,0, "Event: {}".format(event))
            screen.refresh()
            #print "Event: {}".format(event)
            
        if dpad_down:
            #clear last position
            screen.addstr(2,0, "Position: {}".format(player))
            screen.addch(player[0],player[1],' ')
            player = add(player, next_position)
            screen.addstr(3,0, "Position: {}".format(player))
            #time.sleep(3)
            #screen.addstr(2,0, "Player: {}".format(player))
            screen.addch(player[0],player[1],curses.ACS_DIAMOND)
            screen.refresh()
    #End While
    

if __name__ == '__main__':
    curses.wrapper(main)


