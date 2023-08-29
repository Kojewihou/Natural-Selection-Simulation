import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle, Polygon
import numpy as np

def visualize(roundResults, boundaryRadius, frameRate):
    """
    Visualize the simulation results using animations.

    This function creates an animation to visualize the simulation results.

    Parameters:
    - roundResults: Results of the simulation round containing organism and food data.
    - boundaryRadius (float): The radius of the circular boundary.
    - frameRate (int): The number of frames per second.
    """

    organismArray, foodArray = roundResults
    time_steps = organismArray.shape[2]

    fig, ax = plt.subplots()

    fig.set_facecolor("#009dc4")
    fig.canvas.setWindowTitle("Natural Selection Simulator - Round {1}")

    wood = Circle((0, 0), boundaryRadius, fill=True, color='green', ec="#C2B280", linewidth=20, alpha=1)
    home = Circle((0, 0), boundaryRadius * 0.2, fill=True, color='yellow', ec="brown", linewidth=2, alpha=1)
    square_center = (0, 0)
    square_side_length = 0.15 * boundaryRadius

    ax.add_patch(wood)
    ax.add_patch(home)

    organismScatter = ax.scatter([], [], c="#F4E3B5", marker='D', label = "Organism")
    foodScatter = ax.scatter([], [], c='darkgreen', marker='o', label='Food')
    ax.set_title('Animated Scatter Plot')
    ax.set_xlim(-boundaryRadius, boundaryRadius)
    ax.set_ylim(-boundaryRadius, boundaryRadius)
    ax.axis("off")
    ax.axis("equal")
    ax.legend(loc='upper right')

    angles = np.linspace(0, 2 * np.pi, 3, endpoint=False)
    x_vertices = 0.2*boundaryRadius * np.cos(angles)
    y_vertices = 0.2*boundaryRadius * np.sin(angles)
    vertices = list(zip(x_vertices, y_vertices))
    house = Polygon(vertices, closed=True, edgecolor='brown', facecolor='yellow', alpha=1)
    ax.add_patch(house)

    # Plot lines from origin to vertices
    for x, y in zip(x_vertices, y_vertices):
        ax.plot([0, x], [0, y], color='brown')


    def animate(frame):
        currentOrganismPositions = organismArray[:, :, frame]
        currentFood = foodArray[:, :, frame]
        currentFood = currentFood[:, ~np.all(np.isnan(currentFood), axis=0)]
        organismScatter.set_offsets(currentOrganismPositions[:2, :].T)
        foodScatter.set_offsets(currentFood[:2, :].T)
        ax.set_title(f'Food Consumed: {int(np.sum(currentOrganismPositions[5,:]))}/{foodArray.shape[1]} - Frame {frame}')

    animation = FuncAnimation(fig, animate, frames=time_steps, interval=1000 / frameRate)

    plt.show()
    plt.close()
    savePath = "C:\\Users\\Elliot\\Documents\\Git\\Natural-Selection-Simulation\\Animations\\Ani.gif"