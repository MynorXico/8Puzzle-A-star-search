class State(object):
    """ Machine State """

    def __init__(self, Numbers):
        self.CurrentBoard = Numbers[:]
        self.ZeroPosition = self.CurrentBoard.index(0)
        self.Path = ""
        self.Cost = 0;

    def Heuristics1(self):
        cost = 0
        for i in range(len(self.CurrentBoard)):
           if(i != self.CurrentBoard[i]):
               cost+=1
        return cost
    
    def GenerateChildren(self, VisitedMatrices, FrontierMatrices, FrontierStates, CostsList):
        # Can Move Up
        if(int(self.ZeroPosition / 3)) != 0:
            tmpMatrix = self.MoveUp()
            if not (tmpMatrix in VisitedMatrices):
                tmpState = State(tmpMatrix)
                tmpState.Cost = (self.Cost + 1 + tmpState.Heuristics1())
                tmpState.Path = self.Path + "U"
                tmpState.ZeroPosition = self.ZeroPosition - 3
                if(tmpMatrix in FrontierMatrices):
                    stateIndex = FrontierMatrices.index(tmpMatrix)
                    if(FrontierStates[stateIndex].Cost > tmpState.Cost):
                        FrontierStates[stateIndex] = tmpState
                        CostsList[stateIndex] = tmpState.Cost
                else:
                    FrontierMatrices.append(tmpMatrix)
                    FrontierStates.append(tmpState)
                    CostsList.append(tmpState.Cost)
        # Can Move Down
        if(int(self.ZeroPosition / 3)) != 2:
            tmpMatrix = self.MoveDown()
            if not (tmpMatrix in VisitedMatrices):
                tmpState = State(tmpMatrix)
                tmpState.Cost = (self.Cost + 1 + tmpState.Heuristics1())
                tmpState.Path = self.Path + "D"
                tmpState.ZeroPosition = self.ZeroPosition + 3
                if(tmpMatrix in FrontierMatrices):
                    stateIndex = FrontierMatrices.index(tmpMatrix)
                    if(FrontierStates[stateIndex].Cost > tmpState.Cost):
                        FrontierStates[stateIndex] = tmpState
                        CostsList[stateIndex] = tmpState.Cost
                else:
                    FrontierMatrices.append(tmpMatrix)
                    FrontierStates.append(tmpState)
                    CostsList.append(tmpState.Cost)
        # Can Move Left
        if(int(self.ZeroPosition % 3)) != 0:
            tmpMatrix = self.MoveLeft()
            if not (tmpMatrix in VisitedMatrices):
                tmpState = State(tmpMatrix)
                tmpState.Cost = (self.Cost + 1 + tmpState.Heuristics1())
                tmpState.Path = self.Path + "L"
                tmpState.ZeroPosition = self.ZeroPosition - 1

                if(tmpMatrix in FrontierMatrices):
                    stateIndex = FrontierMatrices.index(tmpMatrix)

                    if(FrontierStates[stateIndex].Cost > tmpState.Cost):
                        FrontierStates[stateIndex] = tmpState
                        CostsList[stateIndex] = tmpState.Cost
                else:
                    FrontierMatrices.append(tmpMatrix)
                    FrontierStates.append(tmpState)
                    CostsList.append(tmpState.Cost)
        # Can Move Right
        if(int(self.ZeroPosition % 3)) != 2:
            tmpMatrix = self.MoveRight()
            if not (tmpMatrix in VisitedMatrices):
                tmpState = State(tmpMatrix)
                tmpState.Cost = (self.Cost + 1 + tmpState.Heuristics1())
                tmpState.Path = self.Path + "R"
                tmpState.ZeroPosition = self.ZeroPosition + 1
                if(tmpMatrix in FrontierMatrices):
                    stateIndex = FrontierMatrices.index(tmpMatrix)
                    if(FrontierStates[stateIndex].Cost > tmpState.Cost):
                        FrontierStates[stateIndex] = tmpState
                        CostsList[stateIndex] = tmpState.Cost
                else:
                    FrontierMatrices.append(tmpMatrix)
                    FrontierStates.append(tmpState)
                    CostsList.append(tmpState.Cost)


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

    def PrintState(self):
        matrix = []
        list = []
        for i in range(len(self.CurrentBoard)):
            if(i%3 == 0):
                list = []
            if(self.CurrentBoard[i] == 0):
                list.append("*")
            else:
                list.append(str(self.CurrentBoard[i]))
            if(i % 3 == 0):
                matrix.append(list)
    
        for row in matrix:
            print(row)
        print("")
