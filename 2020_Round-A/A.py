for _ in range(int(input())):
    N,B = map(int,input().split())
    array = sorted(list(map(int,input().split())))
    sumvalue = 0
    ans = 0
    for i in range(N):
        sumvalue+=array[i]
        if sumvalue > B:
            sumvalue-=array[i]
            break
        ans+=1
    print("Case #"+str(_+1)+":",i)