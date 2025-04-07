import sys

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGraphicsScene, QGraphicsView, QHBoxLayout, QSizePolicy

from FileSystem import FileSystemView
from ToolBar import ToolBar


class MainWidget(QWidget):
    def __init__(self, dir_path):
        super().__init__()
        self.setWindowTitle("My App")
        self.setGeometry(300, 300, 1600, 1600)

        # toolbar
        self.toolbar = ToolBar(self)

        # graphic view
        self.scene = QGraphicsScene()
        view = QGraphicsView(self.scene)
        view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # file system
        self.fileSystem = FileSystemView(dir_path)
        self.fileSystem.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # organize the widgets
        # vertical layout (toolbar - horizontal layout [view - file system])
        layoutH = QHBoxLayout()
        layoutH.addWidget(view, stretch=3)
        layoutH.addWidget(self.fileSystem, stretch=1)

        layoutV = QVBoxLayout()
        layoutV.addWidget(self.toolbar)
        layoutV.addLayout(layoutH)
        self.setLayout(layoutV)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dirPath = r'./testDir'
    demo = MainWidget(dirPath)
    demo.show()
    sys.exit(app.exec())