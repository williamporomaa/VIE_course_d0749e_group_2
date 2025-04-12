from PySide6.QtCore import QAbstractListModel
from PySide6.QtWidgets import QWidget, QTreeView, QListView, QListWidget


class AssetList(QListWidget):
    def __init__(self):
        super().__init__()

        self.items = {}

    def addItemAndName(self, item_name, item):
        # making sure that the item name is not already used
        new_item_name = item_name
        counter = 0;
        while(True):
            if not new_item_name in self.items:
                break
            else:
                counter += 1
                new_item_name = f'{item_name}_{counter}'

        # adding the item into the list
        self.items[new_item_name] = item
        self.addItem(new_item_name)
