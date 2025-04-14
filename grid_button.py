from PySide6.QtCore import QRect
from PySide6.QtWidgets import QComboBox, QInputDialog, QGraphicsRectItem

class GridButton(QComboBox):
    def __init__(self, mainWidget):
        super().__init__()
        self.mainWidget = mainWidget
        #Create empty list
        self.currentGrid = []
        QComboBox.addItem(self, "Generate Grid")
        QComboBox.addItem(self, "8x8 grid")
        QComboBox.addItem(self, "7x6 grid")
        QComboBox.addItem(self, "10x10 grid")
        QComboBox.addItem(self, "Custom grid")

        self.currentIndexChanged.connect(self.generateGrid)

    def generateGrid(self, index):
        scene_width = self.mainWidget.scene_width
        scene_height = self.mainWidget.scene_height
        
        ##clear current grid:
        for item in self.currentGrid:
            self.mainWidget.scene.removeItem(item)
        self.currentGrid.clear()

        if(index == 1):

            for i in range(8):
                for j in range(8):
                                            #left x-cord, left y-cord, width, height
                    self.currentGrid.append(self.mainWidget.scene.addRect(scene_width*i/8, scene_height*j/8, scene_width/8, scene_height/8)) 
            self.mainWidget.scene.gridSizeX = 8
            self.mainWidget.scene.gridSizeY = 8
        elif(index == 2):
            for i in range(7):
                for j in range(6):
                    self.currentGrid.append(self.mainWidget.scene.addRect(scene_width*i/8, scene_height*j/8, scene_width/8, scene_height/8))
            self.mainWidget.scene.gridSizeX = 7
            self.mainWidget.scene.gridSizeY = 6
        elif(index == 3):
            for i in range(10):
                for j in range(10):
                    self.currentGrid.append(self.mainWidget.scene.addRect(scene_width*i/8, scene_height*j/8, scene_width/8, scene_height/8))
            self.mainWidget.scene.gridSizeX = 10
            self.mainWidget.scene.gridSizeY = 10
        elif(index == 4):
            custom_y, ok = QInputDialog.getInt(self.mainWidget, "Custom Grid", "Grid height:")
            if ok and custom_y:
                custom_x, ok = QInputDialog.getInt(self.mainWidget, "Custom Grid", "Grid length:")
                if ok and custom_x:
                    for i in range(custom_x):
                        for j in range(custom_y):
                            self.currentGrid.append(self.mainWidget.scene.addRect(scene_width*i/8, scene_height*j/8, scene_width/8, scene_height/8))
                    self.mainWidget.scene.gridSizeX = custom_x
                    self.mainWidget.scene.gridSizeY = custom_y
                else:
                    #idk some error handling here
                    return
            else:
                #idk some error handling here
                return
        else:
            print("index = ",index)