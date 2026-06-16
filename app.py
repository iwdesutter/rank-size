
# FIRST-PARTY PROGRAM MODULES

from data.load_data import get_states_pops_demo_am, get_states_pops # type: ignore
from processing.metrics import refine_states_pops, gen_states_data # type: ignore
from visualization.chart_builder import get_scatter, get_trendline # type: ignore


# THIRD-PARTY LIBRARIES

# import math
import sys

# import pandas as pd
import pyqtgraph as pg
from PySide6.QtWidgets import QApplication, QWidget, QCheckBox, QVBoxLayout, QHBoxLayout, QFormLayout, QTableWidget, QTableWidgetItem, QGroupBox, QPushButton, QLineEdit, QLabel, QFileDialog
# import numpy as np


# PROGRAM SETUP

# print(QApplication.instance())
app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)

window = QWidget()

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

layout_l_sidebar.addLayout(layout_button_files)
layout_l_sidebar.addLayout(layout_file_path)
layout_l_sidebar.addLayout(layout_form_header)
layout_l_sidebar.addWidget(button_build_cities)
layout_l_sidebar.addLayout(layout_forms_pops_cities)
layout_l_sidebar.addWidget(button_calc_viz)

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
line_min_cities.setText("3")
line_max_cities.setText("10000000000")

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














# table setup

table = QTableWidget()
table.setColumnCount(4)
table.setHorizontalHeaderLabels(
    ["State", "Reg Slope", "Reg Int", "R2"]
)
layout_center.addWidget(plot_widget)
layout_center.addWidget(table)
colors = ["r", "g", "b", "c", "m", "y"]

def display_data(states_data):

  table.setRowCount(len(states_data))

  count = 0
  for currentState, currentData in states_data.items():

    color = colors[count % len(colors)]
    
    # adds scatter plot and trendline
    scatter = get_scatter(currentData, color)

    # this function here should probably be defined outside of the loop, but I'll have to work out a solution later which still allows scatter to be defined
    def toggle_scatter(state):
      scatter.setVisible(bool(state))

    plot_widget.addItem(scatter)
    trendline, slope, intercept = get_trendline(currentData, color)
    plot_widget.addItem(trendline)
    plot_widget.setLabel("bottom", "Rank Log")
    plot_widget.setLabel("left", "Size Log")

    checkbox = QCheckBox(currentState)
    checkbox.setChecked(True)
    layout.addWidget(checkbox)

    # adds checkboxes
    def make_toggle(scatter):
      def toggle(state):
          scatter.setVisible(bool(state))
      return toggle

    checkbox.stateChanged.connect(make_toggle(scatter))
    checkbox.stateChanged.connect(make_toggle(trendline))

    # adds checkboxes, data to table

    table.setCellWidget(count, 0, checkbox)
    table.setItem(count, 1, QTableWidgetItem(str(slope)))
    table.setItem(count, 2, QTableWidgetItem(str(intercept)))

    print(currentState, slope, intercept)
    count += 1


window.show()
sys.exit(app.exec())
