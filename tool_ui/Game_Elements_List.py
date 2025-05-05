from PySide6.QtCore import QAbstractListModel
from PySide6.QtWidgets import QWidget, QTreeView, QListView, QListWidget


class AssetList(QListWidget):
    def __init__(self):
        super().__init__()

        self.items = {}
        self.lastSelectedItem = None
        self.itemClicked.connect(self.onItemClick)

    def addItemAndName(self, item_name, item):
        # making sure that the item name is not already used
        new_item_name = item_name
        counter = 0
        while(True):
            if not new_item_name in self.items:
                break
            else:
                counter += 1
                new_item_name = f'{item_name}_{counter}'

        # adding the item into the list
        self.items[new_item_name] = item
        self.addItem(new_item_name)

        return new_item_name

    def onItemClick(self, item):
        if self.lastSelectedItem is not None:
            self.items[self.lastSelectedItem].setSelected(False)
        self.lastSelectedItem = item.text()
        self.items[self.lastSelectedItem].setSelected(True)
