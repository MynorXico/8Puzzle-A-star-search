import Solver
import State
import time
import os
import Report
from threading import Thread
from timeit import default_timer as timer

import winsound
Freq = 2500 # Set Frequency To 2500 Hertz
Dur = 5000 # Set Duration To 1000 ms == 1 second

clear = lambda: os.system('cls')

Numbers = input("Ingrese los números de izquierda a derecha de arriba hacia abajo separados por una coma:\n").split(",")
Numbers = list(map(int, Numbers))
s = Solver.Solver()
timer()
solution = s.Solve(Numbers)
t = timer()
s = State.State(Numbers)
s.PrintState()
for i in solution:
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
print(str(t)+ "segundos")
#winsound.Beep(Freq,Dur)
Report.WriteReport(t)