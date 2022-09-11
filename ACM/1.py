n = int(input())
output= []
for i in range(n):
    m = int(input())
    str1 = str(input())
    str2 = str(input())
    x = str1.replace("G", "B")
    y = str2.replace("G", "B")
    if x == y:
        output.append('YES')
    else:
        output.append("NO")
for j in output:
    print(j)