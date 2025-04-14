from PySide6.QtWidgets import QApplication, QWidget, QGraphicsScene, QGraphicsView

class GraphicScene(QGraphicsScene):
    gridSizeX = 0
    gridSizeY = 0
    grid_size = 0
    def __init__(self):
        super().__init__()