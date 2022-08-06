
def binary_number(number:int,width):
    n = bin(number)[2:]
    n = n.rjust(width,'0')
    return n

def b2i(strin):
    n  = 0
    for i in enumerate(strin[::-1]):
        n +=   (2**i[0])*int(i[1])
    return n
