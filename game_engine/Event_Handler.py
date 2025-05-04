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

    