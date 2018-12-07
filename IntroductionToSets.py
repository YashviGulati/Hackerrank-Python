def average(array):
    sum=0
    setarray=set(array)
    for i in setarray:
        sum=sum+i
    return sum/len(setarray)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)