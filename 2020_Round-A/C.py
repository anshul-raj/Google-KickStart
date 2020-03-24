import math
def fun(array,K):
    s = 1
    e = max(array)
    while (s<e):
        m = (s + e) //2
        sum_value = 0
        for i in array:
            if i > m:
                sum_value+=math.ceil((i/m) - 1)
        if sum_value > K:
            s = m + 1
        else:
            e = m 
    return s

for _ in range(int(input())):
    N,K = map(int,input().split())
    sessions = list(map(int,input().split()))
    myHeap = []
    for i in range(len(sessions)-1):
        dif =  sessions[i+1] - sessions[i]
        myHeap.append(dif)

    ans = fun(myHeap,K)

    print("Case #"+str(_+1)+":",ans)
