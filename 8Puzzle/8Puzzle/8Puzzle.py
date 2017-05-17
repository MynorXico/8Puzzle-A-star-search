import Solver
import State
import time
import os
from threading import Thread
import winsound
Freq = 2500 # Set Frequency To 2500 Hertz
Dur = 5000 # Set Duration To 1000 ms == 1 second


clear = lambda: os.system('cls')

Numbers =[4,8,5,6,7,0,3,1,2]
s = Solver.Solver()
solution = s.Solve(Numbers)

s = State.State(Numbers)
s.PrintState()
for i in solution:
    time.sleep(1)
    s.ZeroPosition = s.CurrentBoard.index(0)
    if(i == "U"):
        s.CurrentBoard = s.MoveUp()
    elif(i == "D"): 
        s.CurrentBoard = s.MoveDown()
    elif(i == "L"):
        s.CurrentBoard = s.MoveLeft()
    elif(i == "R"):
        s.CurrentBoard = s.MoveRight()
    s.PrintState()
 
print(solution)
winsound.Beep(Freq,Dur)

