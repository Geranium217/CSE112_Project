import helper
import instructions

class RegisterFile:
    def __init__(self):

        self.registers = {
                "R0":helper.binary_number(0,16),
                "R1":helper.binary_number(0,16),
                "R2":helper.binary_number(0,16),
                "R3":helper.binary_number(0,16),
                "R4":helper.binary_number(0,16),
                "R5":helper.binary_number(0,16),
                "R6":helper.binary_number(0,16)
                }

        self.FLAGS = { 'V':0,
                       'L':0,
                       'G':0,
                       'E':0 }

    
    def set_flags(self,flag):
        self.FLAGS[flag] = 1

    def get_flags(self,flag):
        return True if self.FLAGS[flag] else False 

    def reset_flags(self):
        for k in self.FLAGS.keys():
            self.FLAGS[k] = 0

    def set_register(self,r,value):
        self.registers[r] = value

    def get_all_flag(self):
        x = '0'*12

        x += '1' if self.FLAGS['V'] else '0'
        x += '1' if self.FLAGS['L'] else '0'
        x += '1' if self.FLAGS['G'] else '0'
        x += '1' if self.FLAGS['E'] else '0'
        return x 

    def get_register(self,r):
        return self.registers[r]
    
    def dump(self):
        f = ''
        f += self.registers['R0'] + ' '
        f += self.registers['R1'] + ' '
        f += self.registers['R2'] + ' '
        f += self.registers['R3'] + ' '
        f += self.registers['R4'] + ' '
        f += self.registers['R5'] + ' '
        f += self.registers['R6'] + ' '
        f += self.get_all_flag()
        return f


class ExecutionEngine:
    def __init__(self):
        self.RF = RegisterFile()

    def execute(self,ins,PC,memory):
        halt, new_pc = instructions.dispatch(self,ins,PC,memory)
        return (halt,new_pc)



