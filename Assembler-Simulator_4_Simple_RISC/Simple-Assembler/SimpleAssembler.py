import processing as proc
import error_handling as err
import grammar as g

if __name__ == '__main__':
    variables = dict()
    var_flag = False
    labels = dict()
    address_counter = 0
    assembly = []

    while address_counter<256:
        line = input()
        try:
            results = g.final_expr.parse_string(line, parseAll=True)
        except Exception as e:
            err.error_handle(e)
            exit()

        if results.get_name() == 'Empty':
            continue
        elif results.get_name() == 'LAB_D':
            label_name = results['LAB']
            if label_name not in labels.keys():
                labels[label_name] = address_counter
            else:
                print("Label Defined Again!")
                exit()
            try:
                binary_line = proc.function_map[ results['TYPE'] ](
                        results,
                        labels,
                        variables)
            except Exception as e:
                print(e)
                exit()
            assembly.append(binary_line)

        elif results.get_name() == 'VAR':
            if not var_flag:
                variables[results['VAR'][1]] = len(variables) + 1
                continue
            else:
                print("Variable not declared at the start")
                print("Program Will Terminate!")
                exit()
        else :
            var_flag = True
            try:
                binary_line = proc.function_map[ results.get_name() ](
                        results,
                        labels,
                        variables)
            except Exception as e:
                print(e)
                exit()
            assembly.append(binary_line)
            if results.get_name() == 'T_F':
                break
        address_counter +=1
    else:
        print("Last Instruction is not hlt!")
        print("Program Will Terminate!")
        exit()




    assembly = proc.post_process( assembly ,
            labels,
            variables)

    for i in assembly:
        print(i)

