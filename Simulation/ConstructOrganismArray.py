import numpy as np

def ConstructOrganismArray(organismCount, boundaryRadius, roundLength, frameRate):
    """
    Construct an array containing properties of organisms for simulation.

    This function generates an array containing properties of organisms for each round of a simulation.

    Parameters:
    - organismCount (int): The number of organisms to generate.
    - boundaryRadius (float): The radius of the circular boundary.
    - roundLength (int): The number of rounds in the simulation.
    - frameRate (int): The number of frames per round.

    Returns:
    - organismArray (numpy.ndarray): Array containing properties of organisms.
    """

    roundLength = roundLength * frameRate + 1

    properties = ["xPosition", "yPosition", "direction", "speed", "size", "food"]

    organismArray = np.empty((len(properties), organismCount, roundLength))

    organismArray[0, :, 0] = 0  # xPosition
    organismArray[1, :, 0] = 0  # yPosition
    organismArray[2, :, 0] = np.random.uniform(
        0, 2 * np.pi, size=(organismCount))  # Initial Direction
    organismArray[3, :, :] = 2  # Size
    organismArray[4, :, :] = boundaryRadius / (frameRate * 10)  # Speed 10s to traverse 50m
    organismArray[5, :, 0] = 0  # Food

    print(organismArray.shape)
    return organismArray
