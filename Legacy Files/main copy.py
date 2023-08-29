import numpy as np
from random import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns

from Objects import Organism, Food
from UI import *
from Utils import CollisionDetection, foodSpawnPosition


def initializeSimulation():


    round = 0

    #Set Initial Conditions
    organismCount = 1000
    foodCount = 200
    spawnPoint = (0.5,0.5)
    foodMinSpawnRadius = 0.2
    minSpeed = 0.001

    #Load UI elements
    LoadUI()

    organismArray = np.empty(organismCount, dtype=object)
    foodArray = np.empty(foodCount, dtype=object)

    #Initialize all organism and food objects
    for i in range(organismCount):
        organismArray[i] = Organism(spawnPoint=spawnPoint, size= np.random.uniform(2,10), speed=np.random.uniform(minSpeed, 10*minSpeed))

    for i in range(foodCount):
        foodArray[i] = Food(foodSpawnPosition(spawnPoint=spawnPoint, foodMinSpawnRadius=foodMinSpawnRadius))

    return organismArray, foodArray

def animatePlots(organismArray, foodArray):

    frame_rate = 60  # Desired frame rate in frames per second
    interval = 1000 / frame_rate  # Interval in milliseconds

    # Create a figure and axis for the plot
    fig, ax = plt.subplots()
    ax.set_title(label="Simulation")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    plotOrganisms = np.vectorize(lambda organism: ax.plot([], [], '8', markersize=organism.size, color="purple")[0])
    organismPlots = plotOrganisms(organismArray)

    def nextMove(organism, organismPlot):
        organism.Move()
        organismPlot.set_data(organism.x, organism.y)

    nextMove = np.vectorize(nextMove)

    def update(frame):
        nextMove(organismArray, organismPlots)
        return organismPlots
    
    simulation = FuncAnimation(fig, update, frames=np.arange(0,100), blit=True, interval=interval)

    plt.show()


if __name__ == "__main__":
    organismArray, foodArray = initializeSimulation()
    animatePlots(organismArray, foodArray)