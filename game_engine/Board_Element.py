from Game_Element import GameElement

class BoardElement(GameElement):
    def __init__(self, x, y, width, height, image_path, tiles=None):
        super().__init__("board", x, y, width, height, 7, image_path)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image_path = image_path
        self.elements = []
        self.tiles = tiles

    def add_element(self, element):
        self.elements.append(element)

    def remove_element(self, element=None):
        # Remove an element from the board
        # If element is None, remove the last element in the list
        if index is not None:
            self.elements.pop(index)
        else:
            self.elements.remove(element)

    def get_elements(self):
        # Return a list of elements on the board
        return self.elements

    def clear_board(self):  
        # Clear all elements from the board
        self.elements.clear()

    def get_menu(self):
        menu = ["close"]

        return menu
