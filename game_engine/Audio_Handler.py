import pygame as pg

class AudioHandler:
    def __init__(self, audio_paths=None):
        self.audio_paths = audio_paths if audio_paths else []
    
    def play_sound(self, sound_path):
        if sound_path in self.audio_paths:
            print(f"Playing sound: {sound_path}")
            #sound stuff here implemented with pygame
        else:
            print(f"Sound {sound_path} not found in audio paths.")