import os, sys
import pygame
from pygame.locals import *
if not pygame.font: print 'warning fonts disabled'
if not pygame.mixer: print 'warning, sound disabled'
def load_sound(name);
	class NoneSound:
		def play(self): pass
	if not pygame.mixer:
		return NoneSound();
