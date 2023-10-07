n = int(input())
while n>0:
    n -= 1
    k = int(input())
    x1=[str(n) for n in input().split()]
    
    x2=[str(n) for n in input().split()]
    x3=[str(n) for n in input().split()]
    arr = [x1, x2, x3]
    bi = {}
    di = {}
    for i in range(3):
        for j in range(k):
            bi[arr[i][j]]=0
    for i in range(3):
        for j in range(k):
            if bi[arr[i][j]]==1:
                di[arr[i][j]]+=1
            else:
                bi[arr[i][j]]=1
                di[arr[i][j]]=1
    for i in range(3):
        s1 = 0
        for j in range(k):
            if di[arr[i][j]]==1:
                s1+=3
            elif di[arr[i][j]]==2:
                s1+=1
        print(s1, end=" ")
    print()
    

