# 测测你属什么的
year = eval(input("请输入出生年份:"))
dealyear = year % 12
if dealyear == 0:
    print("monkey")
elif dealyear == 1:
    print("rooster")
elif dealyear == 2:
    print("dog")
elif dealyear == 3:
    print("pig")
elif dealyear == 4:
    print("rat")
elif dealyear == 5:
    print("ox")
elif dealyear == 6:
    print("tiger")
elif dealyear == 7:
    print("rabbit")
elif dealyear == 8:
    print("dragon")
elif dealyear == 9:
    print("snake")
elif dealyear == 10:
    print("horse")
else:
    print("sheep")
