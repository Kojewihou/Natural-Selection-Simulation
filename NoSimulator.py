import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from Simulation import NextMove, FoodCollision

frameRate = 5


def runRound():
    # * Simulation Conditions

    roundLength = 60 * frameRate + 1

    # * The Arena Conditions
    boundaryRadius = 50  # 100x100 box

    # * The Organism Generation
    organismCount = 1000
    properties = ["xPosition", "yPosition",
                  "direction", "speed", "size", "food"]

    organismArray = np.empty((len(properties), organismCount, roundLength))

    organismArray[0, :, 0] = 0  # xPosition
    organismArray[1, :, 0] = 0  # yPosition
    organismArray[2, :, 0] = np.random.uniform(
        0, 2 * np.pi, size=(organismCount))  # Initial Direction
    organismArray[3, :, :] = 1  # Size
    organismArray[4, :, :] = boundaryRadius / \
        (frameRate*10)  # Speed 10s to traverse 50m
    organismArray[5, :, 0] = 0  # Food

    # * Food Generation

    foodCount = 200
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
    foodArrayDisplay = foodArray.copy()

    for roundNumber in range(roundLength-1):
        start_time = time.time()
        organismArray = NextMove(
            organismArray, roundNumber, organismCount, boundaryRadius)
        organismArray, foodArray = FoodCollision(
            organismArray, foodArray, roundNumber + 1)
        elapsed_time = time.time() - start_time
        # print(f"Frame-{roundNumber + 1} took {elapsed_time:.6f} seconds to simulate.")

    percentConsumed = np.sum(organismArray[5, :, -1])/foodCount * 100
    print(f"Percentage of Food Consumed: {percentConsumed}%")
    return organismArray, foodArrayDisplay


def visualize(tuple):
    simulationMatrix = tuple[0]
    foodArray = tuple[1]
    time_steps = simulationMatrix.shape[2]
    fig, ax = plt.subplots()
    sc = ax.scatter([], [], c='b', marker='D')
    ax.set_title('Animated Scatter Plot')
    ax.set_xlabel('X Position')
    ax.set_ylabel('Y Position')
    ax.set_xlim(-55, 55)  # Adjust limits based on your data
    ax.set_ylim(-55, 55)  # Adjust limits based on your data

    ax2 = ax.twinx()
    ax2.scatter(foodArray[0, :], foodArray[1, :],
                c='r', marker='x', label='Tree')
    ax2.legend()

    def animate(frame):
        # Access the 3D matrix for the current time step
        current_positions = simulationMatrix[:, :, frame]
        # Plot the scatter plot with current positions
        sc.set_offsets(current_positions[:2, :].T)
        ax.set_title(
            f'Food Consumed: {np.sum(current_positions[5,:])}  - F{frame}')

    animation = FuncAnimation(
        fig, animate, frames=time_steps, interval=1000/frameRate)

    plt.show()


if __name__ == "__main__":
    visualize(runRound())
