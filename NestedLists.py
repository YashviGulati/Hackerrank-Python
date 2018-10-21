import sys
a=[]
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    a.append([name,score])
small=a[0][1]
i=1
for i in range(int(len(a))):
    if(small>a[i][1]):
        small=a[i][1]
        
for i in range(int(len(a))):
    if(small==a[i][1]):
        a[i][1]=sys.maxsize

small=a[0][1]
b=[]
i=1
for i in range(int(len(a))):
    if(small>a[i][1]):
        small=a[i][1]

for i in range(int(len(a))):
    if(small==a[i][1]):
        b.append(a[i][0])
b=sorted(b)
for i in range(int(len(b))):
    print(b[i])