import sys

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGraphicsView, QHBoxLayout, \
    QSizePolicy, QGraphicsItem

from Game_Elements_List import AssetList
from Tool_Bar import ToolBar
from Graphics_Scene import GraphicScene
from Game_Element_Settings import ElementView


class MainWidget(QWidget):
    width = 1600
    height = 1600
    scene_width = 400
    scene_height = 400
    actualizeSignal = Signal()

    def __init__(self, dir_path):
        super().__init__()
        
        self.setWindowTitle("My App")
        self.setGeometry(300, 300, self.width, self.height)

        # graphic view
        self.scene = GraphicScene()
        self.scene.setSceneRect(0, 0, 400, 400)
        view = QGraphicsView(self.scene)
        view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # item list
        self.assetList = AssetList(self)
        self.assetList.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # element view
        self.elementView = QVBoxLayout()
        self.elementOpened = []

        # toolbar   #note: Changed so that tool bar is generated last, this is so that the scene exists before grid_button is called, otherwise its initilaziation doesnt work
        self.toolbar = ToolBar(self, dir_path)

        # organize the widgets
        # vertical layout (toolbar - horizontal layout [item list - view - item attributes])
        self.layoutH = QHBoxLayout()
        self.layoutH.addWidget(self.assetList, stretch=1)
        self.layoutH.addWidget(view, stretch=3)
        self.layoutH.addLayout(self.elementView, stretch=1)

        layoutV = QVBoxLayout()
        layoutV.addWidget(self.toolbar)
        layoutV.addLayout(self.layoutH)
        self.setLayout(layoutV)

    def addElementView(self, item):
        if not item.name in self.elementOpened:
            view = ElementView(self, item)
            self.actualizeSignal.connect(view.actualizePosAndScale)
            self.elementView.addWidget(view)
            self.elementOpened.append(item.name)

    def acualizeElementView(self):
        self.actualizeSignal.emit()

        
    def getGameState(self):
        # Return the current game state as a dictionary
        return {
            "pieces": self.getPiecesData(),
        }
        
    def setGameState(self, state):
        # Update the game state from the given dictionary
        self.setPiecesData(state["pieces"])

    def getPiecesData(self):
        pieces_data = []
        for item in self.scene.items():
            if isinstance(item, QGraphicsItem):
                piece_data = {
                    "x": item.x(),
                    "y": item.y(),
                    "type": item.data(0)
                }
                pieces_data.append(piece_data)
        return pieces_data

    def setPiecesData(self, pieces_data):
        self.scene.clear()
        for piece_data in pieces_data:
            piece = QGraphicsItem()
            piece.setX(piece_data["x"])
            piece.setY(piece_data["y"])
            piece.setData(0, piece_data["type"])
            self.scene.addItem(piece)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dirPath = r'./testDir'
    demo = MainWidget(dirPath)
    demo.show()
    sys.exit(app.exec())