#password must be 8 characters long with at least 1 symbol

from random import randint
import random

def mySolution():
    pw = []
    for x in range(8):
        char1 = chr(randint(33,122))
        pw.append(char1)
        
    result = "".join(pw)
    return result


def realSolution():
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    passlen = 8
    p = "".join(random.sample(s,passlen))

    return p


print(mySolution())

print(realSolution())
