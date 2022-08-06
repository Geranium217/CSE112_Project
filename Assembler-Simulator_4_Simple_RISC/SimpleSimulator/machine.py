
import memory
import engine

class Machine:
    def __init__(self):
        self.Memory = memory.Memory()
        self.EE = engine.ExecutionEngine()
        self.RF = self.EE.RF
        

    def execute(self,instruction,PC):
        return self.EE.execute(instruction,PC,self.Memory)


