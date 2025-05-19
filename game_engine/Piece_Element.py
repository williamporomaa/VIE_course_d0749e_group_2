from .Game_Element import GameElement
class PieceElement(GameElement):
    def __init__(self, board, name, x, y, width, height, image_path, removable=True,
                 snapping=False, moveable=True,  dragable=False, stackable=False):
        super().__init__(name, x, y, width, height, 6, image_path, removable)
        self.board = board
        self.moveable = moveable
        self.dragable = dragable
        self.stackable = stackable
        self.snapping = snapping
        self.should_snap = snapping
        if self.snapping:
            self.snap((x,y))

    def get_menu(self):
        menu = ["close"]
        if(self.moveable):
            menu.append("move")
        if(self.removable):
            menu.append("remove")
        return menu

    def do_function(self, index, mouse_pos=None):
        #temporary testing function
    
        if index == -1:
            self.set_position(mouse_pos)
        elif index == 0:
            #closing menu happens in event handler
            pass
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

    def set_position(self, pos):
        if self.snapping:
            self.snap(pos)
        else:
            super().set_position(pos)

    def snap(self, pos):
        min_dist = float('inf')
        final_pos = pos
        for tile in self.board.tiles:
            dist = (pos[0] - tile[0])**2+(pos[1] - tile[1])**2
            if dist<min_dist:
                min_dist = dist
                final_pos = tile
        super().set_position(final_pos)