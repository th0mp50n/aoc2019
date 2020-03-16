import copy
import os
from colorama import Fore, init
init(autoreset=True)

f = open("input10test0")

def deepcopy_init(input, init):
    output = copy.deepcopy(input)
    for i in output:
        for j in range(len(i)):
            i[j] = init
    return output

field = []
for line in f.readlines():
    field.append(list(line.rstrip()))

up, right, down, left = (0,1), (1,0), (0,-1), (-1,0)

def inside(a, field):
    if a[0]>=0 and a[0]<len(field[0]) and a[1]>=0 and a[1]<len(field):
        return 1
    else:
        return 0

def move(a, b):
    return (a[0]+b[0], a[1]+b[1])

def moves(a, field):
    result = []
    for dir in (up, right, down, left):
        new = move(a, dir)
        if inside(new, field):
            result.append(new)
    return result

def print_field(field, pos=None):
    os.system('cls')
    for i in range(len(field)):
        for j in range(len(field[0])):
            if pos and i==pos[0] and j==pos[1]:
                print(Fore.GREEN + field[i][j], end='')
            else:
                print(field[i][j], end='')
        print("", end='\n')


scratch = deepcopy_init(field, None)


print_field(field, (0,1))