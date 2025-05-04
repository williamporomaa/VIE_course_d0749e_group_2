from Game_Element import GameElement

class GameMenu(GameElement):
    def __init__(self, name, x, y, width, height, text, image_path = None,  buttons=None):
        super().__init__(name, x, y, width, height, image_path)
        self.buttons = buttons if buttons is not None else []
        self.text = text

    def add_button(self, button):
        self.buttons.append(button)