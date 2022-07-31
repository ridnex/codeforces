arr = [4, 7, 44, 77, 47, 74, 444, 447, 477, 474, 744, 747, 777, 774]
str = ""
k = int(input())
for i in arr:
    if k%i==0:
        str+="b"
    else:
        str+="a"
if "b" in str:
    print("YES")
else:
    print("NO")