from Game_Element import GameElement
import pygame as pg
import sys

class ButtonElement(GameElement):
    def __init__(self, name, x, y, width, height, image_path, function, text, menu=None):
        super().__init__(name, x, y, width, height, image_path)
        self.function = function
        self.text = text
        self.menu = menu

    def set_action(self, function):
        self.button_function = function

    def click(self):
        if self.action:
            self.action()

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