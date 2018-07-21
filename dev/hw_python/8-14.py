num = [2, 4, 6, 8, 10, 12, 14]
# for i in range(len(num) // 2):
#     temp = num[i]
#     num[i] = num[len(num) - 1 - i]
#     num[len(num) - 1 - i] = temp
# print(num)

#left + right 가 len-1이 되도록
# 2.
# right_idx = len(num)-1
# for i in range(int(len(num)/2)):
#     left_idx = i
#     temp = num[left_idx]
#     num[left_idx] = num[right_idx - left_idx]
#     num[right_idx - left_idx] = temp
# print(num)

for left_idx in range(int(len(num)/2)):
    right_idx = len(num) - left_idx -1
    temp = num[left_idx]
    num[left_idx] = num[right_idx]
    num[right_idx] = temp
print(num)