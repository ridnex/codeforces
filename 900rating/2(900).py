n = int(input())
m =[int(x) for x in input().split(" ")]
m.sort()
sum = 0
for i in m:
    sum += i
sum_2 = 0
cnt = 0
while(sum_2*2<= sum):
    sum_2+= m[-1]
    m.pop()
    cnt+=1
print(cnt)
