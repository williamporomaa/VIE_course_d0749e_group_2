from .Game_Element import GameElement
class PieceElement(GameElement):
    def __init__(self, name, x, y, width, height, image_path, moveable=True, allowed_movement=None):
        super().__init__(name, x, y, width, height, 6, image_path)
        self.moveable = moveable

    def get_menu(self):
        menu = ["close"]
        if(self.moveable):
            menu.append("move")
        return menu

    def do_function(self, index, mouse_pos=None):
        #temporary testing function
        print("piece function ", index)

        if index == 0:
            print("moved piece")
            self.set_position(mouse_pos)
            print("new position: ", self.x, self.y)
            print("new rectangle position: ", self.rectangle.x, self.rectangle.y)

        elif index == 1:
            print("moving piece")
            return self
        
        return None