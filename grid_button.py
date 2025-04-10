from PySide6.QtCore import QRectF
from PySide6.QtWidgets import QComboBox, QInputDialog

class GridButton(QComboBox):
    def __init__(self, mainWidget):
        super().__init__()
        self.mainWidget = mainWidget
        QComboBox.addItem(self, "8x8 grid")
        QComboBox.addItem(self, "7x6 grid")
        QComboBox.addItem(self, "10x10 grid")
        QComboBox.addItem(self, "Custom grid")

        self.currentIndexChanged.connect(self.generateGrid)

    def generateGrid(self, index):
        scene_width = self.mainWidget.scene_width
        scene_height = self.mainWidget.scene_height
        
        if(index == 0):
            #left cord, top cord, width, height
            for i in range(8):
                for j in range(8):
                    self.mainWidget.scene.addRect(scene_width*i/8, scene_height*j/8, scene_width/8, scene_height/8)
        elif(index == 1):
            for i in range(7):
                for j in range(6):
                    self.mainWidget.scene.addRect(scene_width*i/8, scene_height*j/8, scene_width/8, scene_height/8)
        elif(index == 2):
            for i in range(10):
                for j in range(10):
                    self.mainWidget.scene.addRect(scene_width*i/8, scene_height*j/8, scene_width/8, scene_height/8)
        elif(index == 3):
            custom_y, ok = QInputDialog.getInt(self.mainWidget, "Custom Grid", "Grid height:")
            if ok and custom_y:
                custom_x, ok = QInputDialog.getInt(self.mainWidget, "Custom Grid", "Grid length:")
                if ok and custom_x:
                    for i in range(custom_x):
                        for j in range(custom_y):
                            self.mainWidget.scene.addRect(scene_width*i/8, scene_height*j/8, scene_width/8, scene_height/8)
                else:
                    #idk some error handling here
                    return
            else:
                #idk some error handling here
                return
        else:
            print("index = ",index)