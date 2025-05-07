from PySide6.QtCore import Qt
from PySide6.QtWidgets import QListWidget


class AssetList(QListWidget):
    def __init__(self, main_widget):
        super().__init__()

        self.items = {}
        self.lastSelectedItem = None
        self.itemClicked.connect(self.onItemClick)
        self.currentItemChanged.connect(self.onCurrentItemChange)
        self.mainWidget = main_widget

    def addItemAndName(self, item_name, item):
        new_item_name = self.checkItemName(item_name)

        # adding the item into the list
        self.items[new_item_name] = item
        self.addItem(new_item_name)

        return new_item_name

    def onItemClick(self, item):
        if self.lastSelectedItem is not None:
            self.items[self.lastSelectedItem].setSelected(False)
        self.lastSelectedItem = item.text()
        self.items[self.lastSelectedItem].setSelected(True)

    def onCurrentItemChange(self, current, previous):
        self.mainWidget.addElementView(self.items[current.text()])

    def checkItemName(self, item_name):
        # making sure that the item nameEdit is not already used
        new_item_name = item_name
        counter = 0
        while (True):
            if not new_item_name in self.items:
                break
            else:
                counter += 1
                new_item_name = f'{item_name}_{counter}'

        return new_item_name

    def changeItem(self, old_item_name, new_item_name):
        new_item_name = self.checkItemName(new_item_name)

        item = self.items[old_item_name]
        del self.items[old_item_name]
        self.items[new_item_name] = item

        self.mainWidget.elementOpened.remove(old_item_name)
        self.mainWidget.elementOpened.append(new_item_name)

        self.findItems(old_item_name,Qt.MatchExactly)[0].setText(new_item_name)

        return new_item_name
