import numpy as np

# * Simulation Conditions
frameRate = 60
roundLength = 60 * frameRate

# * The Arena Conditions
boundaryLength = 100  # 100x100 box

# * The Organism Generation
organismCount = 100
properties = ["xPosition", "yPosition", "direction", "speed", "size", "food"]

organismArray = np.empty((len(properties), organismCount, 1))


organismArray[0, :] = boundaryLength/2  # xPosition
organismArray[1, :] = boundaryLength/2  # yPosition
organismArray[2, :] = np.random.uniform(
    0, 2 * np.pi, size=(organismCount, 1))  # Direction
organismArray[3, :] = 5  # Size
organismArray[4, :] = boundaryLength/(frameRate*5)  # Speed
organismArray[5, :] = 0  # Food


def nextMove(organismArray):
    # Copy Most Recent Layer
    nextMoveArray = organismArray[:, :, -1].copy()

    xPositions = nextMoveArray[0, :]
    yPositions = nextMoveArray[1, :]
    directions = nextMoveArray[2, :]
    speeds = nextMoveArray[4, :]

    # Apply the rules to each organism using array operations
    # Update the direction for some organisms
    random_mask = np.random.rand(organismCount) < 0.005
    
    directions[random_mask] = 2 * np.pi * np.random.rand(sum(random_mask))

    # Update x and y positions based on speed and direction
    xPositions += speeds * np.cos(directions)
    yPositions += speeds * np.sin(directions)

    # Reflect off the boundaries
    xPositions[xPositions < 0] = -xPositions[xPositions < 0]
    xPositions[xPositions > boundaryLength] = (
        2*boundaryLength) - xPositions[xPositions > boundaryLength]
    yPositions[yPositions < 0] = -yPositions[yPositions < 0]
    yPositions[yPositions > boundaryLength] = (
        2*boundaryLength) - yPositions[yPositions > boundaryLength]

    # Ensure directions remain within the range [0, 2*pi)
    directions = directions % (2 * np.pi)

    # Add new data to Organism Array
    organismArray = np.concatenate(
        (organismArray, nextMoveArray[:, :, np.newaxis]), axis=2)

    return organismArray

for roundNumber in range(roundLength):
    organismArray = nextMove(organismArray)
print(organismArray.shape)
print(organismArray[:, :, -1].astype(int))
print(organismArray[:, :, 0].astype(int))
