import pyqtgraph as pg
import numpy as np
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget

# Create a Qt application
app = QApplication([])

# Create a main window
win = QMainWindow()
win.setWindowTitle('Natural Selection Simulation')

# Create a central widget and layout
central_widget = QWidget(win)
layout = QHBoxLayout()
central_widget.setLayout(layout)
win.setCentralWidget(central_widget)

simulationPlot = pg.PlotWidget()
trackerPlot = pg.PlotWidget()

layout.addWidget(simulationPlot)
layout.addWidget(trackerPlot)

# Initialize data for each plot
num_points = 50
x_data = np.random.rand(num_points)
y_data = np.random.rand(num_points)
size_data = np.random.randint(10, 100, num_points)

foodScatter = pg.ScatterPlotItem(x=x_data, y=y_data, size=size_data)
organismScatter = pg.ScatterPlotItem(x=x_data, y=y_data, size=size_data)

simulationPlot.addItem(foodScatter)
simulationPlot.addItem(organismScatter)

simulationPlot.setXRange(0,1)
simulationPlot.setYRange(0,1)

color = QColor(255, 0, 0)  # Red color (RGB values)
brush = QBrush(color)
organismScatter.setBrush(brush)

color = QColor(0, 255, 0)  # Red color (RGB values)
brush = QBrush(color)
foodScatter.setBrush(brush)


# Functions to update data for each plot
def UpdateSimulationPlot():

    x_data = np.random.rand(num_points)
    y_data = np.random.rand(num_points)
    size_data = np.random.randint(10, 100, num_points)

    organismScatter.setData(x=x_data, y=y_data)
    organismScatter.setSize(size_data)
    

def UpdateTrackerPlot():
    pass

timer = QTimer()
timer.timeout.connect(UpdateSimulationPlot)
timer.timeout.connect(UpdateTrackerPlot)
timer.start(100)

# Show the main window
win.show()

# Start the Qt event loop
app.exec_()
