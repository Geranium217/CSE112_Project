import helper

def mov_i(EE,r1,imm):
    v_r = '0'*8
    v_r+= helper.binary_number( imm , 8 )
    EE.RF.set_register(r1,v_r)


def rs_i(EE,r1,imm):
    v1 = helper.b2i(EE.RF.get_register(r1))

    v_r = ( v1 >> imm ) % 16 
    v_r = helper.binary_number( v_r , 16)

    EE.RF.set_register(r1,v_r)

def ls_i(EE,r1,imm):
    v1 = EE.RF.get_register(r1)

    v1 = v1[imm:]
    v1 = v1.ljust(16,'0')


    EE.RF.set_register(r1,v_1)

