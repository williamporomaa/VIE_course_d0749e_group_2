from PySide6.QtWidgets import QApplication, QWidget, QGraphicsScene, QGraphicsView

class GraphicScene(QGraphicsScene):
    gridSizeX = 0
    gridSizeY = 0
    def __init__(self):
        super().__init__()
        self.gridSizeX = 69
        self.gridSizeY = 2