from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon, QImage, QPixmap
from PySide6.QtWidgets import QComboBox, QListWidget

class GridButton(QComboBox):
    def __init__(self, mainWidget):
        super().__init__()
        QComboBox.addItem(self, "8x8 grid")
        QComboBox.addItem(self, "7x6 grid")
        QComboBox.addItem(self, "10x10 grid")
        QComboBox.addItem(self, "Custom grid")


    @Slot(int)
    def generateGrid():
        return