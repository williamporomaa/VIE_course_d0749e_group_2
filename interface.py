import sys

from PySide6.QtGui import QIcon, QImage, QPixmap, QAction
from PySide6.QtWidgets import QApplication, QWidget, QTreeView, QFileSystemModel, QVBoxLayout, QToolBar, \
    QMainWindow, QGraphicsScene, QGraphicsView, QHBoxLayout, QSizePolicy, QGraphicsPixmapItem
from PySide6.QtCore import QSize, Qt


class MainWindow(QMainWindow):
    def __init__(self, dir_path):
        super().__init__()
        self.setWindowTitle("My App")
        self.setGeometry(300, 300, 1600, 1600)

        # toolbar
        self.toolbar = QToolBar("My main toolbar")
        self.toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(self.toolbar)

        button_add = QAction(QIcon("plus-button.png"), "Add", self)
        button_add.triggered.connect(self.button_add_clicked)
        self.toolbar.addAction(button_add)

        self.setToolButtonStyle(Qt.ToolButtonIconOnly)


        # graphic view
        self.scene = QGraphicsScene()
        view = QGraphicsView(self.scene)
        view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # file system
        self.fileSystem = FileSystemView(dir_path)
        self.fileSystem.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # layout containing the widgets
        layout = QHBoxLayout()
        layout.addWidget(view, stretch=3)
        layout.addWidget(self.fileSystem, stretch=1)
        mainWidget = QWidget()
        mainWidget.setLayout(layout)
        self.setCentralWidget(mainWidget)


    def button_add_clicked(self):
        image = QImage(self.fileSystem.get_selected_path())
        pic = QGraphicsPixmapItem()
        pic.setPixmap(QPixmap.fromImage(image))
        self.scene.setSceneRect(0, 0, 400, 400)
        self.scene.addItem(pic)

class FileSystemView(QWidget):
    def __init__(self, dir_path):
        super().__init__()

        # file view
        model = QFileSystemModel()
        model.setRootPath(dir_path)
        self.tree = QTreeView()
        self.tree.setModel(model)
        self.tree.setRootIndex(model.index(dirPath))
        self.tree.setColumnWidth(0, 250)
        self.tree.setAlternatingRowColors(True)

        layout = QVBoxLayout()
        layout.addWidget(self.tree)
        self.setLayout(layout)

    def get_selected_path(self):
        index = self.tree.currentIndex()
        info = self.tree.model().fileInfo(index)
        return info.absoluteFilePath()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    dirPath = r'./testDir'
    demo = MainWindow(dirPath)
    demo.show()
    sys.exit(app.exec())