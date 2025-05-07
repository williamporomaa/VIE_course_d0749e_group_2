from Game_Element import GameElement
class CardElement(GameElement):
    def __init__(self, name, x, y, width, height, face1_path, face2_path=None, card_value=None):
        super().__init__(name, x, y, width, height, 1, face1_path)
        self.face1_path = face1_path
        self.face2_path = face2_path
        self.card_value = card_value

    def get_card_value(self):
        return self.card_value

    def set_card_value(self, card_value):
        self.card_value = card_value

    def flip_card(self):
        if self.image_path == self.face1_path:
            self.image_path = self.face2_path
        else:
            self.image_path = self.face1_path