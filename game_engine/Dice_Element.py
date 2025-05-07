from Game_Element import GameElement
import random

class DiceElement(GameElement):
    def __init__(self, name, x, y, width, height, image_path, sides=6):
        super().__init__(name, x, y, width, height, 4, image_path)
        self.sides = sides
        self.current_value = 1  # Default to the first side
        #might want to add a list of images for each side of the dice

    def roll(self):
        # Roll the dice and return a random value between 1 and the number of sides
        self.current_value = random.randint(1, self.sides)
        return self.current_value

    def get_current_value(self):
        # Return the current value of the dice
        return self.current_value