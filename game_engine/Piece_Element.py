from .Game_Element import GameElement
class PieceElement(GameElement):
    def __init__(self, name, x, y, width, height, image_path, 
                 moveable=True, allowed_movement=None, removable=True):
        super().__init__(name, x, y, width, height, 6, image_path, removable)
        self.moveable = moveable

    def get_menu(self):
        menu = ["close"]
        if(self.moveable):
            menu.append("move")
        menu.append("remove")
        return menu

    def do_function(self, index, mouse_pos=None):
        #temporary testing function
    
        if index == 0:
            self.set_position(mouse_pos)

        elif index == 1:
            if self.moveable:
                return self
            else:
                pass
        
        if index == 2:
            if self.removable:
                self.keep_alive = False
            else:
                pass
        
        return None