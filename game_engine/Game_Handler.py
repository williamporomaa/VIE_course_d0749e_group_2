import sys
from Game_Graphics_Handler import GraphicsHandler
from Event_Handler import EventHandler
import time
import pygame as pg
import Audio_Handler, Board_Element, Game_Button_Element, Card_Element, Deck_Element, Decorative_Element, Dice_Element,  Game_Menu, Piece_Element

class GameHandler():
    def __init__(self):
        #set self.entity_list and self.entity_rectangles
        self.entity_list = []
        self.entity_rectangles = []
        self.read_Entity_List()
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
            time.sleep(1/30)  # import time
            #handle events
            #uh something else?

    def read_Entity_List(self):
        #test entity
        entity = Board_Element.BoardElement(100, 100, 800, 600, "chess.png")
        self.entity_list.append(entity)
        
        for entity in reversed(self.entity_list):
            self.entity_rectangles.append(pg.Rect(entity.x, entity.y, entity.width, entity.height))
                

GameHandler = GameHandler()
GameHandler.game_Loop()