import helper

def mov_i(EE,r1,r2):
    v1 = EE.RF.get_register(r1)
    EE.RF.set_register(r2,v1)
    EE.RF.reset_flags()


def div_i(EE,r1,r2):
    v1 = helper.b2i(EE.RF.get_register(r1))
    v2 = helper.b2i(EE.RF.get_register(r2))

    r = r1%r2
    q = r1//r2

    v_r = helper.binary_number(r,16)
    v_q = helper.binary_number(q,16)

    EE.RF.set_register('R1',v_r)
    EE.RF.set_register('R0',v_q)
    EE.RF.reset_flags()


def not_i(EE,r1,r2):
    v1 = EE.RF.get_register(r1)

    z = ''

    for i in v1:
        if int(i):
            z+='0'
        else:
            z+='1'


    EE.RF.set_register(r2,z)
    EE.RF.reset_flags()


def cmp_i(EE,r1,r2):
    v1 = helper.b2i(EE.RF.get_register(r1))
    v2 = helper.b2i(EE.RF.get_register(r2))

    if v1 < v2:
        EE.RF.set_flags('L')
    elif v1 > v2:
        EE.RF.set_flags('G')
    elif v1 == v2:
        EE.RF.set_flags('E')
