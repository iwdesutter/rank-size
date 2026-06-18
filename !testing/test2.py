import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import (
  QApplication, QWidget, QTableView,
  QMainWindow, QVBoxLayout, QLineEdit,
)
from PySide6.QtCore import Qt, QSortFilterProxyModel, QAbstractTableModel


data = [
  [True, "ARG", -0.9035581772038382, 14.957180389508208],
  [True, "BOL", -1.0181784994358000, 13.949869457907640],
  [True, "BRA", -0.8121718699311921, 15.829136393408662],
  [True, "CAN", -0.7500515016436984, 14.335433416261894],
  [True, "CHL", -0.8835318766859168, 14.153462235420754]
]

# bools = [
#   [True, None, None, None],
#   [True, None, None, None],
#   [True, None, None, None],
#   [True, None, None, None],
#   [True, None, None, None]
# ]

class TableModel(QAbstractTableModel):

  def __init__(self, data, checked):
      super().__init__()
      self._data = data
      self._checked = checked

  def data(self, index, role):
      if role == Qt.ItemDataRole.DisplayRole and index.column() != 0:
          value = self._data[index.row()][index.column()]
          return str(value)

      if role == Qt.ItemDataRole.CheckStateRole and index.column() == 0:
          checked = self._checked[index.row()][index.column()]
          if checked:
              return Qt.CheckState.Checked
          return Qt.CheckState.Unchecked

  def setData(self, index, value, role):
      if role == Qt.ItemDataRole.CheckStateRole and index.column() == 0:
          checked = value == Qt.CheckState.Checked.value
          self._checked[index.row()][index.column()] = checked
          self.dataChanged.emit(index, index, [role])

          if checked:
            print("I am now checked")
            print(data[index.row()][1])
          else:
            print("I am now unchecked")
            print(data[index.row()][1])

          return True
      
      return False

  def rowCount(self, index):
    return len(self._data)

  def columnCount(self, index):
    return len(self._data[0])
  
  def flags(self, index):
    return (
        Qt.ItemFlag.ItemIsSelectable
        | Qt.ItemFlag.ItemIsEnabled
        | Qt.ItemFlag.ItemIsUserCheckable
    )


class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.table = QTableView()

    

    self.model = TableModel(data, data)
    self.proxy_model = QSortFilterProxyModel()
    self.proxy_model.setFilterKeyColumn(-1)  # Search all columns.
    self.proxy_model.setSourceModel(self.model)

    # self.proxy_model.sort(0, Qt.AscendingOrder)

    self.table.setModel(self.proxy_model)

    self.searchbar = QLineEdit()
    self.searchbar.setPlaceholderText("Type to filter...")

    self.searchbar.textChanged.connect(
      self.proxy_model.setFilterFixedString
    )

    layout = QVBoxLayout()
    layout.addWidget(self.searchbar)
    layout.addWidget(self.table)

    container = QWidget()
    container.setLayout(layout)

    self.setCentralWidget(container)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

input("Close program.")