if __name__ == '__main__':
    s = raw_input()
    k=0
    for i in range(1,len(s)):
        v1=(s[i-1:i]).isalnum()
        if(bool(v1)==True):
            print(bool(v1))
            k=k+1
            break
    if(k==0):
        print('False')
    k=0
    for i in range(1,len(s)):
        v1=(s[i-1:i]).isalpha()
        if(bool(v1)==True):
            print(bool(v1))
            k=k+1
            break
    if(k==0):
        print('False')
    k=0
    for i in range(1,len(s)):
        v1=(s[i-1:i]).isdigit()
        if(bool(v1)==True):
            print(bool(v1))
            k=k+1
            break
    if(k==0):
        print('False')
    k=0
    for i in range(1,len(s)):
        v1=(s[i-1:i]).islower()
        if(bool(v1)==True):
            print(bool(v1))
            k=k+1
            break
    if(k==0):
        print('False')
    k=0
    for i in range(1,len(s)):
        v1=(s[i-1:i]).isupper()
        if(bool(v1)==True):
            print(bool(v1))
            k=k+1
            break
    if(k==0):
        print('False')