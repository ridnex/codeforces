a, b = input().split(" ")
l = (int(a)+1)//2
if int(b)<=l:
    print(int(b)*2-1)
else:
    print((int(b)-l)*2)