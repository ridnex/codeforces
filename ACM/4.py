n = int(input())
output = []
for i in range(n):
    m = int(input())
    list1 = [str(x) for x in input().split()]
    list2 = [str(x) for x in input().split()]
    list3 = [str(x) for x in input().split()]
    cnt1=0
    cnt2=0
    cnt3=0
    big_list = list1 + list2 +list3
    new_list = []
    for i in big_list:
        k = big_list.count(i) 
        if k == 3 :
            new_list.append(0)
        elif k == 2 :
            new_list.append(1)
        else:
            new_list.append(3)
    
    for i in range(0, m):
        cnt1+=new_list[i]
    for i in range(m, 2*m):
        cnt2+=new_list[i]
    for i in range(2*m, 3*m):
        cnt3+=new_list[i]
       
    output.append([cnt1, cnt2, cnt3])

for i in range(n):
    for j in range(3):
        print(output[i][j], end = " ")
    print()

    

        

    
    