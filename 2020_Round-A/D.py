class Node:
    def __init__(self):
        self.child = {}
        self.count = 1
class PrefixTree:
    def __init__(self,K):
        self.Root = Node()
        self.Sum = 0
        self.K = K
    def add(self,x):
        current = self.Root
        for i in x:
            if i in current.child:
                current = current.child[i]
                self.Sum -= current.count//self.K
                current.count+=1
                self.Sum += current.count//self.K

            else:
                current.child[i] = Node()
                current = current.child[i]
                self.Sum += 1//self.K

    def Answer(self):
        return self.Sum


for _ in range(int(input())):
    N,K = map(int,input().split())
    
    myTree = PrefixTree(K)
    
    for __ in range(N):
        myTree.add(input())

    print("Case #"+str(_+1)+":",myTree.Answer())