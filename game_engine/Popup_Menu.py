import pygame as pg

class PopupMenu():
    def __init__(self, menu, pos, button_width, button_height):
        self.x = pos[0]
        self.y = pos[1]
        self.button_width = button_width
        self.button_height = button_height
        self.buttons = []
        #self.popup_rectangle = pg.Rect(popup.x, popup.y, popup.button_width, popup.button_height*len(menu))
        for text in menu:
            self.buttons.append(text)
        
        self.rectangle = pg.Rect(self.x, self.y, self.button_width, self.button_height*len(self.buttons))