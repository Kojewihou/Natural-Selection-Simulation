import numpy as np

def NextMove(organismArray, roundNumber, boundaryRadius, directionChangeProbability):
    """
    Update organism positions and directions for the next round.

    This function updates the positions and directions of organisms for the next round based on their
    current positions, directions, speeds, and the specified boundary radius.

    Parameters:
    - organismArray (numpy.ndarray): Array containing information about organisms' positions and properties.
    - roundNumber (int): The current round number.
    - boundaryRadius (float): The radius of the circular boundary.
    - directionChangeProbability (float): Probability of changing direction for each organism.

    Returns:
    - Updated organismArray after computing the next move.
    """

    organismArray[:, :, roundNumber] = organismArray[:, :, roundNumber - 1]
    currentFrameData = organismArray[:, :, roundNumber]

    organismCount = organismArray.shape[1]

    xPositions = currentFrameData[0, :]
    yPositions = currentFrameData[1, :]
    directions = currentFrameData[2, :]
    speeds = currentFrameData[4, :]

    # Update the direction for some organisms
    random_mask = np.random.rand(organismCount) < directionChangeProbability
    directions[random_mask] += np.random.choice([-np.pi / 4, np.pi / 4], p=[0.5, 0.5])

    # Update x and y positions based on speed and direction
    xPositions += speeds * np.cos(directions)
    yPositions += speeds * np.sin(directions)

    # Reflect off the circular boundary
    distance_from_center = np.sqrt(xPositions**2 + yPositions**2)
    outside_boundary_mask = distance_from_center > boundaryRadius

    # Reverse direction for organisms outside the boundary
    directions[outside_boundary_mask] += np.pi

    # Update positions for boundary reflection
    xPositions[outside_boundary_mask] = (xPositions[outside_boundary_mask] /
                                          distance_from_center[outside_boundary_mask]) * boundaryRadius
    yPositions[outside_boundary_mask] = (yPositions[outside_boundary_mask] /
                                          distance_from_center[outside_boundary_mask]) * boundaryRadius

    # Ensure directions remain within the range [0, 2*pi)
    directions = directions % (2 * np.pi)

    return organismArray
