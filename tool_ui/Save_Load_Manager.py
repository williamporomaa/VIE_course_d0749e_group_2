import json
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QComboBox, QFileDialog, QMessageBox, QGraphicsItem

from tool_ui.Enums import ElementTypes
from tool_ui.Graphic_Item import GraphicItem


class SaveLoadButton(QComboBox):
    saveGameSignal = Signal()
    loadGameSignal = Signal()

    def __init__(self, mainWidget):
        super().__init__()
        self.mainWidget = mainWidget
        QComboBox.addItem(self, "Save/load")
        QComboBox.addItem(self, "Save Game")
        QComboBox.addItem(self, "Load Game")

        self.currentIndexChanged.connect(self.handleAction)

    def handleAction(self, index):
        if index == 1:  # Save Game
            self.saveGame()
        elif index == 2:  # Load Game
            self.loadGame()

    def saveGame(self):
        try:
            file_path, _ = QFileDialog.getSaveFileName(self, "Save Game", "", "JSON Files (*.json)")
            if file_path:
                game_state = self.getGameState()  # Assuming mainWidget has a method to get the game state
                with open(file_path, 'w') as file:
                    json.dump(game_state, file, indent=4)
                print("Game saved successfully.")
                QMessageBox.information(self, "Save Game", "Game saved successfully.")
                self.saveGameSignal.emit()
        except Exception as e:
            print(f"Error saving game: {e}")
            QMessageBox.critical(self, "Save Game", f"Error saving game: {e}")
        

    def loadGame(self):
        try:
            file_path, _ = QFileDialog.getOpenFileName(self, "Load Game", "", "JSON Files (*.json)")
            if file_path:
                with open(file_path, 'r') as file:
                    game_state = json.load(file)
                self.setGameState(game_state)  # Assuming mainWidget has a method to set the game state
                print("Game loaded successfully.")
                QMessageBox.information(self, "Load Game", "Game loaded successfully.")
                self.loadGameSignal.emit()
        except Exception as e:
            print(f"Error loading game: {e}")
            QMessageBox.critical(self, "Load Game", f"Error loading game: {e}")

    def getGameState(self):
        # Return the current game state as a dictionary
        return {
            "items": self.getItemsData(),
            "board": self.getBoardData()
        }

    def setGameState(self, state):
        # Update the game state from the given dictionary
        self.mainWidget.scene.clear()
        self.mainWidget.assetList.clear()
        self.setItemsData(state["items"])
        self.setBoardData(state["board"])

    def getItemsData(self):
        items_data = []
        for name,item in self.mainWidget.assetList.items.items():
            if item.elementType.value not in [ElementTypes.Board.value, ElementTypes.Tile.value]:
                item_data = {
                    "name": name,
                    "type": item.elementType.value,
                    "x": item.getX(),
                    "y": item.getY(),
                    "height": item.getHeight(),
                    "width": item.getWidth(),
                    "image_path": item.imagePath,
                    "flags": item.getFlagsValues()
                }
                items_data.append(item_data)
        return items_data

    def setItemsData(self, items_data):
        for item_data in items_data:
            item = GraphicItem(item_data["image_path"], self.mainWidget, item_data["name"])
            item.elementType = ElementTypes(item_data["type"])
            item.move(item_data["x"], item_data["y"])
            item.changeScale(item_data["height"]/item.getHeight())
            for flagValue in item_data["flags"]:
                flag = ElementTypes.flags(item.elementType)(flagValue)
                item.gameFlags.append(flag)

    def getBoardData(self):
        for _, item in self.mainWidget.assetList.items.items():
            if item.elementType.value in [ElementTypes.Board.value]:
                board_data = {
                    "x": item.getX(),
                    "y": item.getY(),
                    "height": item.getHeight(),
                    "width": item.getWidth(),
                    "image_path": item.imagePath,
                    "tiles": self.getTilesData()
                }
                return board_data

    def getTilesData(self):
        tiles_data = []
        for tile in self.mainWidget.toolbar.grid_button_add.currentGrid:
            rect = tile.boundingRect()
            center = rect.center()
            tile_data = {
                "x": center.x(),
                "y": center.y(),
                "height": rect.height(),
                "width": rect.width()
            }
            tiles_data.append(tile_data)
        return tiles_data

    def setBoardData(self, board_data):
        board = GraphicItem(board_data["image_path"], self.mainWidget, "board")
        board.elementType = ElementTypes.Board
        board.move(board_data["x"], board_data["y"])
        board.changeScale(board_data["height"] / board.getHeight())
        self.mainWidget.toolbar.grid_button_add.generateFromTiles(board_data["tiles"])

