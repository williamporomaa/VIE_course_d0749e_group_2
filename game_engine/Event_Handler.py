import pygame as pg
import sys
from game_engine.Popup_Menu import PopupMenu

class EventHandler:
    def __init__(self, game_handler, entity_list):
        self.game_handler = game_handler
        self.right_clicked = None # -1 means no element is selected 
        self.left_clicked = None
        self.graphics_handler = game_handler.graphics_handler
        self.entity_list = entity_list
        self.popup = None
        self.mouse_listener = None

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    pg.quit()
                    sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:

                    #assume move, this is not pretty but it works
                    if self.mouse_listener:
                        self.mouse_listener.do_function(0, event.pos)
                        self.mouse_listener = None

                    elif self.popup:
                        if self.popup.rectangle.collidepoint(event.pos):
                            #check which menu is clicked by calculating the index
                            index = (event.pos[1]-self.popup.y)//self.popup.button_height
                            #strange fix that could work, basically entity sends back itself if it needs user input
                            self.mouse_listener = self.selected_entity.do_function(index)
                            if self.mouse_listener == "remove":
                                if self.selected_entity in self.entity_list:
                                    self.entity_list.remove(self.selected_entity)
                                self.selected_entity = None
                        #close popup no matter if the button was clicked or left click was outside
                        self.popup = None
                        self.graphics_handler.popup = None
                    else:
                        for entity in reversed(self.entity_list):
                            if entity.rectangle.collidepoint(event.pos):
                                self.left_clicked = entity                     
                                break
                    
                elif event.button == 3:
                    self.mouse_listener = None
                    entity = None
                    self.right_clicked = None
                    for entity in reversed(self.entity_list):
                        if entity.rectangle.collidepoint(event.pos):
                            entity = entity                     
                            break

                    #Check if a popup exists and if so just remove it
                    if self.popup:
                        self.popup = None
                        self.graphics_handler.popup = None
                    elif entity:
                        self.entity_right_click_event(entity, event.pos)
                else:
                    continue
            elif event.type == pg.MOUSEBUTTONUP:
                self.left_clicked = None
            elif event.type == pg.MOUSEMOTION:
                if self.left_clicked:
                    if self.left_clicked.element_type == 6:
                        self.left_clicked.do_function(0, event.pos)
            
    
    def entity_right_click_event(self, entity, mouse_pos):
        type = entity.element_type  #0 = button, 1 = card, 2 = deck, 3 = decorative, 4 = dice, 5 = menu, 6 = piece, 7 = board
        if type == 5:
            pass
        else:
            self.right_clicked = entity
            menu = entity.get_menu()
            self.popup = PopupMenu(menu, mouse_pos, 100, 50) 
            self.graphics_handler.popup = self.popup
            
