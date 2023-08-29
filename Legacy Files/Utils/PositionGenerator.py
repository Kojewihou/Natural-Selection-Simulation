from random import random
from math import sqrt

def foodSpawnPosition(spawnPoint, foodMinSpawnRadius):
    while True:
        x = random()
        y = random()
        
        # Calculate distance from the center (0.5, 0.5)
        distance = sqrt((x - spawnPoint[0])**2 + (y - spawnPoint[1])**2)
        
        # If the distance is greater than 0.2 (outside the circle), return the position
        if distance > foodMinSpawnRadius:
            return (x, y)

