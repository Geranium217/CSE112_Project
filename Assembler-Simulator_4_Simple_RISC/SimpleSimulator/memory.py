


class Memory:
    def __init__(self):
        constant = '0'*16
        self.memory = [ constant for x in range(256) ]
    
    def getData(self,number):
        return self.memory[number]

    def setData(self,number,data):
        self.memory[number] = data
        
    def Load(self):
        from sys import stdin
        counter = 0
        for line in stdin:
            line = line.rstrip('\n')
            self.setData(counter,line)
            counter+=1

    def dump(self):
        for i in self.memory:
            print(i)
