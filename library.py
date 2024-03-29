# file : library.py
# contains classes, functions, and miscellaneous helper code

# included libraries
import pygame, sys
from button import *

# global definitions (multi-file)
globals = {
    'scene' : 'menu',
    'simulation' : '???',
    'width' : 1280,
    'height' : 720
}

# set screen size
SCREEN = pygame.display.set_mode((globals['width'], globals['height']))

######################### generic helper functions #########################
def get_font(size, name="lemon_days"): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/" + name + ".ttf", size)

def addLine(x1, y1, x2, y2, sw, col):
    line = pygame.draw.line(SCREEN, col, (x1, y1), (x2, y2), width=sw)

def addRect(x, y, w, h, c):
    scratch_pad = pygame.Surface((w, h))
    scratch_pad_rect = scratch_pad.get_rect(center=(x, y))
    scratch_pad.fill(c)
    SCREEN.blit(scratch_pad, scratch_pad_rect)

def map(n, start1, stop1, start2, stop2):
    return ((n - start1) / (stop1 - start1))*(stop2 - start2) + start2

######################### timed intervals (switching scenes) #########################
class Interval():
    def __init__(self, **config):
        # button graphic
        self.callback = config['callback']
        self.duration = config['duration']
        self.cover = pygame.Surface((globals['width'], globals['height']))
        self.alpha = 0
        self.direction = "forward"
        self.done = False
        
        # extra arguments (for callback function)
        self.simulation = config['simulation']
        
    def update(self, screen):
        if self.direction == "forward":
            self.alpha += (255 - self.alpha) / (self.duration / 2)

            if (255 - self.alpha < 0.01):
                self.direction = "backward"
                self.callback()
                globals['simulation'] = self.simulation
        elif self.direction == "backward":
            self.alpha += (0 - self.alpha) / (self.duration / 2)

            if (self.alpha < 0.01):
                self.done = True
        
        self.cover.set_alpha(self.alpha)
        self.cover.fill((0, 0, 0))
        screen.blit(self.cover, (0, 0))


######################### adding timed intervals #########################
intervals = []

def addInterval(args):
    argList = [None] * 3
    for i in range(0, len(args)):
        argList[i] = args[i]


    intervals.append(Interval(
        callback = argList[0],
        duration = argList[1],
        simulation = argList[2]
    ))    