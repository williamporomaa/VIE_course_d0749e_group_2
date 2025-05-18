import sys
import json
from game_engine.Game_Graphics_Handler import GraphicsHandler
from game_engine.Event_Handler import EventHandler
import time
import pygame as pg
from game_engine import Audio_Handler, Board_Element, Game_Button_Element, Card_Element, Deck_Element, Decorative_Element, Dice_Element,  Game_Menu, Piece_Element

ELEMENT_TYPE_MAP = {
    "button": 0,
    "card": 1,
    "deck": 2,
    "decorative": 3,
    "dice": 4,
    "menu": 5,
    "piece": 6,
    "board": 7
}
class GameHandler():
    def __init__(self):
        self.entity_list = self.read_Entity_List()
        pg.display.init()
        main_surface = pg.display.set_mode((1000, 800))
        self.graphics_handler = GraphicsHandler(self.entity_list, main_surface)
        self.event_handler = EventHandler(self, self.entity_list)
        print(self.entity_list)
    #quit logic is a bit funky rn, working on a fix but its not prioritised
    def game_Loop(self):
        while True:
            self.graphics_handler.render_Scene()
            self.event_handler.handle_events()
            time.sleep(1/30)  # import time
            #handle events
            #uh something else?

    def read_Entity_List(self):
        try:
            # Prompt the user to enter the path to the JSON file
            file_path = input("Enter the path to the game state JSON file: ")
            with open(file_path, 'r') as file:
                game_state = json.load(file)
                
            entity_list = []
            
            # Read board data
            board_data = game_state.get("board", {})
            if board_data:
                board = Board_Element.BoardElement(
                    board_data["x"],
                    board_data["y"],
                    board_data["width"],
                    board_data["height"],
                    board_data["image_path"],
                    board_data["tiles", []],
                    element_type=ELEMENT_TYPE_MAP["board"]
                )
                entity_list.append(board)
            
            # Read items data
            items_data = game_state.get("items", [])
            for item_data in items_data:
                item_type_str = item_data["type"]
                element_type = ELEMENT_TYPE_MAP.get(item_type_str, None)
                if element_type is None:
                    print(f"Unknown element type: {item_type_str}")
                    continue
                
                if element_type == 6:  # piece
                    entity = Piece_Element.PieceElement(
                        item_data["name"],
                        item_data["x"],
                        item_data["y"],
                        item_data["width"],
                        item_data["height"],
                        item_data["image_path"],
                        item_data["moveable"],
                        item_data["allowed_movement"]
                    )
                elif element_type == 2:  # deck
                    entity = Deck_Element.DeckElement(
                        item_data["name"],
                        item_data["x"],
                        item_data["y"],
                        item_data["width"],
                        item_data["height"],
                        item_data["image_path"],
                        item_data["card_list"]
                    )
                elif element_type == 1:  # card
                    entity = Card_Element.CardElement(
                        item_data["name"],
                        item_data["x"],
                        item_data["y"],
                        item_data["width"],
                        item_data["height"],
                        item_data["face1_path"],
                        item_data["face2_path"],
                        item_data["card_value"]
                    )
                elif element_type == 4:  # dice
                    entity = Dice_Element.DiceElement(
                        item_data["name"],
                        item_data["x"],
                        item_data["y"],
                        item_data["width"],
                        item_data["height"],
                        item_data["image_path"]
                    )
                else:
                    # Skip unknown types
                    continue
                
                # Add flags to the entity
                for flag in item_data.get("flags", []):
                    entity.add_flag(flag["value"])
                
                    entity_list.append(entity)

            return entity_list
        except Exception as e:
            print(f"Error reading entity list: {e}")
            return []

GameHandler = GameHandler()
GameHandler.game_Loop()