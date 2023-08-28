import numpy as np
import time

from Simulation import NextMove, FoodCollision

def main():
    # * Simulation Conditions
    frameRate = 60
    roundLength = 60 * frameRate

    # * The Arena Conditions
    boundaryRadius = 50  # 100x100 box

    # * The Organism Generation
    organismCount = 500
    properties = ["xPosition", "yPosition", "direction", "speed", "size", "food"]

    organismArray = np.empty((len(properties), organismCount, 1))


    organismArray[0, :] = 0  # xPosition
    organismArray[1, :] = 0  # yPosition
    organismArray[2, :] = np.random.uniform(
        0, 2 * np.pi, size=(organismCount, 1))  # Direction
    organismArray[3, :] = 1  # Size
    organismArray[4, :] = boundaryRadius/(frameRate*5)  # Speed
    organismArray[5, :] = 0  # Food

    # * Food Generation

    foodCount = 150
    # Generate random angles (polar coordinates)
    angles = np.random.uniform(0, 2 * np.pi, foodCount)

    # Generate random radii within the boundary radius
    radii = np.sqrt(np.random.uniform(
        0.3*boundaryRadius, boundaryRadius**2, foodCount))

    # Convert polar coordinates to Cartesian coordinates
    x_positions = radii * np.cos(angles)
    y_positions = radii * np.sin(angles)

    # Create the foodArray
    foodArray = np.vstack((x_positions, y_positions))


    for roundNumber in range(roundLength):
        start_time = time.time()
        organismArray = NextMove(organismArray, organismCount, boundaryRadius)
        organismArray, foodArray = FoodCollision(organismArray, foodArray)
        elapsed_time = time.time() - start_time
        print(f"Frame-{roundNumber} took {elapsed_time:.6f} seconds to simulate.")
    print(organismArray[:, :, -1].astype(str), "\n\n\n")
    print(organismArray[:, :, 0].astype(str))

if __name__ == "__main__":
    main()