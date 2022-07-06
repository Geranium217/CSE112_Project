import grammar as g

def test_if_FLAGS(*registers):
    if 'FLAGS' in registers:
        raise Exception(f"FLAGS cannot be used here")

def function_type_a(res,labels,variables):
    opcode_map = {
            'add':'10000',
            'sub':'10001',
            'mul':'10110',
            'xor':'11010',
            'or':'11011',
            'and':'11100' }

    test_if_FLAGS( res['R1'],
            res['R2'],
            res['R3'])


    bin_line = str(opcode_map[ res['INS'] ] ) + '00' 
    bin_line+= g.register_binary_map[ res['R1'] ] + \
            g.register_binary_map[ res['R2'] ] + \
            g.register_binary_map[ res['R3'] ]

    return (0,bin_line)
    
def function_type_b(res,labels,variables):
    opcode_map = {
            'mov':'10010',
            'rs':'11000',
            'ls':'11001' }
    Immediate_value = int( res['IMM'][1] )

    if( Immediate_value > 255 or Immediate_value<0 ):
        raise Exception("Invalid Immediate Value {}".format(Immediate_value) )
    
    test_if_FLAGS( res['R1'])

    bin_line = str(opcode_map[ res['INS'] ] ) +  \
            g.register_binary_map[ res['R1'] ] + \
            binary_number( Immediate_value )

    return (0,bin_line)

def function_type_c(res,labels,variables):
    opcode_map = {
            'mov':'10011',
            'not':'11101',
            'cmp':'11110',
            'div':'10111' }

    if res['INS'] == 'mov':
        test_if_FLAGS(res['R2'])
    else:
        test_if_FLAGS( res['R1'],
                res['R2'])
    
    bin_line = str(opcode_map[ res['INS'] ] ) + '00000' + \
            g.register_binary_map[ res['R1'] ] + \
            g.register_binary_map[ res['R2'] ] 

    return (0,bin_line)

def function_type_d(res,labels,variables):
    opcode_map = {
            'ld':'10100',
            'st':'10101' }

    variable_name = res['MEM']
    if variable_name not in variables.keys():
        if variable_name in labels.keys():
            raise Exception(f"Using label '{variable_name}' instead of a variable")
        else:
            raise Exception(f"Variable '{variable_name}' is not defined")

    test_if_FLAGS(res['R1'])
    
    bin_line = str(opcode_map[ res['INS'] ] ) +\
            g.register_binary_map[ res['R1'] ]

    bin_line = { 'processed' : bin_line ,
            'post': { 'type' : 'D' , 'variable' : variable_name }
            }

    return (1,bin_line)

def function_type_e(res,labels,variables):
    opcode_map = {
            'jmp':'11111',
            'jlt':'01100',
            'jgt':'01101',
            'je':'01111' }

    label_name = res['MEM']
    if label_name not in labels.keys():
        if label_name in variables.keys():
            raise Exception(f"Using variable '{label_name}' instead of a label")
        else:
            raise Exception(f"Label '{label_name}' is not defined")
    
    bin_line = str(opcode_map[ res['INS'] ] ) + '000'
    bin_line = { 'processed' : bin_line ,
            'post': { 'type' : 'E' , 'label' : label_name }
            }
 
    return (1,bin_line)

def function_type_f(res,labels,variables):
    opcode_map = {
            'hlt':'01010' }
    
    bin_line = str(opcode_map[ res['T_F'] ] ) + '0'*11

    return (0,bin_line)



function_map = {
        'T_A': function_type_a,
        'T_B': function_type_b,
        'T_C': function_type_c,
        'T_D': function_type_d,
        'T_E': function_type_e,
        'T_F': function_type_f}

def binary_number(number:int):
    n = bin(number)[2:]
    n = n.rjust(8,'0')
    return n

def post_process( assembly:list , labels:dict , variables:dict ):
    hlt_pos = len(assembly)-1
    final_assembly = []
    for line in assembly:
        if( line[0] ):
            new_line = line[1]['processed']
            if line[1]['post']['type'] == 'E':
                label_name = line[1]['post']['label']
                new_line += binary_number(labels[label_name])
            elif line[1]['post']['type'] == 'D':
                variable_name = line[1]['post']['variable']
                variable_address = hlt_pos + variables[variable_name]
                new_line += binary_number(variable_address)
            final_assembly.append(new_line)
        else:
            final_assembly.append(line[1])

    return final_assembly

