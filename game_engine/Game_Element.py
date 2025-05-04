import sys

class GameElement:
    def __init__(self, name, x, y, width, height, image_path=None):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image_path = image_path

    def get_position(self):
        return (self.x, self.y)

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def get_size(self):
        return (self.width, self.height)

    def set_size(self, width, height):
        self.width = width
        self.height = height

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name