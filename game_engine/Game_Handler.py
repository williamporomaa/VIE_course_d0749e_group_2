import sys
from Game_Graphics_Handler import GraphicsHandler
import time
import pygame as pg
from Event_Handler import EventHandler

class GameHandler():
    def __init__(self):
        self.entity_list = [] #read entity list from json file somehow
        pg.display.init()
        main_surface = pg.display.set_mode((1000, 800))
        self.graphics_handler = GraphicsHandler(self.entity_list, main_surface)
        self.event_handler = EventHandler(self)
        pass

    #quit logic is a bit funky rn, working on a fix but its not prioritised
    def game_Loop(self):
        while True:
            self.graphics_handler.render_Scene()
            self.event_handler.handle_events()
            #handle events
            #uh something else?

                

GameHandler = GameHandler()
GameHandler.game_Loop()