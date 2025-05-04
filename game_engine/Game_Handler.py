import sys
from Game_Graphics_Handler import GraphicsHandler
from Event_Handler import EventHandler
import time
import pygame as pg
import Audio_Handler, Board_Element, Button_Element, Card_Element, Deck_Element, Decorative_Element, Dice_Element,  Game_Menu, Piece_Element

class GameHandler():
    def __init__(self):
        self.entity_list =  self.read_Entity_List()
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

    def read_Entity_List(self):
        entity_list = []
        #test entity
        entity = Board_Element.BoardElement("board", 100, 100, 800, 600, "chess.png")
        entity_list.append(entity)
        
        return entity_list
                

GameHandler = GameHandler()
GameHandler.game_Loop()