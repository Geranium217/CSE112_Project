# from memory import memory
# from execution_engine import execution_engine as EE
# from pc import PC

import helper
from machine import Machine as m
Machine = m()
Machine.Memory.Load() # Load from stdin

PC = 0

halted = False # Machine is currently running

while (not halted):
    ins =  Machine.Memory.getData(PC)
    halted , new_pc = Machine.execute(ins,PC)
    
    print(f"{helper.binary_number(PC,8)} ",end='')
    print(Machine.RF.dump())
    PC = new_pc

Machine.Memory.dump()
