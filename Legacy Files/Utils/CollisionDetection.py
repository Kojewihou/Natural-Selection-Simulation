import numpy as np
from itertools import product

def CollisionDetection(foodArray, organismArray):
    for organism, food in product(organismArray, foodArray):
        if is_collision(organism, food):
            organism.EatsFood()

def is_collision(organism, food):
    distance = np.sqrt((food.x - organism.x)**2 + (food.y - organism.y)**2)
    return distance <= (food.size + organism.size)