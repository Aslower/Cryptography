table = {}
arc_table = {}

table[0] = 1
arc_table[1] = 0

for i in range(1, 255):
    table[i] = (table[i-1] << 1) ^ table[i-1]
    if(table[i] & 0x100): table[i] ^= 0x11b

    arc_table[ table[i] ] = i
#乘法
def multiplication(x ,y):
    if((not x) or (not y)): return 0
    return table[ (arc_table[x] + arc_table[y]) % 255 ]
#除法
def division(x, y):
    inverse = table[ (255 - arc_table[y]) % 255 ]
    return multiplication(x, inverse)



