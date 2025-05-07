from Game_Element import GameElement

class DecorativeElement(GameElement):
    def __init__(self, name, x, y, width, height, image_path):
        super().__init__(name, x, y, width, height, 3,image_path)
