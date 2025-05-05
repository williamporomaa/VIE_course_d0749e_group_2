from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QToolBar


class ElementView(QWidget):
    def __init__(self, main_widget, element):
        super().__init__()

        self.mainWidget = main_widget
        self.element = element

        layout = QVBoxLayout()

        # toolbar
        toolbar = QToolBar()
        button_close = QAction(QIcon("../toolbarIcons/cross-button.png"), "Close", self)
        button_close.triggered.connect(self.Close)
        toolbar.addAction(button_close)
        layout.addWidget(toolbar)

        # label
        label = QLabel(f"{self.element.name}")
        layout.addWidget(label)

        self.setLayout(layout)

    def Close(self):
        self.mainWidget.elementOpened.remove(self.element.name)
        self.mainWidget.elementView.removeWidget(self)
        self.deleteLater()


