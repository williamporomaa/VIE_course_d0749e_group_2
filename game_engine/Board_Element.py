from Game_Element import GameElement

class BoardElement(GameElement):
    def __init__(self, name, x, y, width, height, image_path, grid=None):
        super().__init__(name, x, y, width, height, image_path)
        self.elements = []
        self.grid = grid

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
