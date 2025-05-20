from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QToolBar, QLineEdit, QHBoxLayout, QComboBox, QMenu

from tool_ui.Enums import ElementTypes


class ElementView(QWidget):
    def __init__(self, main_widget, element):
        super().__init__()

        self.mainWidget = main_widget
        self.element = element

        layout = QVBoxLayout()

        # toolbar
        toolbar = QToolBar()
        button_close = QAction(QIcon("./toolbarIcons/cross-button.png"), "Close", self)
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
        nameLayout.addWidget(QLabel('name:'))
        self.nameEdit = QLineEdit(f"{self.element.name}")
        self.nameEdit.returnPressed.connect(self.onNameChange)
        nameLayout.addWidget(self.nameEdit)
        mainLayout.addLayout(nameLayout)

        # type display
        typeLayout = QHBoxLayout()
        typeLayout.addWidget(QLabel('type'))
        self.typeCombo = QComboBox()
        for type in ElementTypes:
            self.typeCombo.addItem(type.name)
        self.typeCombo.setCurrentText(self.element.elementType.name)
        self.typeCombo.currentIndexChanged.connect(self.onTypeChange)
        typeLayout.addWidget(self.typeCombo)
        mainLayout.addLayout(typeLayout)

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
        flagsLayout = QVBoxLayout()
        flagsLayout.addWidget(QLabel('flags:'))

        self.currentFlagsLayout = QVBoxLayout()
        for flag in self.element.gameFlags:
            self.addFlag(flag)
        flagsLayout.addLayout(self.currentFlagsLayout)

        self.flagCombo = QComboBox()
        self.flagCombo.addItem('add a flag')
        for flag in ElementTypes.flags(self.element.elementType):
            if not flag in self.element.gameFlags:
                self.flagCombo.addItem(flag.name)
        self.flagCombo.activated.connect(self.onFlagAdd)
        flagsLayout.addWidget(self.flagCombo)
        mainLayout.addLayout(flagsLayout)

        self.setLayout(layout)

    def addFlag(self, flag):
        flagLayout = QHBoxLayout()
        flagLabel = QLabel(flag.name)
        flagLayout.addWidget(flagLabel)

        flagButton = QAction(QIcon("./toolbarIcons/cross-button.png"), "remove flag", self)
        flagButton.triggered.connect(self.onFlagRemove)
        flagMenu = QMenu()
        flagMenu.addAction(flagButton)
        flagLayout.addWidget(flagMenu)

        flagWidget = QWidget()
        flagWidget.setLayout(flagLayout)
        self.currentFlagsLayout.addWidget(flagWidget)
        flagLabel.setParent(flagWidget)
        flagButton.setParent(flagWidget)

    def onNameChange(self):
        self.element.changeName(self.nameEdit.text())
        self.nameEdit.setText(self.element.name)

    def onTypeChange(self):
        self.element.changeType(ElementTypes[self.typeCombo.currentText()])

    def onPosChange(self):
        try:
            x = float(self.xEdit.text())
            y = float(self.yEdit.text())
            self.element.move(x,y)
        except ValueError:
            self.actualizePosAndScale()

    def onScaleChange(self):
        try:
            scale = float(self.scaleEdit.text())
            self.element.setScale(scale)
        except ValueError:
            self.actualizePosAndScale()

    def onFlagAdd(self, index):
        if not self.flagCombo.currentIndex() == 0:
            flag = ElementTypes.flags(self.element.elementType)[self.flagCombo.currentText()]
            self.element.gameFlags.append(flag)

            self.addFlag(flag)

            self.flagCombo.removeItem(index)
            self.flagCombo.setCurrentText('add a flag')

    def onFlagRemove(self):
        flagWidget = self.sender().parent()
        flag = ElementTypes.flags(self.element.elementType)[flagWidget.children()[1].text()]
        self.element.gameFlags.remove(flag)

        self.currentFlagsLayout.removeWidget(flagWidget)
        flagWidget.deleteLater()

        self.flagCombo.addItem(flag.name)

    def actualizePosAndScale(self):
        self.xEdit.setText(f'{self.element.getX()}')
        self.yEdit.setText(f'{self.element.getY()}')
        self.scaleEdit.setText(f'{self.element.scale()}')


    def close(self):
        self.mainWidget.elementOpened.remove(self.element.name)
        self.mainWidget.elementView.removeWidget(self)
        self.deleteLater()


