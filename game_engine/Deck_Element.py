from game_engine.Game_Element import GameElement
import random

class DeckElement(GameElement):
    def __init__(self, name, x, y, width, height, image_path, card_list=None):
        super().__init__(name, x, y, width, height, 2, image_path)
        self.card_list = card_list

    def add_card(self, card):
        # Add a card to the top of the deck
        self.deck.append(card)

    def draw_card(self):
        # Draw a card from the top of the deck
        # If the deck is empty, return None
        if len(self.deck) == 0:
            print("Deck is empty!")
            return None
        else:
            return self.deck.pop()
        
    def shuffle_deck(self):
        # Shuffle the deck of cards
        random.shuffle(self.deck)
        