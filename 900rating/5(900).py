n = int(input())
m = [int(x) for x in input().split(" ")]
m.sort()
for i in m:
    print(i, end=" ")