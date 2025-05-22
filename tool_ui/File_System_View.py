import os.path

from PySide6.QtGui import QAction, QIcon, QImage
from PySide6.QtWidgets import QWidget, QFileSystemModel, QTreeView, QVBoxLayout, QToolBar

from tool_ui.Graphic_Item import GraphicItem


class FileSystemView(QWidget):
    def __init__(self, dir_path, main_widget):
        super().__init__()
        
        self.setWindowTitle("Adding an object")
        self.mainWidget = main_widget

        # toolbar
        self.toolbar = QToolBar()
        button_add = QAction(QIcon("./toolbarIcons/plus-button.png"), "Add", self)
        button_add.triggered.connect(self.Add)
        self.toolbar.addAction(button_add)
        button_cancel = QAction(QIcon("./toolbarIcons/arrow-180.png"), "Cancel", self)
        button_cancel.triggered.connect(self.Cancel)
        self.toolbar.addAction(button_cancel)

        # file view
        model = QFileSystemModel()
        model.setRootPath(dir_path)
        self.tree = QTreeView()
        self.tree.setModel(model)
        self.tree.setRootIndex(model.index(dir_path))
        self.tree.setColumnWidth(0, 250)
        self.tree.setAlternatingRowColors(True)
        self.root_path = model.rootDirectory().absolutePath()

        layout = QVBoxLayout()
        layout.addWidget(self.tree)
        layout.addWidget(self.toolbar)
        self.setLayout(layout)

    def getSelectedPath(self):
        index = self.tree.currentIndex()
        info = self.tree.model().fileInfo(index)
        return info.fileName(), info.baseName()

    def Add(self):
        relative_path = "/chessGame/images/"
        file_name, name = self.getSelectedPath()
        relative_path = relative_path + file_name
        GraphicItem(relative_path, self.mainWidget, name)
        self.close()

    def Cancel(self):
        self.close()