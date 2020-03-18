f = open("./input2")

def compute(mem):
    pc = 0
    while True:
        op = mem[pc]
        if  1 > op or op > 2:
            #print("terminated with op {} and pc {}".format(op, pc))
            break
        arg1, arg2, dest = mem[pc+1:pc+4]
        #print(op, arg1, arg2, dest)
        if op == 1:
            mem[dest] = mem[arg1] + mem[arg2]
        if op == 2:
            mem[dest] = mem[arg1] * mem[arg2]
        #print(mem)
        pc = pc + 4
    return mem[0]

mem = list(map(int, f.readline().rstrip().split(",")))
tests = [(a,b) for a in range(0,100) for b in range(0,100)]

for t in tests:
    memc = mem.copy()
    memc[1] = t[0]
    memc[2] = t[1]
    result = compute(memc)
    print("{}\t{}\t{}".format(t[0], t[1], result))
    if result == 19690720:
        break

