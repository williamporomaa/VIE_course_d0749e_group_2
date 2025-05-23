import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGraphicsView, QHBoxLayout, \
    QSizePolicy, QGraphicsItem

from tool_ui import Game_Elements_List, Tool_Bar, Graphics_Scene, Game_Element_Settings



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
        self.scene = Graphics_Scene.GraphicScene()
        self.scene.setSceneRect(0, 0, 400, 400)
        view = QGraphicsView(self.scene)
        view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # item list
        self.assetList = Game_Elements_List.AssetList(self)
        self.assetList.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # element view
        self.elementView = QVBoxLayout()
        self.elementOpened = []

        # toolbar   #note: Changed so that tool bar is generated last, this is so that the scene exists before grid_button is called, otherwise its initilaziation doesnt work
        self.toolbar = Tool_Bar.ToolBar(self, dir_path)

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
            view = Game_Element_Settings.ElementView(self, item)
            self.actualizeSignal.connect(view.actualizePosAndScale)
            self.elementView.addWidget(view)
            self.elementOpened.append(item.name)

    def acualizeElementView(self):
        self.actualizeSignal.emit()

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dirPath = r'.'
    demo = MainWidget(dirPath)
    demo.show()
    sys.exit(app.exec())