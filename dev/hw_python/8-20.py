def mask_security_number(security_number):
    list = []
    for i in security_number:
        list.append(i) #list에 스트링값 잘라서 넣어주기 #하나하나가 스트링으로 들어감
    idx = len(list)-1
    for i in range(idx,idx-4,-1):
        list[i] = "*" #마지막 네자리 *로 변경
    masked_security_num = ""
    for i in range(len(list)):
        masked_security_num += list[i] #변경 된 리스트를 문자열로 변경

    return masked_security_num

print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))

#힌트 참고 후
# def mask_security_number(security_number):
#     idx = len(security_number) - 4
#     masked_security_num = security_number[0:idx] + "****"
#
#     return masked_security_num
#
# print(mask_security_number("880720-1234567"))
# print(mask_security_number("8807201234567"))
# print(mask_security_number("930124-7654321"))
# print(mask_security_number("9301247654321"))
# print(mask_security_number("761214-2357111"))
# print(mask_security_number("7612142357111"))