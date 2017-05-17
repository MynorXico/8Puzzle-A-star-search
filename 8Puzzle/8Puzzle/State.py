class State(object):
    """ Machine State """

    def __init__(self, Numbers):
        self.CurrentBoard = Numbers[:]
        self.ZeroPosition = self.CurrentBoard.index(0)
        self.Path = ""
        self.Cost = 0;

    def Heuristics1(self):
        cost = 0
        for i in len(self.CurrentBoard):
           if(i != self.CurrentBoard[i]):
               cost+=1
        return cost
    
    def GenerateChildren(self, VisitedMatrices, FrontierMatrices, FrontierStates):
        # Can Move Up
        if(self.ZeroPosition / 3) != 0:
            tmpMatrix = self.MoveUp()
            if not (tmpMatrix in VisitedMatrices):
                tmpState = State(tmpMatrix)
                tmpState.Cost = (self.Cost + 1 + tmpState.Heuristics1())
                tmpState.Path = self.Path + "U"
                if(tmpMatrix in FrontierMatrices):
                    stateIndex = FrontierMatrices.index(tmpMatrix)
                    if(FrontierStates[stateIndex].Cost > tmpState.Cost):
                        FrontierStates[stateIndex].Cost = tmpState.Cost
                else:
                    FrontierMatrices.append(tmpMatrix)
                    FrontierStates.append(tmpState)
           


    def MoveUp(self):
        tmpMatrix = self.CurrentBoard[:]
        tmp = tmpMatrix[self.ZeroPosition]
        tmpMatrix[self.ZeroPosition] = tmpMatrix[self.ZeroPosition-3]
        tmpMatrix[self.ZeroPosition - 3] = tmp;
        return tmpMatrix

    def MoveDown(self):
        tmpMatrix = self.CurrentBoard[:]
        tmp = tmpMatrix[self.ZeroPosition]
        tmpMatrix[self.ZeroPosition] = tmpMatrix[self.ZeroPosition+3]
        tmpMatrix[self.ZeroPosition +3] = tmp;
        return tmpMatrix

    def MoveRight(self):
        tmpMatrix = self.CurrentBoard[:]
        tmp = tmpMatrix[self.ZeroPosition]
        tmpMatrix[self.ZeroPosition] = tmpMatrix[self.ZeroPosition+1]
        tmpMatrix[self.ZeroPosition + 1] = tmp;
        return tmpMatrix

    def MoveLeft(self):
        tmpMatrix = self.CurrentBoard[:]
        tmp = tmpMatrix[self.ZeroPosition]
        tmpMatrix[self.ZeroPosition] = tmpMatrix[self.ZeroPosition-1]
        tmpMatrix[self.ZeroPosition-1] = tmp;
        return tmpMatrix