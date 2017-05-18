from timeit import default_timer as timer
import State

class Solver(object):
    """ 8 Puzzle Solver"""
    
    def __init__(self, **kwargs):
        self.FrontierStates = []
        self.ExpandedNodes = 0
        self.FrontierMatrices = []
        self.VisitedMatrices = []
        self.ZeroPosition = 0
        self.tmpState = 0
        self.CostsList = []

    def Solve(self, Numbers):
        GoalState = State.State([0,1,2,3,4,5,6,7,8])
        
        InitialState = State.State(Numbers[:])
        InitialState.ZeroPosition = Numbers.index(0)

        self.FrontierStates.append(InitialState)
        self.FrontierMatrices.append(InitialState.CurrentBoard)
        self.CostsList.append(InitialState.Heuristics2())
        
        while(len(self.FrontierStates) != 0):
            StateIndex = self.CostsList.index(min(self.CostsList))

            self.tmpState = self.FrontierStates.pop(StateIndex)
            ActualCost = self.CostsList.pop(StateIndex)
            self.FrontierMatrices.pop(StateIndex)

            self.VisitedMatrices.append(self.tmpState.CurrentBoard)
            if GoalState.CurrentBoard == self.tmpState.CurrentBoard:
                return self.tmpState.Path
            
            self.tmpState.GenerateChildren(self.VisitedMatrices, self.FrontierMatrices, self.FrontierStates, ActualCost, self.CostsList)
        print("False")
        return False
                
