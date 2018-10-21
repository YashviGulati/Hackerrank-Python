def swap_case(s):
    p=s
    k=[]
    for i in range(1,len(p)+1):
        val=ord(p[i-1:i])
        if(ord(p[i-1:i])>=65 and ord(p[i-1:i])<=90):
            k.append(chr(ord(p[i-1:i])+32))
            
        elif(ord(p[i-1:i])>=97 and ord(p[i-1:i])<=122):
            k.append(chr(ord(p[i-1:i])-32))
        else:
            k.append(p[i-1:i])
            
    k= ''.join(k)
    return k

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result