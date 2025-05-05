import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon, QImage
from PySide6.QtWidgets import QToolBar, QApplication

from File_System_View import FileSystemView
from Graphic_Item import GraphicItem
from Grid_Manager import GridButton
from Save_Load_Manager import SaveLoadButton

class ToolBar(QToolBar):
    def __init__(self, mainWidget, dir_path):
        super().__init__()
        self.setIconSize(QSize(16, 16))
        self.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.mainWidget = mainWidget

        self.fileSystem = FileSystemView(dir_path, mainWidget)

        button_add = QAction(QIcon("../toolbarIcons/plus-button.png"), "Add", self)
        button_add.triggered.connect(self.buttonAddClicked)
        self.addAction(button_add)

        grid_button_add = GridButton(mainWidget)
        self.addWidget(grid_button_add)
        
        save_load_button = SaveLoadButton(mainWidget)
        save_load_button.saveGameSignal.connect(self.save_game)
        save_load_button.loadGameSignal.connect(self.load_game)
        self.addWidget(save_load_button)


    def save_game(self):
        # May need additional logic before saving, who knows
        print("Preparing to save the game...")
        self.mainWidget.saveLoadManager.saveGame()

    def load_game(self):
        # May need additional logic before loading, who knows
        print("Preparing to load the game...")
        self.mainWidget.saveLoadManager.loadGame()

    def buttonAddClicked(self):
        self.fileSystem.show()

