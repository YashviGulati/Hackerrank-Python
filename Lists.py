if __name__ == '__main__':
    N = int(raw_input())
    l=[]
    for i in range(N):
        a=(raw_input())
        a=a.split()
        if a[0]=="insert":
            pos=int(a[1])
            val=int(a[2])
            l.insert(pos,val)
            
        elif a[0]=="print":
            print(l)
                
        elif a[0]== "append":
            val=int(a[1])
            l.append(val)
            
        elif a[0]== "sort":
            l=sorted(l)
            
        elif a[0]== "remove":
            val=int(a[1])
            l.remove(val)
        
        elif a[0]== "pop":
            k=int(len(l))
            l.remove(l[k-1])
        
        elif a[0]== "reverse":
            l.reverse()