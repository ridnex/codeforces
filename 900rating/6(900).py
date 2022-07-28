n = int(input())

if n!=1:
    arr = [int(x) for x in input().split()]
    cnt = 0
    path = []
    for i in range(n-1):
        if arr[i]<=arr[i+1]:
            cnt+=1
            if i == n-2:
                path.append(cnt)

        else:
            path.append(cnt)
            cnt=0
    path.sort()
    #print(path)
    print(path[-1]+1)
else:
    print(1)