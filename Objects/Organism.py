import numpy as np

class Organism ():

    def __init__(self,spawnPoint , size, speed) -> None:
        self.x, self.y = spawnPoint
        self.size = size
        self.speed = speed
        self.direction = np.random.uniform(0,2*np.pi)
        self.food = 0
        self.canSurvive = False
        self.canReproduce = False
        self.roundAge = 0

    def __str__(self) -> str:
        return f"Organism => Pos: {self.currentPosition}, Age: {self.roundAge}, Food: {self.food}"

    def EatsFood(self):
        self.food +=1
        self.canSurvive = self.food > 1
        self.canReproduce = self.food > 2

    def RoundReset(self):
        self.food = 0
        self.canSurvive = False
        self.canReproduce = False
    
    def Move(self):
        self.x += self.speed * np.cos(self.direction)
        self.y += self.speed * np.sin(self.direction)

        # Reverse direction if out of bounds
        if self.x < 0 or self.x > 1:
            reflection_x = np.pi - self.direction
            self.direction = reflection_x + np.random.uniform(-np.pi/4, np.pi/4)
        if self.y < 0 or self.y > 1:
            reflection_y = -self.direction
            self.direction = reflection_y + np.random.uniform(-np.pi/4, np.pi/4)
        
        self.x += self.speed * np.cos(self.direction)
        self.y += self.speed * np.sin(self.direction)
        self.direction = self.direction % (2 * np.pi)
    
    
    
