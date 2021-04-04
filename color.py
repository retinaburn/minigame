import pygame
from pygame.locals import *
import os
import time

os.putenv('SDL_VIDEODRIVER','fbcon')

HEIGHT = 0
WIDTH = 0
import curses

def main(screen):
    global HEIGHT, WIDTH
    curses.start_color()
    curses.use_default_colors()
    screen = curses.initscr()
    curses.curs_set(0)
    HEIGHT, WIDTH = screen.getmaxyx()
    player = (HEIGHT/2,WIDTH/2)

    #print "Screen: Height: {}, Width: {}".format(h, w)
    #win = curses.newwin(h, w, 0, 0)
    screen.clear()
    screen.refresh()

    for i in range(0, curses.COLORS):
        curses.init_pair(i+1, i, -1)
    for i in range(0,255):
        screen.addstr(str(i) + " ", curses.color_pair(i))
        if i % 7 == 0:
            screen.addch('\n')
   
    screen.getch()
    

if __name__ == '__main__':
    curses.wrapper(main)


