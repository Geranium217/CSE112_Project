import helper

OVERFLOW_C = ( 2**16 ) - 1

opcodes = { 
'10000': 'A',
'10001': 'A',
'10010': 'B',
'10011': 'C',
'10100': 'D',
'10101': 'D',
'10110': 'A',
'10111': 'C',
'11000': 'B',
'11001': 'B',
'11010': 'A',
'11011': 'A',
'11100': 'A',
'11101': 'C',
'11110': 'C',
'11111': 'E',
'01100': 'E',
'01101': 'E',
'01111': 'E',
'01010': 'F'}




register_binary_map = {
        '000':'R0',
        '001':'R1',
        '010':'R2',
        '011':'R3',
        '100':'R4',
        '101':'R5',
        '110':'R6',
        '111':'FLAGS'}

def type_a(EE,instruction,PC,memory):
    import a_type as a_t

    d = { '10000': a_t.add_i ,
    '10001': a_t.sub_i , 
    '10110': a_t.mul_i ,
    '11010': a_t.xor_i ,
    '11011': a_t.or_i ,
    '11100': a_t.and_i }

    r1 = register_binary_map[ instruction[-9:-6] ]
    r2 = register_binary_map[ instruction[-6:-3] ]
    r3 = register_binary_map[ instruction[-3:] ]


    d[ instruction[:5] ](EE,memory,r1,r2,r3)

    return ( False, PC+1 )


def type_b(EE,instruction,PC,memory):
    import b_type as b_t

    d = { '10010': b_t.mov_i ,
    '11000': b_t.rs_i ,
    '11001': b_t.ls_i }

    r1 = register_binary_map[ instruction[-11:-8] ]
    imm = helper.b2i(instruction[-8:])


    d[ instruction[:5] ](EE,r1,imm)

    EE.RF.reset_flags()

    return ( False, PC+1 )


def type_c(EE,instruction,PC,memory):
    import c_type as c_t

    d = { '10011': c_t.mov_i ,
    '10111': c_t.div_i ,
    '11101': c_t.not_i ,
    '11110': c_t.cmp_i }

    r1 = register_binary_map[ instruction[-6:-3] ]
    r2 = register_binary_map[ instruction[-3:] ]


    d[ instruction[:5] ](EE,r1,r2)


    return ( False, PC+1 )

def type_d(EE,instruction,PC,memory):
    import d_type as d_t

    d = { '10100': d_t.ld_i ,
    '10101': d_t.st_i }

    r1 = register_binary_map[ instruction[-11:-8] ]
    address =  instruction[-8:]

    d[ instruction[:5] ](EE,r1,memory,address)


    EE.RF.reset_flags()

    return ( False, PC+1 )

def type_e(EE,instruction,PC,memory):
    import e_type as e_t

    d = { '11111': e_t.jmp_i ,
            '01100': e_t.jlt_i,
            '01101': e_t.jgt_i,
            '01111': e_t.je_i}


    address =  instruction[-8:] 
    new_pc = d[ instruction[:5] ](EE,PC,address)
    EE.RF.reset_flags()

    return ( False, new_pc )

def type_f(EE,instruction,PC,memory):
    import e_type as e_t
    EE.RF.reset_flags()
    return ( True, PC )

def dispatch(EE,instruction,PC,memory):
    code = instruction[:5]
    f_type = opcodes[code] # dispatch type
    halted , new_pc = dispatch_type[f_type](EE,instruction,PC,memory)

    return (halted,new_pc)

dispatch_type = {
        'A' : type_a,
        'B' : type_b,
        'C' : type_c,
        'D' : type_d,
        'E' : type_e,
        'F' : type_f,
        }
