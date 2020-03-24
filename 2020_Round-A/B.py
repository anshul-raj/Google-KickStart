def fun(stacks,P):
    
    dp  = [[0 for i in range(P+1)]for i in range(len(stacks)+1)]

    for i in range(1,len(stacks)+1):
        for j in range(1,P+1):
            for k in range(1,min(len(stacks[0]),j+1)):
                dp[i][j] = max(dp[i-1][j] , dp[i-1][j-k] + stacks[i-1][k] , dp[i][j])
    
    return dp[N][P]

for _ in range(int(input())):
    N,K,P = map(int,input().split())
    stacks = []
    for i in range(N):
        sumvalue = 0 
        temparray = [0]
        temp = list(map(int,input().split()))
        for i in temp:
            sumvalue+=i
            temparray.append(sumvalue)
        stacks.append(temparray)
    
    ans = fun(stacks,P)

    print("Case #"+str(_+1)+":",ans)
