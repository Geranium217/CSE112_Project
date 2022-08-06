import helper



def hlt_i(EE,PC,memory,address):
    n = helper.b2i(address)
    value = memory.getData(n)

    value = helper.binary_number(value,8)

    new_pc = value
    return new_pc



