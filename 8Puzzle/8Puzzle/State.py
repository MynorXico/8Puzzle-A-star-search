import math
class State(object):
    """ Machine State """

    def __init__(self, Numbers):
        self.CurrentBoard = Numbers[:]
        self.ZeroPosition = self.CurrentBoard.index(0)
        self.Path = ""
    def Heuristics1(self):
        cost = 0
        for i in range(len(self.CurrentBoard)):
           if(i != self.CurrentBoard[i]):
               cost+=1
        return cost
    
    def GenerateChildren(self, VisitedMatrices, FrontierMatrices, FrontierStates, ActualCost, CostsList):
        # Can Move Up
        if(int(self.ZeroPosition / 3)) != 0:
            tmpMatrix = self.MoveUp()
            if (tmpMatrix not in VisitedMatrices):
                tmpState = State(tmpMatrix)
                tmpCost = (ActualCost + 1 + tmpState.Heuristics2())
                tmpState.Path = self.Path + "U"
                if(tmpMatrix not in FrontierMatrices):
                    FrontierMatrices.append(tmpMatrix)
                    FrontierStates.append(tmpState)
                    CostsList.append(tmpCost)
                else:                    
                    stateIndex = FrontierMatrices.index(tmpMatrix)
                    if(CostsList[stateIndex] > tmpCost):
                        FrontierStates[stateIndex] = tmpState
                        CostsList[stateIndex] = tmpCost
        # Can Move Down
        if(int(self.ZeroPosition / 3)) != 2:
            tmpMatrix = self.MoveDown()
            if (tmpMatrix not in VisitedMatrices):
                tmpState = State(tmpMatrix)
                tmpCost = (ActualCost + 1 + tmpState.Heuristics2())
                tmpState.Path = self.Path + "D"
                if(tmpMatrix not in FrontierMatrices):
                    FrontierMatrices.append(tmpMatrix)
                    FrontierStates.append(tmpState)
                    CostsList.append(tmpCost)
                else:                    
                    stateIndex = FrontierMatrices.index(tmpMatrix)
                    if(CostsList[stateIndex] > tmpCost):
                        FrontierStates[stateIndex] = tmpState
                        CostsList[stateIndex] = tmpCost
        # Can Move Left
        if(int(self.ZeroPosition % 3)) != 0:
            tmpMatrix = self.MoveLeft()
            if (tmpMatrix not in VisitedMatrices):
                tmpState = State(tmpMatrix)
                tmpCost = (ActualCost + 1 + tmpState.Heuristics2())
                tmpState.Path = self.Path + "L"
                if(tmpMatrix not in FrontierMatrices):
                    FrontierMatrices.append(tmpMatrix)
                    FrontierStates.append(tmpState)
                    CostsList.append(tmpCost)
                else:                    
                    stateIndex = FrontierMatrices.index(tmpMatrix)
                    if(CostsList[stateIndex] > tmpCost):
                        FrontierStates[stateIndex] = tmpState
                        CostsList[stateIndex] = tmpCost
        # Can Move Right
        if(int(self.ZeroPosition % 3)) != 2:
            tmpMatrix = self.MoveRight()
            if (tmpMatrix not in VisitedMatrices):
                tmpState = State(tmpMatrix)
                tmpCost = (ActualCost + 1 + tmpState.Heuristics2())
                tmpState.Path = self.Path + "R"
                if(tmpMatrix not in FrontierMatrices):
                    FrontierMatrices.append(tmpMatrix)
                    FrontierStates.append(tmpState)
                    CostsList.append(tmpCost)
                else:                    
                    stateIndex = FrontierMatrices.index(tmpMatrix)
                    if(CostsList[stateIndex] > tmpCost):
                        FrontierStates[stateIndex] = tmpState
                        CostsList[stateIndex] = tmpCost
        self.Path = ""

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

    def Heuristics2(self):
        cost = 0
        for i in range(len(self.CurrentBoard)):
           cost += (math.fabs(int(self.CurrentBoard[i]/3)-int(i/3)) + math.fabs(int(self.CurrentBoard[i]%3)-int(i%3)))
        return cost