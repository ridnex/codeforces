n = int(input())
output = []
for i in range(n):
    a = int(input())
    str1 = str(input())
    if a!=5 :
        output.append("NO")
    else:
        arr =list(str1)
        arr.sort()
        if arr == ['T', 'i', 'm', 'r', 'u']:
            output.append("YES")
        else:
            output.append("NO")
for j in output:
    print(j)
