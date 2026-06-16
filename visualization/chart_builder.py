# visualization/chart_builder.py

# import math
# import sys
# import pandas as pd
import pyqtgraph as pg
import numpy as np
# from PySide6.QtWidgets import QApplication, QWidget, QCheckBox, QVBoxLayout

# plot = pg.plot()
# plot.setLabel("bottom", "Rank Log")
# plot.setLabel("left", "Size Log")

def get_scatter(currentData, color):
  return pg.ScatterPlotItem(
    x = currentData["rank"],
    y = currentData["size"],
    size = 5,
    pen = color
  )

def get_trendline(currentData, color):

  rank = currentData["rank"]
  size = currentData["size"]

  slope, intercept, *_ = np.polyfit(rank, size, deg = 1)
  x_line = np.linspace(min(rank), max(rank), 100)
  y_line = slope * x_line + intercept

  return pg.PlotDataItem(
    x_line,
    y_line,
    pen = color
  ), slope, intercept
