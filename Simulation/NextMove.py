import numpy as np

def NextMove(organismArray, organismCount, boundaryRadius):
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

    # Reflect off the circular boundary and adjust direction
    distance_from_center = np.sqrt(xPositions**2 + yPositions**2)
    outside_boundary_mask = distance_from_center > boundaryRadius

    # Reflect positions at the boundary
    xPositions[outside_boundary_mask] = (
        xPositions[outside_boundary_mask] /
        distance_from_center[outside_boundary_mask]) * boundaryRadius
    yPositions[outside_boundary_mask] = (
        yPositions[outside_boundary_mask] /
        distance_from_center[outside_boundary_mask]) * boundaryRadius

    # Adjust direction upon boundary reflection
    directions[outside_boundary_mask] = np.arctan2(
        yPositions[outside_boundary_mask], xPositions[outside_boundary_mask])

    # Ensure directions remain within the range [0, 2*pi)
    directions = directions % (2 * np.pi)

    # Add new data to Organism Array
    organismArray = np.concatenate(
        (organismArray, nextMoveArray[:, :, np.newaxis]), axis=2)

    return organismArray