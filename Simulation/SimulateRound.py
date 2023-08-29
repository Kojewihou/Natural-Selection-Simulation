import numpy as np
import time

from .NextMove import NextMove
from .Collision import FoodCollision

def RunRound(organismArray, foodArray, boundaryRadius, frameRate):
    """
    Run a simulation round for organisms interacting with food.

    This function simulates the interaction between organisms and food for a given number of rounds.

    Parameters:
    - organismArray (numpy.ndarray): Array containing information about organisms' properties and positions.
    - foodArray (numpy.ndarray): Array containing information about food positions.
    - frameRate (int): The number of frames per second.

    Returns:
    - Updated organismArray and foodArray after simulating the round.
    """

    roundLength = organismArray.shape[2]

    foodArrayDisplay = foodArray.copy()

    desired_interval = 2.5  # Desired interval in seconds
    directionChangeProbability = 1 - np.exp(-1 / (frameRate * desired_interval))

    roundStartTime = time.time()

    for roundNumber in range(1, roundLength):
        start_time = time.time()
        organismArray = NextMove(organismArray, roundNumber, boundaryRadius, directionChangeProbability)
        organismArray, foodArray = FoodCollision(organismArray, foodArray, roundNumber)
        elapsed_time = time.time() - start_time
        # Uncomment the following line to print simulation time for each frame
        # print(f"Frame-{roundNumber} simulation took {elapsed_time:.6f} seconds.")

    elapsedRoundTime = time.time() - roundStartTime

    print(f"Round took {elapsedRoundTime:.6f} seconds to simulate.")

    percentConsumed = (np.sum(organismArray[5, :, -1]) / foodArrayDisplay.shape[1]) * 100
    print(f"Percentage of Food Consumed: {percentConsumed}%")
    return organismArray, foodArray