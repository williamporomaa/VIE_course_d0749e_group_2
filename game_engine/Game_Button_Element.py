from game_engine.Game_Element import GameElement
from game_engine.Audio_Handler import AudioHandler
from game_engine.Game_Handler import GameHandler
from game_engine.Game_Menu import GameMenu
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
        # Initialize the AudioHandler
        audio_handler = AudioHandler(audio_paths=["sound1.wav", "sound2.wav", "sound3.wav"])
        audio_handler.load_sounds()
        
        # Example: Play a sound
        print("Playing sound1.wav...")
        audio_handler.play_sound("sound1.wav")
        
        # Example: Adjust volume
        print("Setting volume for sound1.wav to 50%...")
        audio_handler.set_volume("sound1.wav", 0.5)
        
        # Example: Stop the sound
        print("Stopping sound1.wav...")
        audio_handler.stop_sound("sound1.wav")
        
        # Example: Stop all sounds
        print("Stopping all sounds...")
        audio_handler.stop_all_sounds()

    def restart_game(self):
        # Restart the game
        pass

    def open_menu(self):
        if self.menu:
            # Open the menu
            pass
