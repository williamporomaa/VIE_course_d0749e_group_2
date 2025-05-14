from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QToolBar

from File_System_View import FileSystemView
from Grid_Manager import GridButton
from Save_Load_Manager import SaveLoadButton
from game_engine.Game_Handler import GameHandler


class ToolBar(QToolBar):
    def __init__(self, mainWidget, dir_path):
        super().__init__()
        self.setIconSize(QSize(16, 16))
        self.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.mainWidget = mainWidget

        self.fileSystem = FileSystemView(dir_path, mainWidget)

        button_add = QAction(QIcon("./toolbarIcons/plus-button.png"), "Add", self)
        button_add.triggered.connect(self.buttonAddClicked)
        self.addAction(button_add)

        self.grid_button_add = GridButton(mainWidget)
        self.addWidget(self.grid_button_add)
        
        save_load_button = SaveLoadButton(mainWidget)
        self.addWidget(save_load_button)

        button_play = QAction(QIcon("./toolbarIcons/disc.png"), "play", self)
        button_play.triggered.connect(self.buttonPlayClicked)
        self.addAction(button_play)

    def buttonAddClicked(self):
        self.fileSystem.show()

    def buttonPlayClicked(self):
        gameHandler = GameHandler()
        gameHandler.game_Loop()

