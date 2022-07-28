n = int(input())
if n>=0:
    print(n)
else:
    m  = -1* n
    d = m % 10
    k = (m %100 - d)//10
    if k>=d :
        sum = (m - k*10)//10 + d
        print(-1 * sum)
    else:
        sum = m // 10
        print(-1*sum)