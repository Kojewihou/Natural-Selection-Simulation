import numpy as np

def distance(x1, y1, x2, y2):
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def FoodCollision(OrganismArray, foodArray):
    num_organisms = OrganismArray.shape[1]
    num_food = foodArray.shape[1]

    org_x = OrganismArray[0, :, -1]
    org_y = OrganismArray[1, :, -1]
    org_radius = OrganismArray[3, :, -1]
    food_x = foodArray[0, :]
    food_y = foodArray[1, :]

    # Calculate distances using broadcasting
    distances = np.sqrt((org_x[:, np.newaxis] - food_x)**2 + (org_y[:, np.newaxis] - food_y)**2)

    # Mask of food items to be consumed
    food_consumed_mask = distances <= org_radius[:, np.newaxis]

    # Increment foodScore for each organism
    OrganismArray[5, :, -1] += np.sum(food_consumed_mask, axis=1)

    # Create a new foodArray without the consumed food
    new_foodArray = foodArray[:, ~np.any(food_consumed_mask, axis=0)]

    return OrganismArray, new_foodArray
