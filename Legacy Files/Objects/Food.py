class Food ():

    def __init__(self, position, value=1, risk=0) -> None:
        
        self.x = position[0]
        self.y = position[1]
        self.size = 1
        self.value = value
        self.risk = 0