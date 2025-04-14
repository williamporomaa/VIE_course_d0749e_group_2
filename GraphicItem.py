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
        x_size = self.mainWidget.scene.gridSizeX
        y_size = self.mainWidget.scene.gridSizeY

        x = self.pos().x()
        y = self.pos().y()
        print("release x: ", x, " releasy y:", y)

        #binary search in x and then do binary search in y
        x = self.itterativeSearch(x_size, x)
        y = self.itterativeSearch(y_size, y)
        print("post-binary search x: ", x, " post-binary search y: ", y)

        self.setX(x*self.mainWidget.scene.grid_size)
        self.setY(y*self.mainWidget.scene.grid_size)

    #works
    def itterativeSearch(self, max, point):
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


