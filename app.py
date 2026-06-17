
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
from PySide6.QtWidgets import QApplication, QWidget, QCheckBox, QVBoxLayout, QHBoxLayout, QFormLayout, QTableWidget, QTableWidgetItem, QGroupBox, QPushButton, QLineEdit, QLabel, QFileDialog, QTableView, QMainWindow
# import numpy as np
# from PySide6.QtCore import Qt, QSortFilterProxyModel, QAbstractTableModel


# PROGRAM SETUP

# print(QApplication.instance())
app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Rank-Size Rule")


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

# header box inputs
# label_line_city_header = QLabel("City Header:")
# line_city_header = QLineEdit()
# label_line_city_header.setBuddy(line_city_header)
# layout_form_header.addRow(label_line_city_header, line_city_header)

label_line_state_header = QLabel("State Header:")
line_state_header = QLineEdit()
label_line_state_header.setBuddy(line_state_header)
layout_form_header.addRow(label_line_state_header, line_state_header)

label_line_pop_header = QLabel("Pop Header:")
line_pop_header = QLineEdit()
label_line_pop_header.setBuddy(line_pop_header)
layout_form_header.addRow(label_line_pop_header, line_pop_header)

# side-by-side forms for min/max pop/cities
# layout_form_pops = QFormLayout()
# layout_form_cities = QFormLayout()
# layout_forms_pops_cities.addLayout(layout_form_pops)
# layout_forms_pops_cities.addLayout(layout_form_cities)

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



table = QTableWidget()

header_lyst = ["", "State", "Reg Slope", "Reg Int", "R2"]
table.setColumnCount(len(header_lyst))
table.setHorizontalHeaderLabels(header_lyst)

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

  table.setRowCount(len(states_data))
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

    checkbox = QCheckBox()
    checkbox.setChecked(True)

    currentStateWidget = QLabel("<span style='color:" + color + "; font-weight: bold;'>" + currentState + "</span>")
    # layout.addWidget(checkbox)

    # adds checkboxes
    def make_toggle(scatter):
      def toggle(state):
          scatter.setVisible(bool(state))
      return toggle

    checkbox.stateChanged.connect(make_toggle(scatter))
    checkbox.stateChanged.connect(make_toggle(trendline))

    # adds checkboxes, data to table

    table.setCellWidget(count, 0, checkbox)
    table.setCellWidget(count, 1, currentStateWidget)
    table.setItem(count, 2, QTableWidgetItem(str(slope)))
    table.setItem(count, 3, QTableWidgetItem(str(intercept)))

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

    data_objects[currentState] = [scatter, trendline, checkbox]
  
  print(data_objects)

  # column width resizing
  table.resizeColumnToContents(0)

  # print(data_lyst)


window.show()
sys.exit(app.exec())
