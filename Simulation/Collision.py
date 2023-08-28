import numpy as np

import numpy as np

def FoodCollision(organismArray, foodArray, roundNumber):
    num_organisms = organismArray.shape[1]
    num_food = foodArray.shape[1]

    org_x = organismArray[0, :, roundNumber]
    org_y = organismArray[1, :, roundNumber]
    org_radius = organismArray[3, :, roundNumber]
    food_x = foodArray[0, :]
    food_y = foodArray[1, :]

    distances = np.sqrt((org_x[:, np.newaxis] - food_x)**2 + (org_y[:, np.newaxis] - food_y)**2)

    # Create a mask to track which food items have been consumed
    food_consumed_mask = np.zeros(num_food, dtype=bool)

    for org_index in range(num_organisms):
        food_within_radius = distances[org_index] <= org_radius[org_index]
        if np.any(food_within_radius):
            closest_food = np.argmin(distances[org_index])
            if food_within_radius[closest_food]:
                organismArray[5, org_index, roundNumber] += 1
                food_within_radius[closest_food] = False  # Mark food as consumed
                food_consumed_mask[closest_food] = True  # Update overall mask

    # Create a new foodArray without the consumed food
    new_foodArray = foodArray[:, ~food_consumed_mask]

    return organismArray, new_foodArray
