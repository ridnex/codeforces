a = int(input())
arr = []
for i in range(a):
    arr.append(list(int(s) for s in input().split(" ") ))
x, y, z = 0, 0, 0
for i in range(a):
    x+=arr[i][0]
    y+=arr[i][1]
    z+=arr[i][2]
if x==0 and y==0 and z==0:
        print("YES")
else:
    print("NO")


