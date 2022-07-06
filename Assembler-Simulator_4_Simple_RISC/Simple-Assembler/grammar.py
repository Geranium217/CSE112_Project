import pyparsing as pp

registers = pp.one_of(["R0",
                        "R1",
                        "R2",
                        "R3",
                        "R4",
                        "R5",
                        "R6",
                        "FLAGS"])

immediate = '$' + pp.Word(pp.nums + '-').leave_whitespace() \
        #White Spaces Aren't Allowed Between $ and number

mem_addr = pp.Word(pp.alphas)

label = pp.Word(pp.alphanums).set_results_name('LAB')
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

non_label_expr = type_a ^ type_b ^ type_c ^ type_d ^ type_e ^ type_f
label_declaration = label_decl + non_label_expr

def delabel(s,loc,tok):
    label_name = tok['LAB']
    label_length = len(label_name)+1
    types = { 'T_A','T_B','T_C','T_D','T_E','T_F' } 
    for t in types:
        if t in tok.keys():
            tok['TYPE'] = t
            return


label_declaration = label_declaration.set_parse_action(delabel)

expr = non_label_expr ^ label_declaration 
final_expr = expr ^ var_def ^ empty_line

register_binary_map = {
        'R0':'000',
        'R1':'001',
        'R2':'010',
        'R3':'011',
        'R4':'100',
        'R5':'101',
        'R6':'110',
        'FLAGS':'111'}

