
# FIRST-PARTY PROGRAM MODULES

from data.load_data import get_states_pops # type: ignore
from processing.metrics import gen_states_data # type: ignore
from visualization.chart_builder import get_scatter, get_trendline # type: ignore


# THIRD-PARTY LIBRARIES

# import math
import sys

# import pandas as pd
import pyqtgraph as pg
from PySide6.QtWidgets import QApplication, QWidget, QCheckBox, QVBoxLayout, QCheckBox, QTableWidget, QTableWidgetItem
import numpy as np


# PROGRAM SETUP

# print(QApplication.instance())
app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)


states_pops = get_states_pops()

states_data = gen_states_data(states_pops)

print(states_data)

window = QWidget()
layout = QVBoxLayout(window)
plot_widget = pg.PlotWidget()

def toggle_scatter(state):
    scatter.setVisible(bool(state))

# table setup

table = QTableWidget()
table.setColumnCount(4)
table.setHorizontalHeaderLabels(
    ["State", "Reg Slope", "Reg Int", "R2"]
)
table.setRowCount(len(states_data))

colors = ["r", "g", "b", "c", "m", "y"]
count = 0
for currentState, currentData in states_data.items():

  color = colors[count % len(colors)]
  
  # adds scatter plot and trendline
  scatter = get_scatter(currentData, color)
  plot_widget.addItem(scatter)
  trendline, slope, intercept = get_trendline(currentData, color)
  plot_widget.addItem(trendline)

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

layout.addWidget(plot_widget)
layout.addWidget(table)

window.show()
sys.exit(app.exec())
