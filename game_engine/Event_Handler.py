import pygame as pg
import sys
from Popup_Menu import PopupMenu

class EventHandler:
    def __init__(self, game_handler):
        self.game_handler = game_handler
        self.selected_element = -1 # -1 means no element is selected 
        self.graphics_handler = game_handler.graphics_handler

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
                    print("mb1 pressed")
                elif event.button == 3:
                    print("mb2 pressed")
                    rect = pg.Rect(event.pos[0], event.pos[1], 1, 1)
                    index = rect.collidelist(self.game_handler.entity_rectangles)
                    if index >= 0:
                        entity = self.game_handler.entity_list[index]
                        self.entity_right_click_event(entity, event.pos)
                else:
                    continue
    
    def entity_right_click_event(self, entity, mouse_pos):
        type = entity.element_type  #0 = button, 1 = card, 2 = deck, 3 = decorative, 4 = dice, 5 = menu, 6 = piece, 7 = board
        if type == 5:
            self.selected_element = -1
        else:
            self.selected_element = entity.element_type
            menu = entity.get_menu()
            self.graphics_handler.popup = PopupMenu(menu, mouse_pos, 100, 50) 
