import random
import copy

def share_dia(x0,y0,x1,y1):
    dx = abs(y1-y0)
    dy = abs(x1-x0)
    return dx == dy

def has_queen(bs,c):
    for i in range(c):
        if share_dia(i,bs[i],c,bs[c]):
            return True
    return False

def has_clashes(the_board):
    for col in range(1,len(the_board)):
        if has_queen(the_board, col):
            return True
    return False

a1=[]
a2=[]
num_found = 0

while num_found <= 92:
    rng = random.Random()
    bd = list(range(8))
    rng.shuffle(bd)
    a2=copy.deepcopy(bd)
    if not has_clashes(a2)  and  a2 not in a1:
        a1.append(a2)
        print("Found solution",a2)
        tries =0
        num_found+=1
