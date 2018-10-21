def mutate_string(string, position, character):
    k=[]
    
    for i in range(1,len(string)+1):
        k.append(string[i-1:i])
    k[position]=character
    k="".join(k)
    return k

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new