#!/bin/python

import math
import os
import random
import re
import sys

def solve(s):
    p=s.split()
    l=[]
    for i in range(len(p)):
        if(ord(p[i][0])>=97 and ord(p[i][0])<=122):
            mini=list(p[i])
            mini[0]=chr(ord(mini[0])-32)
            mini="".join(mini)
            l.append(mini)
        else:
            l.append(p[i])
    k="".join(l)
    m=[]
    for i in range(len(s)):
        if(s[i]==' '):
            m.append(0)
        else:
            m.append(1)
    ajeeb=list(k)
    f=[]
    j=0
    for i in range(len(m)):
        if(m[i]==1):
            f.append(ajeeb[j])
            j=j+1
        else:
            f.append(' ')
    f="".join(f)
    return f


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = raw_input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
