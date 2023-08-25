class Organism ():

    def __init__(self, spawnPoint, size, speed) -> None:
        self.currentPosition = spawnPoint
        self.size = size
        self.speed = speed
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
        pass
    
    
    
