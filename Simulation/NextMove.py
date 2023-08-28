import numpy as np


def NextMove(organismArray, roundNumber, organismCount, boundaryRadius):
    current_data = organismArray[:, :, roundNumber].copy()
    nextMoveArray = current_data.copy()

    xPositions = current_data[0, :]
    yPositions = current_data[1, :]
    directions = current_data[2, :]
    speeds = current_data[4, :]

    # Update the direction for some organisms
    random_mask = np.random.rand(organismCount) < 0.05
    directions[random_mask] += np.random.uniform(-np.pi / 4, np.pi / 4, size=sum(random_mask))

    # Update x and y positions based on speed and direction
    xPositions += speeds * np.cos(directions)
    yPositions += speeds * np.sin(directions)

    # Reflect off the circular boundary
    distance_from_center = np.sqrt(xPositions**2 + yPositions**2)
    outside_boundary_mask = distance_from_center > boundaryRadius

    # Reverse direction for organisms outside the boundary
    directions[outside_boundary_mask] += np.pi

    # Update positions for boundary reflection
    xPositions[outside_boundary_mask] = (
        xPositions[outside_boundary_mask] /
        distance_from_center[outside_boundary_mask]) * boundaryRadius
    yPositions[outside_boundary_mask] = (
        yPositions[outside_boundary_mask] /
        distance_from_center[outside_boundary_mask]) * boundaryRadius

    # Ensure directions remain within the range [0, 2*pi)
    directions = directions % (2 * np.pi)

    # Update nextMoveArray
    nextMoveArray[0, :] = xPositions
    nextMoveArray[1, :] = yPositions
    nextMoveArray[2, :] = directions
    organismArray[:, :, roundNumber + 1] = nextMoveArray

    return organismArray
