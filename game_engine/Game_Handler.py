import sys
from Game_Graphics_Handler import GraphicsHandler
import time

class GameHandler():
    def __init__(self):
        self.entity_list = [] #read entity list from json file somehow
        self.graphics_handler = GraphicsHandler(self.entity_list)
        self.quit = False
        pass

    def game_Loop(self):
        self.graphics_handler.render_Scene()
        #handle events
        #uh something else?
        if self.quit == True:
            sys.exit()
        else:
            time.sleep(0.05) #render the game 20 times per second (20 fps)
            self.game_Loop()
        pass
