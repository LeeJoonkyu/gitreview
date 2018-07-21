def sum_digit(num):
    sum=0
    while num>=10: #1000 이면 1000 100 10 1까지 진행되고 1에서 탈출
        #등호 빠지면 에러
        sum+=num%10
        num//=10
    sum+=num #1을 더해줌.
    return sum

sum2=0
for x in range(1,1001):
    sum2+=sum_digit(x)
print(sum2)

#힌트 참고 후
# def sum_digit(num):
#     sum=0
#     num = str(num)
#     for i in range(len(num)):
#         sum+=int(num[i])
#     return sum
# sum2=0
# for x in range(1,1001):
#     sum2+=sum_digit(x)
# print(sum2)
