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

        if index == 0:
            self.set_position(mouse_pos)

        elif index == 1:
            return self
        
        return None