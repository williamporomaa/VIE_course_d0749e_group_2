from PySide6.QtCore import QSize, Qt, Signal, QRectF
from PySide6.QtGui import QAction, QIcon, QImage, QPixmap
from PySide6.QtWidgets import QComboBox, QListWidget, QWidget

class GridButton(QComboBox):
    def __init__(self, mainWidget):
        super().__init__()
        self.mainWidget = mainWidget
        QComboBox.addItem(self, "8x8 grid")
        QComboBox.addItem(self, "7x6 grid")
        QComboBox.addItem(self, "10x10 grid")
        QComboBox.addItem(self, "Custom grid")

        self.currentIndexChanged.connect(self.generateGrid)

    def generateGrid(self, index):
        
        if(index == 0):
            rectangle = QRectF()
            #left cord, top cord, width, height
            self.mainWidget.scene.addRect(0, 0, self.mainWidget.scene_width/8, self.mainWidget.scene_height/8)
        elif(index == 1):
            print("index is 1")
        elif(index == 2):
            print("index is 2")
        elif(index == 3):
            print("index is 3")
        else:
            print("index = ",index)