a = int(input())
b = int(input())
c = int(input())
arr = []
arr.append(a+b+c)
arr.append(a*b*c)
arr.append(a+b*c)
arr.append(a*b+c)
arr.append((a+b)*c)
arr.append(a*(b+c))
arr.sort()
print(arr[-1])

