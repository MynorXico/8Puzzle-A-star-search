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
        InitialState.Cost = InitialState.Heuristics1()

        self.FrontierStates.append(InitialState)
        self.FrontierMatrices.append(InitialState.CurrentBoard)
        self.CostsList.append(InitialState.Cost)
        
        print (timer())
        while(len(self.FrontierStates) != 0):
            if(len(self.VisitedMatrices)%10000 == 0):
                print (len(self.VisitedMatrices))
                print (timer())
            StateIndex = self.CostsList.index(min(self.CostsList))
            self.tmpState = self.FrontierStates.pop(StateIndex)
            self.CostsList.pop(StateIndex)
            self.FrontierMatrices.pop(StateIndex)
            self.VisitedMatrices.append(self.tmpState.CurrentBoard)
            if GoalState.CurrentBoard == self.tmpState.CurrentBoard:
                print (self.tmpState.Path())
                print(str(timer()) + " (" + str(len(self.VisitedMatrices)) + " )")
                return True
            
            self.tmpState.GenerateChildren(self.VisitedMatrices, self.FrontierMatrices, self.FrontierStates, self.CostsList)
        print("False")
        return False
                
