number = eval(input("请输入一个数:"))
if number % 2 == 0 and number % 3 == 0:
    print("朱文章哈哈哈")
if number % 2 == 0 or number % 3 == 0:
    print("william chu")
if (number % 2 == 0 or number % 3 == 0) and not (number % 2 == 0 and number % 3 == 0):
    print("嘿嘿嘿")
