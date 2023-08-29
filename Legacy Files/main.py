import pyqtgraph as pg
import numpy as np
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget

from Objects import Organism, Food
from Utils import CollisionDetection, foodSpawnPosition


frame_rate = 60  # Desired frame rate in frames per second
interval = 1000 / frame_rate  # Interval in milliseconds


def InitializeSimulationConditions():
    #Set Initial Conditions
    organismCount = 300
    foodCount = 50
    spawnPoint = (0.5,0.5)
    foodMinSpawnRadius = 0.2

    organismArray = np.empty(organismCount, dtype=object)
    foodArray = np.empty(foodCount, dtype=object)

    #Initialize all organism and food objects
    for i in range(organismCount):
        organismArray[i] = Organism(spawnPoint=spawnPoint, size= np.random.uniform(5,25), speedFactor=5)

    for i in range(foodCount):
        foodArray[i] = Food(foodSpawnPosition(spawnPoint=spawnPoint, foodMinSpawnRadius=foodMinSpawnRadius))

    return organismArray, foodArray




def Main(rounds=10):
    # Create a Qt application
    simulator = QApplication([])

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

    organismArray, foodArray = InitializeSimulationConditions()
    
    organismArrayX = np.array([organism.x for organism in organismArray])
    organismArrayY = np.array([organism.y for organism in organismArray])
    size_data = np.array([organism.size for organism in organismArray])
    organismScatter = pg.ScatterPlotItem(x=organismArrayX, y=organismArrayY, size=size_data)

    foodArrayX = np.array([food.x for food in foodArray])
    foodArrayY = np.array([food.y for food in foodArray])
    foodScatter = pg.ScatterPlotItem(x=foodArrayX, y=foodArrayY, size=6)

    simulationPlot.addItem(foodScatter)
    simulationPlot.addItem(organismScatter)

    simulationPlot.setXRange(0,1)
    simulationPlot.setYRange(0,1)
    simulationPlot.setBackground((126, 196, 136))

    color = QColor(255, 0, 0)  # Red color (RGB values)
    brush = QBrush(color)
    organismScatter.setBrush(brush)

    color = QColor(0, 0, 255)  # Red color (RGB values)
    brush = QBrush(color)
    foodScatter.setBrush(brush)

    def UpdateSimulationPlot():

        nextMove = np.vectorize(lambda x: x.Move())
        nextMove(organismArray)

        CollisionDetection(foodArray, organismArray)

        organismArrayX = np.array([obj.x for obj in organismArray])
        organismArrayY = np.array([obj.y for obj in organismArray])

        organismScatter.setData(x=organismArrayX, y=organismArrayY)
        organismScatter.setSize(size=size_data)

    pass

    timer = QTimer()
    timer.timeout.connect(UpdateSimulationPlot)
    timer.start(int(interval))

    # Show the main window
    win.show()

    # Start the Qt event loop
    simulator.exec_()

if __name__ == "__main__":
    Main(10)