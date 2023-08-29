import numpy as np

def FoodCollision(organismArray, foodArray, roundNumber):
    """
    Simulate food collision with organisms.

    This function simulates the interaction between organisms and food, updating the organismArray
    and foodArray based on collisions between organisms and nearby food.

    Parameters:
    - organismArray (numpy.ndarray): Array containing information about organisms' positions and properties.
    - foodArray (numpy.ndarray): Array containing information about food positions.
    - roundNumber (int): The current round number.

    Returns:
    - Updated organismArray and foodArray after simulating food collision.
    """

    num_organisms = organismArray.shape[1]

    # Make a copy of the previous round's foodArray
    foodArray[:, :, roundNumber] = foodArray[:, :, roundNumber - 1]

    currentFoodArray = foodArray[:, :, roundNumber]
    valid_food_indices = ~np.all(np.isnan(currentFoodArray), axis=0)
    num_food = np.sum(valid_food_indices)

    org_x = organismArray[0, :, roundNumber]
    org_y = organismArray[1, :, roundNumber]
    org_radius = organismArray[3, :, roundNumber]

    food_x = currentFoodArray[0, valid_food_indices]
    food_y = currentFoodArray[1, valid_food_indices]

    food_consumed_mask = np.zeros(num_food, dtype=bool)

    # Pre-calculate distances only for valid food positions
    distances = np.sqrt((org_x[:, np.newaxis] - food_x) ** 2 + (org_y[:, np.newaxis] - food_y) ** 2)
    food_within_radius = distances <= org_radius[:, np.newaxis]

    for food_index in range(num_food):
        if np.isnan(food_x[food_index]) or np.isnan(food_y[food_index]):
            continue

        if np.any(food_within_radius[:, food_index]):
            org_indices_within_radius = np.where(food_within_radius[:, food_index])[0]
            closest_org_index = org_indices_within_radius[np.argmin(distances[org_indices_within_radius, food_index])]
            if not food_consumed_mask[food_index]:
                organismArray[5, closest_org_index, roundNumber] += 1
                food_consumed_mask[food_index] = True

    # Mask the consumed food positions in currentFoodArray
    currentFoodArray[0, valid_food_indices] = np.where(food_consumed_mask, np.nan, currentFoodArray[0, valid_food_indices])
    currentFoodArray[1, valid_food_indices] = np.where(food_consumed_mask, np.nan, currentFoodArray[1, valid_food_indices])

    size_diff = foodArray.shape[1] - currentFoodArray.shape[1]
    if size_diff > 0:
        nan_columns = np.full((2, size_diff), np.nan)
        currentFoodArray = np.concatenate((currentFoodArray, nan_columns), axis=1)

    foodArray[:, :, roundNumber] = currentFoodArray

    return organismArray, foodArray
