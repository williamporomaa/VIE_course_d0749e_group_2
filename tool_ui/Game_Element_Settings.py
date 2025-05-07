from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QToolBar, QLineEdit, QHBoxLayout


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

        # nameEdit display
        nameLayout = QHBoxLayout()
        nameLayout.addWidget(QLabel('nameEdit:'))
        self.nameEdit = QLineEdit(f"{self.element.name}")
        self.nameEdit.returnPressed.connect(self.onNameChange)
        nameLayout.addWidget(self.nameEdit)
        mainLayout.addLayout(nameLayout)

        # type display
        # position display
        posLayout = QHBoxLayout()

        posLayout.addWidget(QLabel("x:"))
        self.xEdit = QLineEdit(f"{self.element.getX()}")
        self.xEdit.returnPressed.connect(self.onPosChange)
        posLayout.addWidget(self.xEdit)

        posLayout.addWidget(QLabel("y:"))
        self.yEdit = QLineEdit(f"{self.element.getY()}")
        self.yEdit.returnPressed.connect(self.onPosChange)
        posLayout.addWidget(self.yEdit)

        mainLayout.addLayout(posLayout)

        # scale display
        scaleLayout = QHBoxLayout()
        scaleLayout.addWidget(QLabel('scale:'))
        self.scaleEdit = QLineEdit(f'{self.element.scale()}')
        self.scaleEdit.returnPressed.connect(self.onScaleChange)
        scaleLayout.addWidget(self.scaleEdit)
        mainLayout.addLayout(scaleLayout)

        # flags display

        self.setLayout(layout)

    def onNameChange(self):
        self.element.changeName(self.nameEdit.text())
        self.nameEdit.setText(self.element.name)

    def onPosChange(self):
        try:
            x = float(self.xEdit.text())
            y = float(self.yEdit.text())
            self.element.move(x,y)
        except ValueError:
            pass

        self.xEdit.setText(f'{self.element.getX()}')
        self.yEdit.setText(f'{self.element.getY()}')

    def onScaleChange(self):
        try:
            scale = float(self.scaleEdit.text())
            self.element.setScale(scale)
        except ValueError:
            self.scaleEdit.setText(f'{self.element.scale()}')

    def close(self):
        self.mainWidget.elementOpened.remove(self.element.nameEdit)
        self.mainWidget.elementView.removeWidget(self)
        self.deleteLater()


