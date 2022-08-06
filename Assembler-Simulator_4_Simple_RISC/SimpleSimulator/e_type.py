import helper



def jmp_i(EE,PC,address):
    new_pc = helper.b2i(address)
    return new_pc

def jlt_i(EE,PC,address):

    if EE.RF.get_flags('L'):
        new_pc = helper.b2i(address)
    else:
        new_pc = PC+1

    return new_pc

def jgt_i(EE,PC,address):
    if EE.RF.get_flags('G'):
        new_pc = helper.b2i(address)
    else:
        new_pc = PC+1

    return new_pc



def je_i(EE,PC,address):
    if EE.RF.get_flags('E'):
        new_pc = helper.b2i(address)
    else:
        new_pc = PC+1

    return new_pc
