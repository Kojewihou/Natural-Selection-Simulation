import numpy as np

def ConstructFoodArray(foodCount, boundaryRadius, roundLength, frameRate):
    """
    Construct an array containing randomly generated food positions.

    This function generates an array containing random food positions for each round of a simulation.

    Parameters:
    - foodCount (int): The number of food items to generate.
    - boundaryRadius (float): The radius of the circular boundary.
    - roundLength (int): The number of rounds in the simulation.
    - frameRate (int): The number of frames per round.

    Returns:
    - foodArray (numpy.ndarray): Array containing randomly generated food positions.
    """

    roundLength = roundLength * frameRate + 1

    # Generate random angles (polar coordinates)
    angles = np.random.uniform(0, 2 * np.pi, foodCount)

    # Generate random radii within the boundary radius
    radii = np.random.uniform(
        0.25 * boundaryRadius, 0.9 * boundaryRadius, foodCount)

    # Convert polar coordinates to Cartesian coordinates
    x_positions = radii * np.cos(angles)
    y_positions = radii * np.sin(angles)

    foodArray = np.empty(shape=(2, foodCount, roundLength))

    # Create the foodArray
    foodArray[:, :, 0] = np.vstack((x_positions, y_positions))

    return foodArray

if __name__ == "__main__":
    ConstructFoodArray(100, 50, 100, 30)
