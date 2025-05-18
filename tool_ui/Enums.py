from enum import Enum


class ElementTypes(Enum):
    Button = 0
    Card = 1
    Deck = 2
    Decorative = 3
    Dice = 4
    Menu = 5
    Piece = 6
    Board = 7
    Tile = 8

    @staticmethod
    def flags(type):
        typesFlags = [PieceFlags, CardFlags, DeckFlags, DiceFlags, TileFlags, MenuFlags, ButtonFlags, BoardFlags]
        return typesFlags[type.value]

class PieceFlags(Enum):
    IsSnapping = 0
    IsDraggable = 1
    IsDestroyable = 2
    IsStackable = 3

class CardFlags(Enum):
    IsFlippable = 0

class DeckFlags(Enum):
    CanAddCards = 0
    CanRemoveCards = 1
    CanShuffle = 2

# not defined flags but enums created for expandability
class DiceFlags(Enum):
    pass

class TileFlags(Enum):
    pass

class MenuFlags(Enum):
    pass

class ButtonFlags(Enum):
    pass

class BoardFlags(Enum):
    pass