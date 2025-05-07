import pygame as pg
import sys

class EventHandler:
    def __init__(self, game_handler):
        self.game_handler = game_handler
        self.selected_element = None

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
                        print(entity.element_type)
                else:
                    continue