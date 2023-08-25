import numpy as np

def CollisionDetection(organismArray, foodArray):

    findOrganismPosition = np.vectorize(lambda organismObject: organismObject.currentPosition)
    organismPositionArray = findOrganismPosition(organismArray)

    findOrganismFood = np.vectorize(lambda organismObject: organismObject.size)

    findFoodPosition = np.vectorize(lambda foodObject: foodObject.position)
    foodPositionArray = findFoodPosition(foodArray)