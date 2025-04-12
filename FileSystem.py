from PySide6.QtWidgets import QWidget, QFileSystemModel, QTreeView, QVBoxLayout


class FileSystemView(QWidget):
    def __init__(self, dir_path):
        super().__init__()

        # file view
        model = QFileSystemModel()
        model.setRootPath(dir_path)
        self.tree = QTreeView()
        self.tree.setModel(model)
        self.tree.setRootIndex(model.index(dir_path))
        self.tree.setColumnWidth(0, 250)
        self.tree.setAlternatingRowColors(True)

        layout = QVBoxLayout()
        layout.addWidget(self.tree)
        self.setLayout(layout)

    def get_selected_path(self):
        index = self.tree.currentIndex()
        info = self.tree.model().fileInfo(index)
        return info.absoluteFilePath(), info.baseName()