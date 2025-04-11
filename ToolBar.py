from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon, QImage, QPixmap
from PySide6.QtWidgets import QToolBar, QGraphicsPixmapItem, QComboBox, QListWidget
from grid_button import GridButton
from SaveLoadButton import SaveLoadButton

class ToolBar(QToolBar):
    def __init__(self, mainWidget):
        super().__init__()
        self.setIconSize(QSize(16, 16))
        self.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.mainWidget = mainWidget

        button_add = QAction(QIcon("toolbarIcons/plus-button.png"), "Add", self)
        button_add.triggered.connect(self.button_add_clicked)
        self.addAction(button_add)

        grid_button_add = GridButton(mainWidget)
        self.addWidget(grid_button_add)
        
        save_load_button = SaveLoadButton(mainWidget)
        save_load_button.saveGameSignal.connect(self.save_game)
        save_load_button.loadGameSignal.connect(self.load_game)
        self.addWidget(save_load_button)

    """
    def save_game(self):
        # Implement the logic to save the game
        print("Game saved!")

    def load_game(self):
        # Implement the logic to load the game
        print("Game loaded!")
    """

    def button_add_clicked(self):
        image = QImage(self.mainWidget.fileSystem.get_selected_path())
        pic = QGraphicsPixmapItem()
        pic.setPixmap(QPixmap.fromImage(image))
        self.mainWidget.scene.addItem(pic)