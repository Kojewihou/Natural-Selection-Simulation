import numpy as np

class Organism ():

    def __init__(self,spawnPoint , size, speedFactor) -> None:
        self.x, self.y = spawnPoint
        self.size = size
        self.speed = speedFactor * (0.001 / 0.0001) ** (1 / (25 - 5)) * (0.001 / size)
        self.direction = np.random.uniform(0,2*np.pi)
        self.food = 0
        self.canSurvive = False
        self.canReproduce = False
        self.roundAge = 0
        print(self.size, self.speed)

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
        # Update the position based on speed and direction
        self.x += self.speed * np.cos(self.direction)
        self.y += self.speed * np.sin(self.direction)

        # Reflect off the x-axis boundary
        if self.x < 0:
            self.x = -self.x
            self.direction = np.pi - self.direction
        elif self.x > 1:
            self.x = 2 - self.x
            self.direction = np.pi - self.direction

        # Reflect off the y-axis boundary
        if self.y < 0:
            self.y = -self.y
            self.direction = -self.direction
        elif self.y > 1:
            self.y = 2 - self.y
            self.direction = -self.direction
            
        # Update the position again after potential reflection
        self.x += self.speed * np.cos(self.direction)
        self.y += self.speed * np.sin(self.direction)
        
        # Ensure direction remains within the range [0, 2*pi)
        self.direction = self.direction % (2 * np.pi)
    
    
    
