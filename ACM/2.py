n = int(input())
output = []
for i in range(n):
    m = int(input())
    len_int = len(str(m))
    list_min = []
    for k in range(0, len_int):
        S = int(str(m)[k])*(10**(len_int-k-1))
        if S!= 0:
            list_min.append(S)
    output.append(len(list_min))
    for j in list_min:
        output.append(j)
            
for j in output:
    print(j)

        
