from .Game_Element import GameElement
class PieceElement(GameElement):
    def __init__(self, name, x, y, width, height, image_path, moveable=True, allowed_movement=None):
        super().__init__(name, x, y, width, height, 6, image_path)
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
            return self
        
        destroy_index = 2 if self.moveable else 1
        if index == destroy_index:
            print(f"Destroying piece: {self.name}")
            # Remove self from the entity list
            # This assumes the EventHandler sets selected_entity and has access to entity_list
            # So we can do:
            #   self in self.game_handler.entity_list
            # But since we don't have direct access, return a flag or self and let EventHandler handle removal
            return "destroy"
        
        return None