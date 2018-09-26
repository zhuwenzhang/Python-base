# 输入年利率
annualInterestRate = eval(input("请输入相关年利率（%）："))
monthlyInterestRate = annualInterestRate / 1200

# 输入年
numberOfYears = eval(input("请输入几年："))

# 输入借的钱
loanAmount = eval(input("请输入借的钱："))

# 算出结果
monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
totalPayment = monthlyPayment * numberOfYears * 12

# 输出结果
print("每个月要还：", int(monthlyPayment * 100) / 100, "元")
print("一共要还：", int(totalPayment * 100) / 100, "元")
