import numpy as np
import time

from Simulation import ConstructOrganismArray, ConstructFoodArray, visualize, RunRound


def main():
    frameRate = 60
    boundaryRadius = 100
    roundLength = 30
    organismArray = ConstructOrganismArray(30, boundaryRadius, roundLength, frameRate)
    foodArray = ConstructFoodArray(80, boundaryRadius, roundLength, frameRate)
    roundResult = RunRound(organismArray, foodArray, boundaryRadius, frameRate)
    organismArray, foodArray = roundResult

    visualize(roundResult, boundaryRadius, frameRate)


if __name__ == "__main__":
    main()