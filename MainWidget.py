import sys

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGraphicsScene, QGraphicsView, QHBoxLayout, \
    QSizePolicy, QGraphicsItem, QListWidget

from AssetList import AssetList
from FileSystem import FileSystemView
from ToolBar import ToolBar


class MainWidget(QWidget):
    width = 1600
    height = 1600
    scene_width = 400
    scene_height = 400

    def __init__(self, dir_path):
        super().__init__()
        
        self.setWindowTitle("My App")
        self.setGeometry(300, 300, self.width, self.height)

        # graphic view
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 400, 400)
        view = QGraphicsView(self.scene)
        view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # item view
        self.assetList = AssetList()
        self.assetList.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # file system
        self.fileSystem = FileSystemView(dir_path)
        self.fileSystem.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # toolbar   #note: Changed so that tool bar is generated last, this is so that the scene exists before grid_button is called, otherwise its initilaziation doesnt work
        self.toolbar = ToolBar(self)

        # organize the widgets
        # vertical layout (toolbar - horizontal layout [view - file system])
        layoutH = QHBoxLayout()
        layoutH.addWidget(self.assetList, stretch=1)
        layoutH.addWidget(view, stretch=3)
        layoutH.addWidget(self.fileSystem, stretch=1)

        layoutV = QVBoxLayout()
        layoutV.addWidget(self.toolbar)
        layoutV.addLayout(layoutH)
        self.setLayout(layoutV)
        
    def get_game_state(self):
        # Return the current game state as a dictionary
        return {
            "pieces": self.get_pieces_data(),
            "score": self.score,
            "level": self.level
        }
        
    def set_game_state(self, state):
        # Update the game state from the given dictionary
        self.set_pieces_data(state["pieces"])
        self.score = state["score"]
        self.level = state["level"]

    def get_pieces_data(self):
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

    def set_pieces_data(self, pieces_data):
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