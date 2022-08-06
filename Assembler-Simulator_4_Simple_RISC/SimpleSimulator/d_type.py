import helper



def ld_i(EE,r1,memory,address):
    n = helper.b2i(address)
    value = memory.getData(n)
    EE.RF.set_register(r1,value)




def st_i(EE,r1,memory,address):
    n = helper.b2i(address)
    v1 = EE.RF.get_register(r1)
    memory.setData(n,v1)


