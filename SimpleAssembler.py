import pyparsing as pp

registers = pp.one_of(["R0",
                        "R1",
                        "R2",
                        "R3",
                        "R4",
                        "R5",
                        "R6"])

flags = pp.Literal("FLAGS")
immediate = '$' + pp.Word(pp.nums) 
immediate = immediate.leave_whitespace()
mem_addr = pp.Word(pp.nums)
label = pp.Word(pp.alphas)

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
                    "ls"]).set_results_name("INS").set_name("ins") \
        + immediate.set_results_name("IMM").set_name("Imm")

type_b = type_b.set_results_name("T_B")
                    
type_c = pp.one_of(["mov",
                    "and"] ).set_results_name("INS").set_name("ins") \
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


expr = type_a ^ type_b ^ type_c ^ type_d ^ type_e ^ type_f


def ex(s):
    try:
            z = expr.parse_string(s)
    except Exception as e:
            return e
    return z
