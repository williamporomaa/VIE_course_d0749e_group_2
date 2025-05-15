import sys
from game_engine.Game_Graphics_Handler import GraphicsHandler
from game_engine.Event_Handler import EventHandler
import time
import pygame as pg
from game_engine import Audio_Handler, Board_Element, Game_Button_Element, Card_Element, Deck_Element, Decorative_Element, Dice_Element,  Game_Menu, Piece_Element

class GameHandler():
    def __init__(self):
        #set self.entity_list and self.entity_rectangles
        self.entity_list = []
        pg.display.init()
        main_surface = pg.display.set_mode((1000, 800))
        self.graphics_handler = GraphicsHandler(self.entity_list, main_surface)
        entity_rectangles = self.read_Entity_List()
        self.event_handler = EventHandler(self, entity_rectangles)
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
        
        #weird way to do it but i need it to work asap
        #Basically it returns a reversed representation of the entity list as pygame rectangles which is used for collision detection
        entity_rectangles = []
        for entity in reversed(self.entity_list):
            entity_rectangles.append(pg.Rect(entity.x, entity.y, entity.width, entity.height))
        return entity_rectangles    

#GameHandler = GameHandler()
#GameHandler.game_Loop()