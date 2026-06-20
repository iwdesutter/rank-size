
# FIRST-PARTY PROGRAM MODULES

from data.load_data import get_states_pops_demo_am, get_states_pops, export_csv # type: ignore
from processing.metrics import refine_states_pops, gen_states_data # type: ignore
from visualization.chart_builder import get_scatter, get_trendline # type: ignore


# THIRD-PARTY LIBRARIES

# import math
import sys
import csv

# import pandas as pd
import pyqtgraph as pg
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QWidget, QCheckBox, QVBoxLayout, QHBoxLayout, QFormLayout, QTableWidget, QTableWidgetItem, QGroupBox, QPushButton, QLineEdit, QLabel, QFileDialog, QTableView, QMainWindow
# import numpy as np
from PySide6.QtCore import Qt, QSortFilterProxyModel, QAbstractTableModel
from PySide6.QtGui import QFont, QColor


# PROGRAM SETUP

# print(QApplication.instance())
app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Rank-Size Ruler")


# FULL UI LAYOUT
layout = QHBoxLayout(window)
plot_widget = pg.PlotWidget()

# LEFT SIDEBAR
layout_l_sidebar = QVBoxLayout()
layout.addLayout(layout_l_sidebar)

layout_button_files = QHBoxLayout()
layout_file_path = QHBoxLayout() 
layout_form_header = QFormLayout()
button_build_cities = QPushButton("Build Cities List")
layout_forms_pops_cities = QFormLayout()
button_calc_viz = QPushButton("Calculate && Visualize")
layout_file_path_export = QHBoxLayout() 

group_uploading = QGroupBox("Loading Data")
group_calculation = QGroupBox("Calculation && Visualization")
group_analysis = QGroupBox("Analysis && Export")
group_uploading_layout = QVBoxLayout()
group_calculation_layout = QVBoxLayout()
group_analysis_layout = QVBoxLayout()
group_uploading.setLayout(group_uploading_layout)
group_calculation.setLayout(group_calculation_layout)
group_analysis.setLayout(group_analysis_layout)

layout_l_sidebar.addLayout(layout_button_files)
layout_l_sidebar.addWidget(group_uploading)
layout_l_sidebar.addWidget(group_calculation)
layout_l_sidebar.addWidget(group_analysis)

group_uploading_layout.addLayout(layout_file_path)
group_uploading_layout.addLayout(layout_form_header)
group_uploading_layout.addWidget(button_build_cities)
group_calculation_layout.addLayout(layout_forms_pops_cities)
group_calculation_layout.addWidget(button_calc_viz)
group_analysis_layout.addLayout(layout_file_path_export)

# LEFT SIDEBAR SUBWIDGETS

# DEMO upload buttons
button_upload_demo1 = QPushButton("Demo File (Americas)")
button_upload_demo2 = QPushButton("Demo File (Other)")
layout_button_files.addWidget(button_upload_demo1)
layout_button_files.addWidget(button_upload_demo2)

# FILE upload button and path text
button_upload_file = QPushButton("Upload File")
line_file_path = QLineEdit()
layout_file_path.addWidget(button_upload_file)
layout_file_path.addWidget(line_file_path)

label_line_state_header = QLabel("State Header:")
line_state_header = QLineEdit()
label_line_state_header.setBuddy(line_state_header)
layout_form_header.addRow(label_line_state_header, line_state_header)

label_line_pop_header = QLabel("Pop Header:")
line_pop_header = QLineEdit()
label_line_pop_header.setBuddy(line_pop_header)
layout_form_header.addRow(label_line_pop_header, line_pop_header)


label_line_min_pop = QLabel("Min Pop:")
line_min_pop = QLineEdit()
label_line_min_pop.setBuddy(line_min_pop)
layout_forms_pops_cities.addRow(label_line_min_pop, line_min_pop)

label_line_max_pop = QLabel("Max Pop:")
line_max_pop = QLineEdit()
label_line_max_pop.setBuddy(line_max_pop)
layout_forms_pops_cities.addRow(label_line_max_pop, line_max_pop)

label_line_min_cities = QLabel("Min Cities:")
line_min_cities = QLineEdit()
label_line_min_cities.setBuddy(line_min_cities)
layout_forms_pops_cities.addRow(label_line_min_cities, line_min_cities)

label_line_max_cities = QLabel("Max Cities:")
line_max_cities = QLineEdit()
label_line_max_cities.setBuddy(line_max_cities)
layout_forms_pops_cities.addRow(label_line_max_cities, line_max_cities)

# ANALYSIS & EXPORT

button_export_location = QPushButton("Export Location")
line_export_location = QLineEdit()
layout_file_path_export.addWidget(button_export_location)
layout_file_path_export.addWidget(line_export_location)

button_export_csv = QPushButton("Export Table as CSV")
group_analysis_layout.addWidget(button_export_csv)

# CENTER LAYOUT
layout_center = QVBoxLayout()
layout.addLayout(layout_center)



# UI INPUT BEHAVIORS
line_file_path.setText("C:/Users/eatyo/OneDrive/Desktop/Rank-Size/!testing/WUP2025-F21-DEGURBA-Cities_Pop.csv")

# line_city_header.setText("City_Name")
line_state_header.setText("ISO3_Code")
line_pop_header.setText("2025")

line_min_pop.setText("0")
line_max_pop.setText("10000000000")
line_min_cities.setText("7")
line_max_cities.setText("10000")

def do_demo_data_am():
  # print(line_city_header.text())
  states_pops = get_states_pops_demo_am()
  states_data = gen_states_data(states_pops)
  display_data(states_data)

def get_file_data():
  file_dialog = QFileDialog()
  # layout.addWidget(file_dialog)
  path, filetype = file_dialog.getOpenFileName()
  print(path)
  line_file_path.setText(path)

def get_file_data_export():
  file_dialog = QFileDialog.getExistingDirectory()
  # layout.addWidget(file_dialog)
  # path, filetype = file_dialog.getOpenFileName()
  path = file_dialog
  print(path)
  line_export_location.setText(path + "/output.csv")

def build_cities():
  path = line_file_path.text()
  state_header = line_state_header.text()
  pop_header = line_pop_header.text()

  global states_pops
  states_pops = get_states_pops(path, state_header, pop_header)
  
def calc_and_viz():
  global states_pops
  # global states_data

  # refines city/pop list based on parameters
  popMin = int(line_min_pop.text())
  popMax = int(line_min_pop.text())
  citiesMin = int(line_min_cities.text())
  citiesMax = int(line_max_cities.text())
  states_pops = refine_states_pops(states_pops, popMin, popMax, citiesMin, citiesMax)
  print(states_pops)

  states_data = gen_states_data(states_pops)
  display_data(states_data)

button_upload_demo1.clicked.connect(do_demo_data_am)
button_upload_demo1.show()

button_upload_file.clicked.connect(get_file_data)
button_upload_file.show()

button_build_cities.clicked.connect(build_cities)
button_build_cities.show()

button_calc_viz.clicked.connect(calc_and_viz)
button_calc_viz.show()

def export_csv_lyst():
  path = line_export_location.text()
  return export_csv(data_lyst, path)

button_export_location.clicked.connect(get_file_data_export)
button_export_location.show()

button_export_csv.clicked.connect(export_csv_lyst)
button_export_csv.show()



table = QTableView()

header_lyst = ["", "State", "Reg Slope", "Reg Int", "R2"]
# table.setColumnCount(len(header_lyst))
# table.setHorizontalHeaderLabels(header_lyst)

layout_center.addWidget(plot_widget)

# layout_center.addWidget(QCheckBox())


plot_widget.setLabel("bottom", "Rank Log")
plot_widget.setLabel("left", "Size Log")

# FILTER (i.e. checkbox, line filter) LAYOUT & BEHAVIOR
checkbox_main = QCheckBox("")
searchbar = QLineEdit()
layout_center_filter = QHBoxLayout()
layout_center.addLayout(layout_center_filter)
layout_center_filter.addWidget(checkbox_main)
layout_center_filter.addWidget(searchbar)

searchbar.setPlaceholderText("Type to filter table")
def update_from_searchbar():
  print(searchbar.text())

layout_center.addWidget(table)
colors = ["#FF0000", "#00FF00", "#0000FF", "#00FFFF", "#FF00FF", "#FFFF00"]

# def make_lyst_to_table():
#    pass



# CHECKBOX DELEGATES & SEARCHBAR FUNCTIONALITY FROM
# https://www.pythonguis.com/tutorials/pyside6-widget-search-bar/
# https://www.pythonguis.com/faq/how-to-create-a-filter-search-bar-for-a-qtablewidget/

def get_delegate_obj(index_row):
  state_name = data_lyst[index_row + 1][0]
  scatter = data_objects[state_name][0]
  trendline = data_objects[state_name][1]
  return scatter, trendline

class TableModel(QAbstractTableModel):

  def __init__(self, data, checked):
    super().__init__()
    self._data = data
    self._checked = checked

  def data(self, index, role):
    if role == Qt.ItemDataRole.DisplayRole and index.column() != 0: # only operates on non-checkbox columns
      value = self._data[index.row()][index.column() - 1]
      return str(value)

    if role == Qt.ItemDataRole.CheckStateRole and index.column() == 0: # only operates on initial checkbox column
      checked = self._checked[index.row()][0]
      if checked:
        return Qt.CheckState.Checked.value
      return Qt.CheckState.Unchecked.value
    
    # sets weight, color

    if role == Qt.ItemDataRole.FontRole and index.column() == 1:
      font = QFont()
      font.setBold(True)
      return font
    
    if role == Qt.ItemDataRole.ForegroundRole:
      if index.column() == 1:
        return QColor(colors[index.row() % len(colors)])
      
  def checked_states(self):
    # print(proxy_model)
    # row = 0
    # column = 0
    # proxy_index = proxy_model.index(row, column)

    # value = proxy_model.data(proxy_index, Qt.ItemDataRole.DisplayRole)
    # checked = proxy_model.data(proxy_index, Qt.ItemDataRole.CheckStateRole)
    # print(value, checked)
    # print(proxy_model.rowCount())

    proxy_bools = []
    for row in range(proxy_model.rowCount()):
      if proxy_model.data(proxy_model.index(row, 0), Qt.ItemDataRole.CheckStateRole) == 2:
        currentBool = True
      else:
        currentBool = False
      proxy_bools.append(currentBool)

    # print(proxy_bools)
    return proxy_bools
  
  def set_all_checked_state(self, state):
    print("!!!!!")
    print("We're turning them", state)

    changed_rows = []
    proxy = proxy_model

    # identifies proxy rows in original (full, unsearched) model
    for proxy_row in range(proxy.rowCount()):
      source_index = proxy.mapToSource(
        proxy.index(proxy_row, 0)
      )
      
      self.setData(
        source_index,
        state,
        Qt.ItemDataRole.CheckStateRole,
        remind = False
      )

      changed_rows.append(source_index.row())

    # updates checkboxes in table
    for row in changed_rows:
      idx = self.index(row, 0)
      self.dataChanged.emit(
        idx,
        idx,
        [Qt.ItemDataRole.CheckStateRole]
      )
    # updates whole table
    # print(self.index(0, 0))
    self.dataChanged.emit(
        self.index(0, 0),
        self.index(len(self._checked) - 1, 0),
        [Qt.ItemDataRole.CheckStateRole]
    )

  def remind_main_checkbox(self):
    states = self.checked_states()
    if all(states):
      checkbox_main.setCheckState(Qt.CheckState.Checked)
    elif not any(states):
      checkbox_main.setCheckState(Qt.CheckState.Unchecked)
    else:
      checkbox_main.setCheckState(Qt.CheckState.PartiallyChecked)

  def setData(self, index, value, role, remind = True):
    if role == Qt.ItemDataRole.CheckStateRole and index.column() == 0: # only operates on initial checkbox column

      print("The checkbox has the value", value)
      if Qt.CheckState.Checked.value == 2:
        currentCheckValue = True
      else:
        currentCheckValue = False

      if value == 2:
        value = True
      
      checked = (value == currentCheckValue)
      # print(value, currentCheckValue)
      self._checked[index.row()][0] = checked
      self.dataChanged.emit(index, index, [role])

      adjacent_scatter, adjacent_trendline = get_delegate_obj(index.row())

      if checked:
        # print("I am now checked")
        # adjacent_scatter, adjacent_trendline = get_delegate_obj(index.row())
        plot_widget.addItem(adjacent_scatter)
        plot_widget.addItem(adjacent_trendline)
      else:
        # print("I am now unchecked")
        plot_widget.removeItem(adjacent_scatter)
        plot_widget.removeItem(adjacent_trendline)

      # changes state of main checkbox based on states of all checkboxes
      if remind:
        print("We ARE running remind!")
        model.remind_main_checkbox()

      # print(states)
      # checkbox_main.setCheckState(Qt.CheckState.PartiallyChecked)
      # self.dataChanged.emit(
      #   index,
      #   index,
      #   [Qt.ItemDataRole.CheckStateRole]
      # )

      return True
    
    return False

  def rowCount(self, index):
    return len(self._data)

  def columnCount(self, index):
    return len(self._data[0]) + 1
  
  # Source - https://stackoverflow.com/a/64288596
  # Posted by musicamante
  # Retrieved 2026-06-18, License - CC BY-SA 4.0
  def headerData(self, section, orientation, role = QtCore.Qt.DisplayRole):
    if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
      return header_lyst[section]
    return super().headerData(section, orientation, role)

  def flags(self, index):
    return (
      Qt.ItemFlag.ItemIsSelectable
      | Qt.ItemFlag.ItemIsEnabled
      | Qt.ItemFlag.ItemIsUserCheckable
    )















def display_data(states_data):

  # clears existing scatters/trendlines from chart
  # if plot_widget.listDataItems() != []:
  # for item in plot_widget.listDataItems():
  #   plot_widget.removeItem(item)
  # plot_widget.clear()
  global data_objects
  data_objects = {}
  for state, objects in data_objects.items():
    for item in objects:
      plot_widget.removeItem(item)

  # table.setRowCount(len(states_data))
  global data_lyst
  data_lyst = [header_lyst[1:len(header_lyst)]] # takes header list, excluding first item

  count = 0
  
  for currentState, currentData in states_data.items():

    color = colors[count % len(colors)]
    
    # adds scatter plot and trendline
    scatter = get_scatter(currentData, color)

    # def toggle_scatter(state):
    #   scatter.setVisible(bool(state))

    plot_widget.addItem(scatter)
    trendline, slope, intercept = get_trendline(currentData, color)
    plot_widget.addItem(trendline)



    # bool_show_state = True
    new_lyst = []
    # new_lyst.append(True)
    new_lyst.append(currentState)
    # if bool_show_state:
    #   new_lyst.append("Long Country Name")       
    new_lyst.append(float(slope))
    new_lyst.append(float(intercept))
    data_lyst.append(new_lyst)

    # print(currentState, slope, intercept)
    count += 1

    data_objects[currentState] = [scatter, trendline]
  
  print(data_objects)

  # column width resizing


  data_lyst_ex_header = data_lyst[1:len(data_lyst)]

  trues = [] # this code fixes stupid issue where APPARENTLY [True] * 67 or whatever makes multiple references to the same thing...
  for item in data_lyst_ex_header:
    trues.append([True])

  global model
  model = TableModel(data_lyst_ex_header, trues)
  global proxy_model
  proxy_model = QSortFilterProxyModel()
  proxy_model.setFilterKeyColumn(-1)  # Search all columns.
  proxy_model.setSourceModel(model)

  print(data_lyst_ex_header)

  checkbox_main.setCheckState(Qt.CheckState.Checked)

  table.setModel(proxy_model)
  # table.setHorizontalHeader(header_lyst)
  table.resizeColumnToContents(0)
  table.resizeColumnToContents(1)

  searchbar.textChanged.connect(
    proxy_model.setFilterFixedString
  )

  table.setDragEnabled(False)
  # updates state of main checkbox when view searchbar/view is updated
  searchbar.textChanged.connect(model.remind_main_checkbox)

  table.show()

# changes state of all checkboxes based on state of main checkbox
def force_checkboxes():
  state = checkbox_main.isChecked()
  print(state)
  # print(state)
  # print(model)
  model.set_all_checked_state(state)
checkbox_main.clicked.connect(force_checkboxes)

def skip_intermediate():
  if checkbox_main.checkState() == Qt.CheckState.PartiallyChecked:
    checkbox_main.setCheckState(Qt.CheckState.Checked)
checkbox_main.clicked.connect(skip_intermediate)

window.show()
sys.exit(app.exec())
