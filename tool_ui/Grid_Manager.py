from PySide6.QtWidgets import QComboBox, QInputDialog, QMessageBox
import math

class GridButton(QComboBox):
    def __init__(self, mainWidget):
        super().__init__()
        self.mainWidget = mainWidget
        #Create empty list
        self.currentGrid = []
        self.grid_size = 0
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
            self.grid_size = math.sqrt((scene_height*scene_width)/(8*8))
            for i in range(8):
                for j in range(8):
                                            #left x-cord, left y-cord, width, height
                    rect = self.mainWidget.scene.addRect(self.grid_size*i, self.grid_size*j, self.grid_size, self.grid_size)
                    self.currentGrid.append(rect)
            self.mainWidget.scene.gridSizeX = 8
            self.mainWidget.scene.gridSizeY = 8
        elif(index == 2):
            self.grid_size = math.sqrt((scene_height*scene_width)/(7*6))
            for i in range(7):
                for j in range(6):
                    rect = self.mainWidget.scene.addRect(self.grid_size*i, self.grid_size*j, self.grid_size, self.grid_size)
                    self.currentGrid.append(rect)
            self.mainWidget.scene.gridSizeX = 7
            self.mainWidget.scene.gridSizeY = 6
        elif(index == 3):
            self.grid_size = math.sqrt((scene_height*scene_width)/(10*10))
            for i in range(10):
                for j in range(10):
                    rect = self.mainWidget.scene.addRect(self.grid_size*i, self.grid_size*j, self.grid_size, self.grid_size)
                    self.currentGrid.append(rect)
            self.mainWidget.scene.gridSizeX = 10
            self.mainWidget.scene.gridSizeY = 10
        elif(index == 4):
            custom_y, ok = QInputDialog.getInt(self.mainWidget, "Custom Grid", "Grid height:")
            if ok and custom_y:
                custom_x, ok = QInputDialog.getInt(self.mainWidget, "Custom Grid", "Grid length:")
                if ok and custom_x:
                    self.grid_size = math.sqrt((scene_height*scene_width)/(custom_x*custom_y))
                    for i in range(custom_x):
                        for j in range(custom_y):
                            rect = self.mainWidget.scene.addRect(self.grid_size*i, self.grid_size*j, self.grid_size, self.grid_size)
                            self.currentGrid.append(rect)
                    self.mainWidget.scene.gridSizeX = custom_x
                    self.mainWidget.scene.gridSizeY = custom_y
                else:
                    #idk some error handling here
                    QMessageBox.critical(self.mainWidget, "Error", "Invalid input for grid length.")
                    return
            else:
                #idk some error handling here
                QMessageBox.critical(self.mainWidget, "Error", "Invalid input for grid height.")
                return
        else:
            print("index = ",index)
        self.mainWidget.scene.grid_size = self.grid_size
        print(self.mainWidget.scene.grid_size)

    def generateFromTiles(self, tiles):
        ##clear current grid:
        for item in self.currentGrid:
            self.mainWidget.scene.removeItem(item)
        self.currentGrid.clear()

        for tile in tiles:
            rect = self.mainWidget.scene.addRect(tile["x"]-tile["width"]/2, tile["y"]-tile["height"]/2,
                                                 tile["width"], tile["height"])