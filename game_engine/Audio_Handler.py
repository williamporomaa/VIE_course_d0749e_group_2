import pygame as pg

class AudioHandler:
    def __init__(self, audio_paths=None):
        # Initialize the audio handler
        pg.mixer.init()
        self.audio_paths = audio_paths if audio_paths else []
        self.loaded_sounds = {}  # Dictionary to store loaded sounds
    
    def load_sounds(self):
        # Load all audio files from the provided paths
        for sound_path in self.audio_paths:
            try:
                self.loaded_sounds[sound_path] = pg.mixer.Sound(sound_path)
                print(f"Loaded sound: {sound_path}")
            except Exception as e:
                print(f"Error loading sound {sound_path}: {e}")
    
    def play_sound(self, sound_path, loops=0):
        # Play a sound if it is loaded
        if sound_path in self.loaded_sounds:
            self.loaded_sounds[sound_path].play(loops=loops)
            print(f"Playing sound: {sound_path}")
        else:
            print(f"Sound {sound_path} not found in loaded sounds.")
    
    def stop_sound(self, sound_path):
        # Stop a sound if it is playing
        if sound_path in self.loaded_sounds:
            self.loaded_sounds[sound_path].stop()
            print(f"Stopped sound: {sound_path}")
        else:
            print(f"Sound {sound_path} not found in loaded sounds.")
            
    def set_volume(self, sound_path, volume):
        # Set the volume for a specific sound (0.0 to 1.0)
        if sound_path in self.loaded_sounds:
            self.loaded_sounds[sound_path].set_volume(volume)
            print(f"Set volume for {sound_path} to {volume}")
        else:
            print(f"Sound {sound_path} not found in loaded sounds.")
            
    def stop_all_sounds(self):
        # Stop all currently playing sounds
        pg.mixer.stop()
        print("Stopped all sounds.")