n, m=input().split(" ")
n=int(n)
m=int(m)
arr = [int(x) for x in input().split(" ")]
arr.sort()
list = []
for i in range(m-n+1):
    list.append(arr[i+n-1]-arr[i])
list.sort()
print(list[0])