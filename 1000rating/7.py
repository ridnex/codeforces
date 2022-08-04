#Драконы
s, n = [int(x) for x in input().split(" ")]
arr = []
condition = True
for i in range(n):
    x, y = [int(x) for x in input().split(" ")]
    arr.append([x, y])
arr.sort()
for i in arr:
    if s> i[0]:
        s = s + i[1]
    else:
        condition = False

if condition == False:
    print("NO")
else:
    print("YES")
