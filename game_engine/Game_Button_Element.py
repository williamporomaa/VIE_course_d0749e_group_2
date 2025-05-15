from game_engine.Game_Element import GameElement
import pygame as pg
import sys

class GameButtonElement(GameElement):
    def __init__(self, name, x, y, width, height, image_path, function, text, menu=None):
        super().__init__(name, x, y, width, height, 0, image_path)
        self.function = function    
        self.text = text
        self.menu = menu

    def set_action(self, function):
        self.function = function

    def click(self):
        if self.function == "start_game":
            self.start_game()
        elif self.function == "quit_game":
            self.quit_game()
        elif self.function == "change_audio":
            self.change_audio()
        elif self.function == "restart_game":
            self.restart_game()
        elif self.function == "open_menu":
            self.open_menu()

    def quit_game(self):
        # Quit the game
        pg.quit()
        sys.exit()

    def start_game(self):
        # Start the game
        pass

    def change_audio(self):
        # Change the audio settings
        pass

    def restart_game(self):
        # Restart the game
        pass

    def open_menu(self):
        if self.menu:
            # Open the menu
            pass
