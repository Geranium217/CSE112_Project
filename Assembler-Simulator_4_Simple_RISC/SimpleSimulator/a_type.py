import helper

OVERFLOW_C = (2**16)-1

def add_i(EE,memory,r1,r2,r3):
    v1 = helper.b2i(EE.RF.get_register(r1))
    v2 = helper.b2i(EE.RF.get_register(r2) )

    v3 = v1+v2

    if(  v3  > (OVERFLOW_C) ):
        EE.RF.set_flags('V')
    else:
        EE.RF.reset_flags()

    v3 = v3 % (OVERFLOW_C+1)

    v3 = helper.binary_number(v3,16)

    EE.RF.set_register(r3,v3)

def sub_i(EE,memory,r1,r2,r3):
    v1 = helper.b2i(EE.RF.get_register(r1))
    v2 = helper.b2i(EE.RF.get_register(r2) )

    v3 = v1 - v2

    if( v2 > v1 ):
        EE.RF.set_flags('V')
        v3 = 0
    else:
        EE.RF.reset_flags()

    v3 = helper.binary_number(v3,16)
    EE.RF.set_register(r3,v3)


def mul_i(EE,memory,r1,r2,r3):
    v1 = helper.b2i(EE.RF.get_register(r1))
    v2 = helper.b2i(EE.RF.get_register(r2) )

    v3 = v1*v2

    if(  v3  > (OVERFLOW_C) ):
        EE.RF.set_flags('V')
    else:
        EE.RF.reset_flags()
    v3 = v3 % (OVERFLOW_C + 1) 
    v3 = helper.binary_number(v3,16)
    EE.RF.set_register(r3,v3)
    



def xor_i(EE,memory,r1,r2,r3):
    v1 = EE.RF.get_register(r1)
    v2 = EE.RF.get_register(r2)

    v3 = ''

    for i in zip(v1,v2):
        if int(i[0]) ^ int(i[1]) :
            v3+='1'
        else:
            v3+='0'
    EE.RF.reset_flags()
    EE.RF.set_register(r3,v3)



def or_i(EE,memory,r1,r2,r3):
    v1 = EE.RF.get_register(r1)
    v2 = EE.RF.get_register(r2)

    v3 = ''

    for i in zip(v1,v2):
        if int(i[0]) | int(i[1]) :
            v3+='1'
        else:
            v3+='0'
    EE.RF.set_register(r3,v3)
    EE.RF.reset_flags()

def and_i(EE,memory,r1,r2,r3):
    v1 = EE.RF.get_register(r1)
    v2 = EE.RF.get_register(r2)

    v3 = ''

    for i in zip(v1,v2):
        if int(i[0]) & int(i[1]) :
            v3+='1'
        else:
            v3+='0'
    EE.RF.set_register(r3,v3)
    EE.RF.reset_flags()
