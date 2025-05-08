class PopupMenu():
    def __init__(self, menu, pos, button_width, button_height):
        self.x = pos[0]
        self.y = pos[1]
        self.button_width = button_width
        self.button_height = button_height
        self.buttons = []
        for text in menu:
            self.buttons.append(text)
