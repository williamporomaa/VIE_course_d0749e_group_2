import json
from PySide6.QtCore import QSize, Qt, Signal, QRectF
from PySide6.QtGui import QAction, QIcon, QImage, QPixmap
from PySide6.QtWidgets import QComboBox, QListWidget, QWidget, QFileDialog, QMessageBox

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
                game_state = self.mainWidget.get_game_state()  # Assuming mainWidget has a method to get the game state
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
                self.mainWidget.set_game_state(game_state)  # Assuming mainWidget has a method to set the game state
                print("Game loaded successfully.")
                QMessageBox.information(self, "Load Game", "Game loaded successfully.")
                self.loadGameSignal.emit()
        except Exception as e:
            print(f"Error loading game: {e}")
            QMessageBox.critical(self, "Load Game", f"Error loading game: {e}")
        
        