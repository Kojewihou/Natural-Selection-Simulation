import numpy as np

def ConstructOrganismArray(organismCount, boundaryRadius, frameRate):
    roundLength = 60 * frameRate + 1

    properties = ["xPosition", "yPosition",
                  "direction", "speed", "size", "food"]

    organismArray = np.empty((len(properties), organismCount, roundLength))

    organismArray[0, :, 0] = 0  # xPosition
    organismArray[1, :, 0] = 0  # yPosition
    organismArray[2, :, 0] = np.random.uniform(
        0, 2 * np.pi, size=(organismCount))  # Initial Direction
    organismArray[3, :, :] = 1  # Size
    organismArray[4, :, :] = boundaryRadius / (frameRate*10)  # Speed 10s to traverse 50m
    organismArray[5, :, 0] = 0  # Food

    return organismArray