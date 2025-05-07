from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QToolBar, QTextEdit, QLineEdit


class ElementView(QWidget):
    def __init__(self, main_widget, element):
        super().__init__()

        self.mainWidget = main_widget
        self.element = element

        layout = QVBoxLayout()

        # toolbar
        toolbar = QToolBar()
        button_close = QAction(QIcon("../toolbarIcons/cross-button.png"), "Close", self)
        button_close.triggered.connect(self.close)
        toolbar.addAction(button_close)
        layout.addWidget(toolbar)

        # main part
        mainWindow = QWidget()
        mainLayout = QVBoxLayout()
        mainWindow.setLayout(mainLayout)
        layout.addWidget(mainWindow)

        # name display
        self.name = QLineEdit(f"{self.element.name}")
        self.name.returnPressed.connect(self.onNameChange)
        mainLayout.addWidget(self.name)

        self.setLayout(layout)

    def onNameChange(self):
        new_name = self.element.changeName(self.name.text())
        self.name.setText(new_name)

    def close(self):
        self.mainWidget.elementOpened.remove(self.element.name)
        self.mainWidget.elementView.removeWidget(self)
        self.deleteLater()


