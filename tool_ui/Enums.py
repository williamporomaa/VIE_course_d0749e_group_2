from enum import Enum


class ElementTypes(Enum):
    Piece = 0
    Card = 1
    Deck = 2
    Dice = 3
    Tile = 4
    Menu = 5
    Button = 6

    @staticmethod
    def flags(type):
        typesFlags = [PieceFlags, CardFlags, DeckFlags, DiceFlags, TileFlags, MenuFlags, ButtonFlags]
        return typesFlags[type.value]

class PieceFlags(Enum):
    IsSnapping = 0
    IsDraggable = 1
    IsDestroyable = 2
    IsStackable = 3

class CardFlags(Enum):
    pass

class DeckFlags(Enum):
    pass

class DiceFlags(Enum):
    pass

class TileFlags(Enum):
    pass

class MenuFlags(Enum):
    pass

class ButtonFlags(Enum):
    pass