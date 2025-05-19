import sys
import json
from game_engine.Game_Graphics_Handler import GraphicsHandler
from game_engine.Event_Handler import EventHandler
import time
import pygame as pg
from game_engine import Audio_Handler, Board_Element, Game_Button_Element, Card_Element, Deck_Element, Decorative_Element, Dice_Element,  Game_Menu, Piece_Element
import os

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
            file_path = (r"./chessGame/chess.json")
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
                    board_data["tiles"],
                )
                entity_list.append(board)
            
            # Read items data
            items_data = game_state.get("items", [])
            for item_data in items_data:
                item_type = item_data.get("type")
                if item_type == 6:  # piece
                    flag_data = item_data["flags"]
                    entity = Piece_Element.PieceElement(
                        item_data["name"],
                        item_data["x"],
                        item_data["y"],
                        item_data["width"],
                        item_data["height"],
                        item_data["image_path"],
                        #flags:
                        flag_data["IsRemovable"],
                        flag_data["IsSnapping"],
                        flag_data["IsMoveable"],
                        flag_data["IsDraggable"]
                        flag_data["IsStackable"]
                    )
                elif item_type == 2:  # deck
                    flag_data = item_data["flags"]
                    entity = Deck_Element.DeckElement(
                        item_data["name"],
                        item_data["x"],
                        item_data["y"],
                        item_data["width"],
                        item_data["height"],
                        item_data["image_path"],
                        item_data["card_list"]
                    )
                elif item_type == 1:  # card
                    flag_data = item_data["flags"]
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
                elif item_type == 4:  # dice
                    flag_data = item_data["flags"]
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
                # for flag in item_data.get("flags", []):
                #      entity.add_flag(flag["value"])
                entity_list.append(entity)
                    

            return entity_list
        except Exception as e:
            print(f"Error reading entity list: {e}")
            return []

GameHandler = GameHandler()
GameHandler.game_Loop()