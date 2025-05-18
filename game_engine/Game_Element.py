import sys
import pygame as pg

class GameElement:
    def __init__(self, name, x, y, width, height, element_type, image_path=None, removable=False):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.element_type = element_type 
        self.keep_alive = True
        self.removable = removable
#0 = button, 1 = card, 2 = deck, 3 = decorative, 
# 4 = dice, 5 = menu, 6 = piece, 7 = board
# 8 = tile
#felt like doing string matching would take to long
        self.image_path = image_path
        self.rectangle = pg.Rect(x, y, width, height)

    def get_position(self):
        return (self.x, self.y)

    def set_position(self, pos):
        #todo: place the object so that its center ends up at the mouse position
        self.x = pos[0]-self.width//2
        self.y = pos[1]-self.height//2
        self.rectangle = pg.Rect(self.x, self.y, self.width, self.height)

    def get_size(self):
        return (self.width, self.height)

    def set_size(self, width, height):
        self.width = width
        self.height = height

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name