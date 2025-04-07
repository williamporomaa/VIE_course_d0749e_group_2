from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon, QImage, QPixmap
from PySide6.QtWidgets import QToolBar, QGraphicsPixmapItem


class ToolBar(QToolBar):
    def __init__(self, mainWidget):
        super().__init__()
        self.setIconSize(QSize(16, 16))
        self.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.mainWidget = mainWidget

        button_add = QAction(QIcon("toolbarIcons/plus-button.png"), "Add", self)
        button_add.triggered.connect(self.button_add_clicked)
        self.addAction(button_add)

    def button_add_clicked(self):
        image = QImage(self.mainWidget.fileSystem.get_selected_path())
        pic = QGraphicsPixmapItem()
        pic.setPixmap(QPixmap.fromImage(image))
        self.mainWidget.scene.setSceneRect(0, 0, 400, 400)
        self.mainWidget.scene.addItem(pic)