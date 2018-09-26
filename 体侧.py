# pytho磅和英寸测体重
weight = eval(input("输入你的体重："))
height = eval(input("输入你的身高："))
a = 0.45359237
b = 0.0254
c = weight * a
d = height * b
e = c / (d * d)
print("标准是:", format(e, ".2f"))
if e < 18.5:
    print("偏瘦")
elif e < 25:
    print("正常")
elif e < 30:
    print("偏胖")
else:
    print("肥胖")
