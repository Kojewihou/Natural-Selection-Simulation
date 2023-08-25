import numpy as np
from random import random

from Objects import Organism, Food
from UI import *
from Utils import CollisionDetection, foodSpawnPosition

def main():


    round = 0

    #Set Initial Conditions
    organismCount = 40
    foodCount = 200
    spawnPoint = (0.5,0.5)
    foodMinSpawnRadius = 0.2

    #Load UI elements
    LoadUI()

    organismArray = np.empty(organismCount, dtype=object)
    foodArray = np.empty(foodCount, dtype=object)

    #Initialize all organism and food objects
    for i in range(organismCount):
        organismArray[i] = Organism(spawnPoint=spawnPoint,size= 1, speed=500)

    for i in range(foodCount):
        foodArray[i] = Food(foodSpawnPosition(spawnPoint=spawnPoint, foodMinSpawnRadius=foodMinSpawnRadius))

    

if __name__ == "__main__":
    main()