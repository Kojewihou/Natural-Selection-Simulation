import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle, Rectangle

from Simulation import NextMove, FoodCollision, ConstructOrganismArray, ConstructFoodArray


def RunRound(organismArray, foodArray, frameRate):
    # * Simulation Conditions

    roundLength = organismArray.shape[2]

    foodArrayDisplay = foodArray.copy()

    desired_interval = 2.5  # Desired interval in second
    directionChangeProbability = 1 - \
        np.exp(-1 / (frameRate * desired_interval))

    roundStartTime = time.time()

    for roundNumber in range(1, roundLength):
        start_time = time.time()
        organismArray = NextMove(
            organismArray, roundNumber, boundaryRadius, directionChangeProbability)
        # elapsed_time = time.time() - start_time
        # print(f"Frame-{roundNumber + 1} movement took {elapsed_time:.6f} seconds to simulate.")
        organismArray, foodArray = FoodCollision(
            organismArray, foodArray, roundNumber)
        elapsed_time = time.time() - start_time
        # print( f"Frame-{roundNumber} collision took {elapsed_time:.6f} seconds to simulate.")
        # time.sleep(1)

    elapsedRoundTime = time.time() - roundStartTime

    print(f"Round  took {elapsedRoundTime:.6f} seconds to simulate.")

    percentConsumed = (
        np.sum(organismArray[5, :, -1]) / foodArrayDisplay.shape[1]) * 100
    print(f"Percentage of Food Consumed: {percentConsumed}%")
    return organismArray, foodArrayDisplay


def visualize(tuple, boundaryRadius, frameRate):
    simulationMatrix, foodArray = tuple
    time_steps = simulationMatrix.shape[2]

    fig, ax = plt.subplots()

    wood = Circle((0, 0), boundaryRadius, fill=True,
                  color='green', linewidth=2, alpha=0.5)
    home = Circle((0, 0), boundaryRadius*0.2, fill=True,
                  color='red', linewidth=2, alpha=0.2)
    square_center = (0, 0)  # Square center coordinates (x, y)
    square_side_length = 0.15*boundaryRadius    # Length of each side of the square
    house = Rectangle((square_center[0] - square_side_length/2, square_center[1] - square_side_length/2),
                      square_side_length, square_side_length, fill=True, color='black', linewidth=2)

    ax.add_patch(wood)
    ax.add_patch(home)
    sc = ax.scatter([], [], c='r', marker='D')
    ax.set_title('Animated Scatter Plot')
    ax.set_xlabel('X Position')
    ax.set_ylabel('Y Position')
    # Adjust limits based on your data
    ax.set_xlim(-boundaryRadius, boundaryRadius)
    # Adjust limits based on your data
    ax.set_ylim(-boundaryRadius, boundaryRadius)
    ax.axis("off")

    ax.add_patch(house)

    ax2 = ax.twinx()
    ax2.scatter(foodArray[0, :], foodArray[1, :],
                c='g', marker='8', label='Tree')
    # Adjust limits based on your data
    ax2.set_xlim(-boundaryRadius, boundaryRadius)
    ax2.set_ylim(-boundaryRadius, boundaryRadius)
    ax2.axis("off")  # Adjust limits based on your data
    ax2.legend()

    def animate(frame):
        # Access the 3D matrix for the current time step
        current_positions = simulationMatrix[:, :, frame]
        # Plot the scatter plot with current positions
        sc.set_offsets(current_positions[:2, :].T)
        ax.set_title(
            f'Food Consumed: {np.sum(current_positions[5,:])}  - F{frame}')

    animation = FuncAnimation(
        fig, animate, frames=time_steps, interval=1000/200)
    plt.show()
    plt.close()
    
    path = "C:\\Users\\Elliot\\Documents\\Git\\Natural-Selection-Simulation\\Animations\\round.gif"
    #animation.save(path, writer='pillow', fps=frameRate)


if __name__ == "__main__":
    frameRate = 24
    boundaryRadius = 200
    roundLength = 10
    organismArray = ConstructOrganismArray(
        6000, boundaryRadius, roundLength, frameRate)
    foodArray = ConstructFoodArray(200, boundaryRadius)
    roundResult = RunRound(organismArray, foodArray, frameRate)
    visualize(roundResult, boundaryRadius, frameRate)
