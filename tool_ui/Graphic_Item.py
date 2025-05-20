import os
import sys

from PySide6.QtGui import QPixmap, Qt, QImage
from PySide6.QtWidgets import QGraphicsPixmapItem, QGraphicsItem

from Enums import ElementTypes, PieceFlags


class GraphicItem(QGraphicsPixmapItem):
    def __init__(self, path, mainWidget, name, type=ElementTypes.Piece):
        super().__init__()

        try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
            folder_path = sys._MEIPASS
        except AttributeError:
            folder_path = os.path.abspath(".")
        file_path = folder_path + path

        self.setPixmap(QPixmap.fromImage(QImage(file_path)))
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemIsFocusable, True)

        height = self.sceneBoundingRect().height()
        width = self.sceneBoundingRect().width()
        self.setOffset(-width/2 +0.5, -height/2 +0.5)

        mainWidget.scene.addItem(self)
        new_name = mainWidget.assetList.addItemAndName(name, self)
        self.name = new_name

        self.imagePath = path
        self.elementType = type
        self.mainWidget = mainWidget
        self.gameFlags = []

    def getX(self):
        return self.pos().x()

    def getY(self):
        return self.pos().y()

    def getHeight(self):
        return self.sceneBoundingRect().height()

    def getWidth(self):
        return self.sceneBoundingRect().width()

    def getFlagsValues(self):
        res = []
        for flag in self.gameFlags:
            res.append(flag.value)
        return res

    def keyPressEvent(self, event, /):
        if self.isSelected():
            if event.key() == Qt.Key_Plus:
                #plus
                self.changeScale(self.scale() + 0.1)
            elif event.key() == Qt.Key_Minus:
                #moins
                self.changeScale(self.scale() - 0.1)

    def changeScale(self, new_scale):
        self.setScale(new_scale)
        self.mainWidget.acualizeElementView()

    def mousePressEvent(self, event, /):
        list = self.mainWidget.assetList
        list.setCurrentItem(list.findItems(self.name,Qt.MatchFixedString)[0])
    
    def mouseReleaseEvent(self, event):
        x = self.pos().x()
        y = self.pos().y()
        #print("release x: ", x, " releasy y:", y)
        self.move(x,y)
        
        super().mouseReleaseEvent(event)

    def move(self, x, y):
        if (self.elementType is ElementTypes.Piece) and (PieceFlags.IsSnapping in self.gameFlags):
            x_size = self.mainWidget.scene.gridSizeX
            y_size = self.mainWidget.scene.gridSizeY

            # binary search in x and then do binary search in y
            x = self.iterativeSearch(x_size, x)
            y = self.iterativeSearch(y_size, y)
            # print("post-binary search x: ", x, " post-binary search y: ", y)

            self.setX((x + 0.5) * self.mainWidget.scene.grid_size)
            self.setY((y + 0.5) * self.mainWidget.scene.grid_size)
        else:
            self.setX(x)
            self.setY(y)
        self.mainWidget.acualizeElementView()

    #works
    def iterativeSearch(self, max, point):
        if(self.mainWidget.scene.grid_size > point):
            return 0
        i = 1
        while i <= max:
            if i*self.mainWidget.scene.grid_size > point:
                return i -1
            i += 1
            
        return max-1

    #doesnt work :(
    def binarySearch(self, high, point):
        low = 0
        while low < high and low >= 0:
            mid = low+high//2
            if(point == mid*self.mainWidget.scene.grid_size):
                #found it instantly (highly unlikely)
                return mid
            elif(point > mid*self.mainWidget.scene.grid_size):
                low = mid+1
            else:
                high = mid-1
        
        return(high+low//2)

    def changeName(self, new_name):
        new_name = self.mainWidget.assetList.changeItem(self.name, new_name)
        self.name = new_name

    def changeType(self, type):
        self.elementType = type
        self.gameFlags.clear()