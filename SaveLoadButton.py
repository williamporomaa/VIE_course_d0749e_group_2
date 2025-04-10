from PySide6.QtCore import QSize, Qt, Signal, QRectF
from PySide6.QtGui import QAction, QIcon, QImage, QPixmap
from PySide6.QtWidgets import QComboBox, QListWidget, QWidget

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
        # Implement the logic to save the game state
        print("Saving game...")
        self.saveGameSignal.emit()

    def loadGame(self):
        # Implement the logic to load the game state
        print("Loading game...")
        self.loadGameSignal.emit()
        