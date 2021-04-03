import pygame
from pygame.locals import *
import os
import locale

locale.setlocale(locale.LC_ALL, '')
code = locale.getpreferredencoding()

MENU_BUTTON = 11
D_PAD = 9

os.putenv('SDL_VIDEODRIVER','fbcon')
pygame.init()
pygame.display.init()
pygame.joystick.init()

print "Found {} joysticks".format(pygame.joystick.get_count())
joy = pygame.joystick.Joystick(0)
joy.init()
print "Name: {}".format(joy.get_name())



import curses

DO_COLOR = 0
HAS_COLOR = 0
HAS_IC = 0
HAS_IL = 0
LONG_NAME = 0
TERM_NAME = 0

def main(screen):
    global DO_COLOR,HAS_COLOR,HAS_IC,HAS_IL,LONG_NAME,TERM_NAME

    screen = curses.initscr()
    h, w = screen.getmaxyx()
    player = [h/2,w/2]

    DO_COLOR = curses.can_change_color()
    HAS_COLOR = curses.has_colors()
    HAS_IC = curses.has_ic()
    HAS_IL = curses.has_il()
    LONG_NAME = curses.longname()
    TERM_NAME = curses.termname()

    #print "Screen: Height: {}, Width: {}".format(h, w)
    #win = curses.newwin(h, w, 0, 0)
    screen.clear()
    screen.addch(player[0],player[1],curses.ACS_DIAMOND)
    screen.refresh()

    running = True
    while(running):
        for event in pygame.event.get():
            if event.type == JOYBUTTONUP and event.button == MENU_BUTTON:
                curses.endwin()
                running = False
            if event.type == JOYHATMOTION:
                screen.addstr(1,0, "Event Value: {}".format(event.value))
                if event.value[1] == 1:
                    screen.addch(player[0],player[1],' ')
                    player[0] = player[0]-1
                    screen.addch(player[0],player[1],curses.ACS_DIAMOND)
                elif event.value[1] == -1:
                    screen.addch(player[0],player[1],' ')
                    player[0] = player[0]+1
                    screen.addch(player[0],player[1],curses.ACS_DIAMOND)
                if event.value[0] == 1:
                    screen.addch(player[0],player[1],' ')
                    player[1] = player[1]+1
                    screen.addch(player[0],player[1],curses.ACS_DIAMOND)
                if event.value[0] == -1:
                    screen.addch(player[0],player[1],' ')
                    player[1] = player[1]-1
                    screen.addch(player[0],player[1],curses.ACS_DIAMOND)

            screen.addstr(0,0, "Event: {}".format(event))
            screen.refresh()
            #print "Event: {}".format(event)

if __name__ == '__main__':
    curses.wrapper(main)

print "Preferred Encoding {}".format(code)
print "Do Color: {}\nHas Color: {}\nHas insert/delete character capabilities: {}\nHas insert/delete line capabilities: {}\nLong Name: {}\nTerminal Name: {}".format(DO_COLOR, HAS_COLOR, HAS_IC, HAS_IL, LONG_NAME, TERM_NAME)

