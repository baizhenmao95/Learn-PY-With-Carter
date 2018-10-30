class AI:
    def __init__(self):
        self.isFirstTurn = True
    def turn(self):
        if self.isFirstTurn:
            self.robot.turnLeft()
            self.isFirstTurn = False
        elif self.robot.lookInFront() == "bot":
            self.robot.attack()
        else:
            self.robot.doNothing()
