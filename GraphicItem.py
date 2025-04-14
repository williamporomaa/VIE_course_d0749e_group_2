from PySide6.QtGui import QPixmap, Qt, QKeySequence
from PySide6.QtWidgets import QGraphicsPixmapItem, QGraphicsItem


class GraphicItem(QGraphicsPixmapItem):
    def __init__(self, image, mainWidget, name):
        super().__init__()

        self.setPixmap(QPixmap.fromImage(image))
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemIsFocusable, True)

        mainWidget.scene.addItem(self)
        mainWidget.assetList.addItemAndName(name, self)

        self.mainWidget = mainWidget

    def keyPressEvent(self, event, /):
        if self.isSelected():
            if event.key() == Qt.Key_Plus:
                #plus
                self.setScale(self.scale() + 0.1)
            elif event.key() == Qt.Key_Minus:
                #moins
                self.setScale(self.scale() - 0.1)
    
    def mouseReleaseEvent(self, event):
        x_size = self.mainWidget.scene.gridSizeX/self.mainWidget.scene_width
        y_size = self.mainWidget.scene.gridSizeY/self.mainWidget.scene_height

        print(self.pos())

        self.setX(40)
        self.setY(40)
