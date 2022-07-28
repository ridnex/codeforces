import math
n, m, a =[float(x) for x in input().split()]
l = math.ceil(n/a)
k = math.ceil(m/a)
print(int(l*k))


