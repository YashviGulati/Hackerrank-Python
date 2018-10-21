if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    
    big=arr[0]
    for i in range(1,n):
        if(big<arr[i]):
            big=arr[i]
    for i in range(n):
        if(big==arr[i]):
            arr[i]=-1
            
    big=arr[0]
    for i in range(1,n):
        if(big<arr[i]):
            big=arr[i]
    print(big)