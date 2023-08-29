import numpy as np

def FoodCollision(organismArray, foodArray, roundNumber):
    num_organisms = organismArray.shape[1]
    num_food = foodArray.shape[1]

    org_x = organismArray[0, :, roundNumber]
    org_y = organismArray[1, :, roundNumber]
    org_radius = organismArray[3, :, roundNumber]
    food_x = foodArray[0, :]
    food_y = foodArray[1, :]

    # Create a mask to track which food items have been consumed
    food_consumed_mask = np.zeros(num_food, dtype=bool)

    for food_index in range(num_food):
        food_x_pos = food_x[food_index]
        food_y_pos = food_y[food_index]

        distances = np.sqrt((org_x - food_x_pos)**2 + (org_y - food_y_pos)**2)
        food_within_radius = distances <= org_radius

        if np.any(food_within_radius):
            org_indices_within_radius = np.where(food_within_radius)[0]
            closest_org_index = org_indices_within_radius[np.argmin(distances[org_indices_within_radius])]
            if not food_consumed_mask[food_index]:  # Check if the food item hasn't been consumed
                organismArray[5, closest_org_index, roundNumber] += 1
                food_consumed_mask[food_index] = True  # Mark food as consumed

    # Create a new foodArray without the consumed food
    new_foodArray = foodArray[:, ~food_consumed_mask]

    return organismArray, new_foodArray
