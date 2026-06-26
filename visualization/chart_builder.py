# visualization/chart_builder.py

import math
import statistics
import pyqtgraph as pg
import numpy as np

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

  slope, intercept = statistics.linear_regression(rank, size)
  x_line = np.linspace(min(rank), max(rank), 3)
  y_line = slope * x_line + intercept

  r = statistics.correlation(rank, size)
  r2 = r ** 2

  # calculates pattern (log-normal, convex, primate)
  # per https://planningtank.com/settlement-geography/rank-size-rule-by-george-zipf-1949
  city1 = math.e ** size[0]
  city2 = math.e ** size[1]
  city3 = math.e ** size[2]
  if ( city1 > (2 * city2) ):
    pattern = "primate"
  elif ( city2 > ((3/2) * city3) ):
    pattern = "binary"
  # elif (convex):
  #   pattern = "convex"
  else:
    pattern = "log-normal"

  return pg.PlotDataItem(
    x_line,
    y_line,
    pen = color
  ), slope, intercept, r, r2, pattern
