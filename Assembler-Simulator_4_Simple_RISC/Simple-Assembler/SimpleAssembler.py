import pyparsing as pp
import types

registers = pp.one_of(["R0",
                        "R1",
                        "R2",
                        "R3",
                        "R4",
                        "R5",
                        "R6",
                        "FLAGS"])


immediate = '$' + pp.Word(pp.nums).leave_whitespace() 

mem_addr = pp.Word(pp.alphas)

label = pp.Word(pp.alphas).set_results_name('LAB')
label_decl = label + ':'
label_decl = label_decl.leave_whitespace()
label_decl = label_decl.set_results_name('LAB_D')

type_a = pp.one_of(["add",
                    "sub",
                    "mul",
                    "xor",
                    "or",
                    "and"] ).set_results_name("INS").set_name("ins") + \
        registers.set_results_name("R1").set_name("reg1") +  \
        registers.set_results_name("R2").set_name("reg2") +  \
        registers.set_results_name("R3").set_name("reg3") \

type_a = type_a.set_results_name("T_A")

type_b = pp.one_of(["mov",
                    "rs",
                    "ls"]).set_results_name("INS").set_name("ins") \
        + registers.set_results_name("R1").set_name("reg1") \
        + immediate.set_results_name("IMM").set_name("Imm")

type_b = type_b.set_results_name("T_B")
                    
type_c = pp.one_of(["mov",
                    "not",
                    "cmp",
                    "div"] ).set_results_name("INS").set_name("ins") \
        + registers.set_results_name("R1").set_name("reg1") \
        + registers.set_results_name("R2").set_name("reg2") 

type_c = type_c.set_results_name("T_C")

type_d = pp.one_of(["ld",
                    "st"]).set_results_name("INS") \
        + registers.set_results_name("R1").set_name("reg1") \
        + mem_addr.set_results_name("MEM").set_name("mem")

type_d = type_d.set_results_name("T_D")


type_e = pp.one_of(["jmp",
                    "jgt",
                    "jlt"]).set_results_name("INS").set_name("ins") \
        + mem_addr.set_results_name("MEM").set_name("mem")
type_e = type_e.set_results_name("T_E")


type_f = pp.one_of(["hlt"]).set_results_name("INS").set_name('ins')
type_f = type_f.set_results_name("T_F")


var_def = pp.Literal("var") + pp.Word(pp.alphas)
var_def = var_def.set_results_name("VAR")

empty_line = pp.Empty().set_results_name("Empty")

expr = type_a ^ type_b ^ type_c ^ type_d ^ type_e ^ type_f
expr = expr ^ ( label_decl + expr ) 
expr = expr ^ var_def ^ empty_line



register_binary_map = {
        'R0':'000',
        'R1':'001',
        'R2':'010',
        'R3':'011',
        'R4':'100',
        'R5':'101',
        'R6':'110',
        'FLAGS':'111'}


def function_type_a(res):
    opcode_map = {
            'add':'10000',
            'sub':'10001',
            'mul':'10110',
            'xor':'11010',
            'or':'11011',
            'and':'11100' }
    bin_line = str(opcode_map[ res['INS'] ] ) + '00' 
    bin_line+= register_binary_map[ res['R1'] ] + \
            register_binary_map[ res['R2'] ] + \
            register_binary_map[ res['R3'] ]

    return (0,bin_line)
    
def function_type_b(res):
    opcode_map = {
            'mov':'10010',
            'rs':'11000',
            'ls':'11001' }
    Immediate_value = int( res['IMM'][1] )

    if( Immediate_value > 255 or Immediate_value<0 ):
        raise Exception("Invalid Immediate Value {}".format(Immediate_value) )
    
    bin_line = str(opcode_map[ res['INS'] ] ) + '000' + bin(Immediate_value)[2:] 

    return (0,bin_line)

def function_type_c(res):
    opcode_map = {
            'mov':'10011',
            'not':'11101',
            'cmp':'11110',
            'div':'10111' }
    
    bin_line = str(opcode_map[ res['INS'] ] ) + '00000' + \
            register_binary_map[ res['R1'] ] + \
            register_binary_map[ res['R2'] ] 

    return (0,bin_line)

def function_type_d(res):
    opcode_map = {
            'ld':'10100',
            'st':'10101' }
    
    bin_line = str(opcode_map[ res['INS'] ] ) +\
            register_binary_map[ res['R1'] ] + \
            get_mem_addr(res['MEM'])

    return (1,bin_line)

def function_type_e(res):
    opcode_map = {
            'jmp':'11111',
            'jlt':'01100',
            'jgt':'01101',
            'je':'01111' }
    
    bin_line = str(opcode_map[ res['INS'] ] ) + '000' + \
            register_binary_map[ res['R1'] ] + \
            get_label_address(res['MEM'])

    return (1,bin_line)

def function_type_f(res):
    opcode_map = {
            'hlt':'01010' }
    
    bin_line = str(opcode_map[ res['INS'] ] ) + '0'*11

    return (0,bin_line)


if __name__ == '__main__':
    variables = dict()
    var_flag = 0
    labels = dict()
    address_counter = 0
    assembly = []

    while address_counter<256:
        line = input()
        try:
            results = expr.parse_string(line, parseAll=True)
        except:
            print("General Syntax Error")
            print("Terminating")
            exit()
    
        if 'LAB_D' not in results.keys():
            binary_line = function_map(results['INS'])
