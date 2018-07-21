num = 120
cnt = 0
for i in range(1, 121):
    if num % i == 0:
       print(i)
       cnt+=1

print("%d의 약수는 총 %d개입니다."%(num,cnt))