def calculate_change(payment, cost):
    # 코드를 작성하세요.
    diff = payment - cost
    fifty = diff // 50000
    diff %= 50000

    ten = diff // 10000
    diff %= 10000

    five = diff // 5000
    diff %= 5000

    one = diff // 1000
    diff %= 1000

    print("50000원 지폐: %d장" % fifty)
    print("10000원 지폐: %d장" % ten)
    print("5000원 지폐: %d장" % five)
    print("1000원 지폐: %d장" % one)

# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)