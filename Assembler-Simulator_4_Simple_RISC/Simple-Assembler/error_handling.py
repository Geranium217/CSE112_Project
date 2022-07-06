import grammar as g

registers = {
        'reg1':1,
        'reg2':2,
        'reg3':3}






def error_handle(e:Exception):
    line = e.line
    tokens = line.split()
    if ':' in line:
        if ':' in tokens[0]:
            line = ' '.join(tokens[1:])
            tokens = tokens[1:]
        else:
            print("No Spaces allowed between label and ':' ")
            return
    try:
        g.non_label_expr.parse_string(line,parse_all=True)
    except Exception as e:
        problem = e.parser_element().name
        if problem == 'ins':
            if len(tokens)>=1:
                print(f"{tokens[0]} is not a valid instruction")
            else:
                print(f"instruction not supplied")
        elif problem in ['reg1','reg2','reg3']:
            reg_pos = registers[problem]
            if len(tokens)>=reg_po:
                reg = tokens[ 
                    reg_po ]
                print(f"{reg} is not a valid register")
            else:
                print(f"Not Enough Registers supplied")
        elif problem == "'$'":
            print(f"{tokens[2]} is not a valid register")
        else:
            print("General Syntax Error")
